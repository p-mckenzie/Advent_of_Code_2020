def main():
    with open('day21.txt', 'r') as f:
        txt = f.read().strip()
        
    f.close()

    from re import findall
    from collections import defaultdict

    mapping = defaultdict(list) # store allergen:[{ingredients}, {ingredients}]
    overall = set() # store set of all ingredients

    for food in txt.split('\n'):
        ingredients, contains = food.split(' (')
        for allergen in findall(r'\w+', contains.split(maxsplit=1)[1]):
            mapping[allergen].append(set(ingredients.split()))
            overall = overall.union(set(ingredients.split()))
            
    # identify which ingredients couldn't have allergens
    allergen_free = overall.copy()
    for allergen, ingreds in mapping.items():
        # whatever ingredient appears in all foods with a certain allergen are options to contain
        has_allergen = set.intersection(*ingreds)
        
        # these can't be allergy-free!
        allergen_free -= has_allergen
        
        # overwrite to only keep the valid options (now mapping maps allergen:{suspicious ingredients})
        mapping[allergen] = has_allergen
        
    # part 1 - inert ingredients
    allergen_free_counts = {x:0 for x in allergen_free}

    # count how many times each inert ingredient occurs in foods
    for food in txt.split('\n'):
        ingredients, contains = food.split(' (')
        for ingredient in ingredients.split():
            try:
                allergen_free_counts[ingredient] += 1
            except KeyError:
                pass
            
    print(sum(allergen_free_counts.values()))

    # part 2 - guilty ingredients, sorted by allergen
    run = True
    while run:
        # iterate through as many times as needed to remove single options from other allergens
        run = False
        for key, val in mapping.items():
            if len(val)==1:
                for key2, val2 in mapping.items():
                    if key2!=key:
                        mapping[key2] = val2-val
            else:
                run = True
                
    # sort alphabetically by allergen
    print(','.join([mapping[x].pop() for x in sorted(mapping.keys())]))
    

if __name__=='__main__':
    main()
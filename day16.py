def main():
    with open('day16.txt', 'r') as f:
        txt = f.read().strip()
    f.close()
    
    rules, mine, nearby = txt.split('\n\n')

    from re import findall
    rule_names = [x.split(':')[0] for x in rules.split('\n')]

    rules = [[int(x) for x in findall('\d+', rule)] for rule in rules.split('\n')]
    mine = [int(x) for x in mine.split('\n')[1].split(',')]
    nearby = [[int(x) for x in findall('\d+', rule)] for rule in nearby.split('\n')[1:]]
    
    invalid_sum = 0 # adds up the invalid values
    invalid_tickets = set() # stores the IDs of invalid tickets

    for ticket_num, ticket in enumerate(nearby):
        for field_ID in range(len(ticket)):
            field_valid = False
            for rule in rules:
                # each field_ID must be valid for at least one rule_ID
                # otherwise, that field_ID is invalid
                field_valid = field_valid or (rule[0]<=ticket[field_ID] and ticket[field_ID]<=rule[1]) or (rule[2]<=ticket[field_ID] and ticket[field_ID]<=rule[3])
            
            if not field_valid:
                invalid_sum += ticket[field_ID]
                invalid_tickets.add(ticket_num)
                
    # part 1
    print(invalid_sum)
    
    # map field_ID to the possibilities for rule_ID
    rule_options = {}
    for field_ID in range(len(mine)):
        rule_options[field_ID] = list(range(len(rules)))
        
    # include only tickets identified as valid in part 1, and our ticket
    valid_tickets = [x for i,x in enumerate(nearby) if i not in invalid_tickets]
    valid_tickets.append(mine)

    winners = {} # will store field_ID:rule_ID pairs as they are identified

    while len(winners)<len(rule_options):
        # iterate through tickets multiple times, eliminating where possible
        
        for ticket in valid_tickets:
            for field_ID in range(len(mine)):
                field = ticket[field_ID]

                # for each field value, check all the rules and retain only those still valid
                rule_options[field_ID] = [rule_option for rule_option in rule_options[field_ID] if (
                    (rules[rule_option][0]<=field and field<=rules[rule_option][1])
                      or (rules[rule_option][2]<=field and field<=rules[rule_option][3]))]

                # if there's only one rule ID left for this field ID, keep it
                if len(rule_options[field_ID])==1:
                    winner = rule_options[field_ID][0]
                    winners[field_ID] = winner

                    # this winner is no longer an option for other field IDs
                    for field_ID in range(len(mine)):
                        try:
                            rule_options[field_ID].remove(winner)
                        except ValueError:
                            pass
                            
    # part 2
    prod = 1
    for x in [mine[x] for x,y in winners.items() if rule_names[y].startswith('departure')]:
        prod *= x
    print(prod)
    
if __name__=='__main__':
    main()
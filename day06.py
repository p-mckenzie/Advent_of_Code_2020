def main():
    with open('day06.txt', 'r') as f:
        txt = f.read().strip()
    f.close()

    pt_1 = 0
    pt_2 = 0

    for group in txt.split('\n\n'):
        qa_union = set()
        qa_intersection = set()
        
        for i, subgroup in enumerate(group.split()):
            subgroup = set(subgroup)
            
            # store union (all questions anyone answered yes to)
            qa_union = qa_union.union(subgroup)
            
            # store intersection (all questions everyone answered yes to)
            if i==0:
                # can't do intersection on empty set
                qa_intersection = subgroup
            else:
                qa_intersection = qa_intersection.intersection(subgroup)
                        
        pt_1 += len(qa_union)
        pt_2 += len(qa_intersection)
        
    print(pt_1)
    print(pt_2)
    
if __name__=='__main__':
    import numpy as np
    main()
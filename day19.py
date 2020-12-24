def check(rule_id, master_message, parsed_rules, depth=0, vocal=False):
    '''Checks if the input master_message matches the input rule_id. Handles recursion and OR conditions.
    Overall function returns True/False (whether the message fulfills the rule given by rule_id), 
    when called as a sub-function during recursion it will also return the intermediate message (after some handling).
    '''
    rule = parsed_rules[rule_id]
    message = master_message
    
    for option in rule.split(' | '):
        if vocal:
            print('\t'*depth, option, message, depth)
        # iterate through OR options, check that all conditions are made

        valid = True # all characters must be valid
        for char in option.split():
            if char.isnumeric():

                # different rule
                valid_section, new_message = check(char, message, parsed_rules, depth=depth+1, vocal=vocal)

                if new_message is None:
                    break

                valid = valid and valid_section
                message = new_message

            else:
                # actual rule
                valid = valid and message.startswith(char[1:-1])
                message = message[1:]
        
        try:
            # continue to next OR if this one failed
            if new_message is None:
                # reset message in case any alterations have been made
                message = master_message
                continue
        except:
            # in some cases, new_message variable is not yet declared
            pass
        
        if valid:
            # one option in the OR was valid
            if depth==0:
                # check no remaining characters exist at the end
                return message==''
            else: 
                return True, message
        else:
            # go to next option in OR
            continue
            
    # if it makes it this far, no OR option was valid
    if depth==0:
        return False
    else:
        return False, None
        
def validate_part_2(word, parsed_rules, width=8):
    # pattern - valid words will follow [42*x, 42*y, 31*y]
    # pattern - rule 42 and rule 31 always have 8 characters (width varies though, 5 in example)

    start = [check('42', word[width*i:width*(i+1)], parsed_rules) for i in range(len(word)//width)]
    end = [check('31', word[width*i:width*(i+1)], parsed_rules) for i in range(len(word)//width)]

    y = 0
    for item in end[::-1]:
        if item:
            y += 1
        else:
            break

    x = 0
    for item in reversed(start[:-2*y]):
        if item:
            x += 1
        else:
            break

    mask = start[:x]+start[x:x+y]+end[-y:] #42x 42y 31y
    return len(mask)==len(word)/width and min(mask) and x>0 and y>0
        
def main():
    with open('day19.txt', 'r') as f:
        txt = f.read().strip()
    f.close()

    rules, messages = txt.split('\n\n')
    messages = messages.split('\n')

    parsed_rules = {}
    for rule in rules.split('\n'):
        ID, content = rule.split(': ')
        parsed_rules[ID] = content
        
    # part 1
    print(sum([check('0', message, parsed_rules) for message in messages]))

    # part 2
    '''
    Turns out these are not needed to actually implement!
    parsed_rules['8'] = '42 | 42 8'
    parsed_rules['11'] = '42 31 | 42 11 31'
    '''
    print(sum([validate_part_2(message, parsed_rules) for message in messages]))

if __name__=='__main__':
    import numpy as np
    main()
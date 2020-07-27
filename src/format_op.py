def format_op(op):
    from ops import ops
    string = '```'
    for item in ops[op].keys():
        if type(ops[op][item]) is list:
            if item == 'armor/speed': 
                string += f'Armor: {ops[op][item][0]} | '
                string += f'Speed: {ops[op][item][1]}'
            else:
                string += f'{item.capitalize()}: '
                for subitem in ops[op][item]:
                    if subitem == ops[op][item][-1]:
                        string += f'{subitem}\n'
                    else:    
                        string += f'{subitem}, '
        else:
            string += f'{item.capitalize()} - {ops[op][item]}\n'
    string += '```'
    return string
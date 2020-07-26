def format_op(op):
    from ops import ops
    string = ''
    for item in ops[op].keys():
        if type(ops[op][item]) is list:
            string += f'{item.capitalize()}: '
            for subitem in ops[op][item]:
                if subitem == ops[op][item][-1]:
                    string += f'{subitem}\n'
                else:    
                    string += f'{subitem}, '
        else:
            string += f'{item.capitalize()} - {ops[op][item]}\n'
    return string
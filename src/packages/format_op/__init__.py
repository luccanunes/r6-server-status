def format_op(op):
    import discord
    from packages.ops import ops
    msg = discord.Embed(title=f'{op.upper()}', colour=discord.Color.from_rgb(244, 175, 44))
    for item in ops[op].keys():
        if type(ops[op][item]) is list:
            string = ''
            for subitem in ops[op][item]:
                if subitem == ops[op][item][-1]:
                    string += f'{subitem}'
                else:    
                    string += f'{subitem}, '
            msg.add_field(name=f'{item.capitalize()}', value=string)
        else:
            msg.add_field(name=f'{item.capitalize()}', value=f'{ops[op][item]}')
    
    return msg
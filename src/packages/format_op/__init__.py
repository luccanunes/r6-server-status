def format_op(op_data):
    import discord
    emb = discord.Embed(title=f'{op_data["name"].title()}', colour=discord.Color.from_rgb(244, 175, 44))
    for key, value in op_data.items():
        if key != 'name':
            if type(value) == list:
                emb.add_field(name=key.title(), value=', '.join(value))    
            else:
                emb.add_field(name=key.title(), value=value)
    return emb
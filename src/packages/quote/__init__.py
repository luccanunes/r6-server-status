def get_quote():
    '''
    generates a random very wise quote
    '''
    from random import randint
    quotes = ['tr7iu5', 'tr7j1o', 'tr7jo9', 'tr7kol', 'trep2v']
    domain = 'https://prnt.sc/'
    
    return domain + quotes[randint(0, len(quotes)-1)] 

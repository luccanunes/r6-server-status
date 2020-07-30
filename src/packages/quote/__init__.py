def get_quote():
    '''
    generates a random very wise quote
    '''
    from random import randint
    # quotes = ['tr7iu5', 'tr7j1o', 'tr7jo9', 'tr7kol', 'tr91t5']
    quotes = ['tr7iu5', 'tr7j1o', 'tr7jo9', 'tr7kol', 'tr97x9']
    domain = 'https://prnt.sc/'
    
    return domain + quotes[randint(0, len(quotes)-1)] 

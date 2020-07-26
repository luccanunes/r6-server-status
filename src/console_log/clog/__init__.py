import os


def log(c, t, decoration=False, ending='\n'):
    os.system("")
    length = len(t)*2 if len(t)*2 <= 209 else 209
    if decoration:
        print(f'[{str(c)}m' + '-'*length + '[0m', end=ending)
        print(f'[{str(c)}m{t:^{length}}[0m', end=ending)
        print(f'[{str(c)}m' + '-'*length + '[0m', end=ending)
    else:
        print(f'[{str(c)}m{t}[0m', end=ending)


def warning(t, decoration=False, ending='\n'):
    os.system("")
    length = len(t)*2 if len(t)*2 <= 209 else 209
    if decoration:
        print('[33m' + '-'*length + '[0m', end=ending)
        print(f'[33m{t:^{length}}[0m', end=ending)
        print('[33m' + '-'*length + '[0m', end=ending)
    else:
        print(f'[33m{t}[0m', end=ending)


def error(t, decoration=False, ending='\n'):
    os.system("")
    length = len(t)*2 if len(t)*2 <= 209 else 209
    if decoration:
        print('[91m' + '-'*length + '[0m', end=ending)
        print(f'[91m{t:^{length}}[0m', end=ending)
        print('[91m' + '-'*length + '[0m', end=ending)
    else:
        print(f'[91m{t}[0m', end=ending)


#log(32, 'sucessfully joined niver da chavosidade server', True)
# log(32, 'Sucessfuly joined "W2S" server', True)
# error('EXITING PROGRAM', True)

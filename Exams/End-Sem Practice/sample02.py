
def f(N):
    '''
    >>> f(20)
    Here are your banknotes:
    $20: 1
    >>> f(40)
    Here are your banknotes:
    $20: 2
    >>> f(42)
    Here are your banknotes:
    $2: 1
    $20: 2
    >>> f(43)
    Here are your banknotes:
    $1: 1
    $2: 1
    $20: 2
    >>> f(45)
    Here are your banknotes:
    $5: 1
    $20: 2
    >>> f(2537)
    Here are your banknotes:
    $2: 1
    $5: 1
    $10: 1
    $20: 1
    $100: 25
    '''
    banknote_values = [1, 2, 5, 10, 20, 50, 100]
    # Insert your code here
    banknotes = dict()
    
    for i in reversed(banknote_values):
        if N // i:
            banknotes[i] = N // i
        
        N %= i
        
    print('Here are your banknotes:')
    for key in sorted(banknotes):
        print(f'${key}: {banknotes[key]}')
                        

if __name__ == '__main__':
    import doctest
    doctest.testmod()

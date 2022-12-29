def isStringEmpty(a):
    if (type(a) != str):
        raise TypeError('a has to be string')
    if (not a):
        raise ValueError('a cannot be null')
    x=len(a.strip())
    if (x==0):
        return False
    return True

try:
    #a = 123
    a="hello"
    # a=' '
    print('isStringEmpty:', isStringEmpty(a))
except ValueError as e:
    print('ValueError raised:', e)
except TypeError as e:
    print('TypeError raised:', e)

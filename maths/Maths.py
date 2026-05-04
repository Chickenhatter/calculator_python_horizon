d = 'p'
a = 0
b = 0
c = 0
while d != '0':
    try:
        a = float(input('a: '))
        b = float(input('b: '))
        c = float(input('c: '))
        if ((b**2) - (4*a*b)) >= 0:
            print((-(b)-(((b**2)-(4*a*c))**0.5))/(2*a))
            print((-(b)+(((b**2)-(4*a*c))**0.5))/(2*a))
        else:
            print('No True')
    except:
        print("Didn't give a number")
    d = input('cont ! 0')

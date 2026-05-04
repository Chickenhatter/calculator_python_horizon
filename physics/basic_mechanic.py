choice = input('m/f')
if choice == 'm':
    print('(dvtamFAPWp)Please give all letters for factors you know')
    commands = input('All of them: ')
    d = False
    v = False
    t = False
    a = False
    m = False
    F = False
    A = False
    P = False
    W = False
    p = False #Power
    for i in commands:
        if i == 'd':
            d = float(input('Distance(m): '))
        if i == 'v':
            v = float(input('Velocity(ms-1): '))
        if i == 't':
            t = float(input('Time(s): '))
        if i == 'a':
            a = float(input('Acceleration(ms-2): '))
        if i == 'm':
            m = float(input('Mass(kg): '))
        if i == 'F':
            F = float(input('Force(N): '))
        if i == 'A':
            A = float(input('Area(m -2): '))
        if i == 'P':
            P = float(input('Pressure(N m -2): '))
        if i == 'W':
            W = float(input('Work(J): '))
        if i == 'p':
            p = float(input('Power(Watts): '))
    x = 0
    while x < 6:
        if (d != False) and (v != False) and (t == False):
            t = d/v
        if (d != False) and (t != False) and (v == False):
            v = d/t
        if (t != False) and (v != False) and (d == False):
            d = v*t
        
        if (v != False) and (a != False) and (t == False):
            t = v/a
        if (v != False) and (t != False) and (a == False):
            a = v/t
        if (t != False) and (a != False) and (v == False):
            v = a*t
        
        if (F != False) and (a != False) and (m == False):
            m = F/a
        if (F != False) and (m != False) and (a == False):
            a = F/m
        if (a != False) and (m != False) and (F == False):
            F = a*m
        
        if (F != False) and (P != False) and (A == False):
            A = F/P
        if (F != False) and (A != False) and (P == False):
            P = F/A
        if (P != False) and (A != False) and (F == False):
            F = P*A

        if (F != False) and (W != False) and (d == False):
            d = W/F
        if (W != False) and (d != False) and (F == False):
            F = W/d
        if (F != False) and (d != False) and (W == False):
            W = F*d

        if (t != False) and (W != False) and (p == False):
            p = W/t
        if (W != False) and (p != False) and (t == False):
            t = W/p
        if (p != False) and (t != False) and (W == False):
            W = p*t
        x += 1
    print('This all results in')
    print(d,'m')
    print(v,'m s -1')
    print(t,'s')
    print(a,'m s -2')
    print(m,'kg')
    print(F,'N')
    print(A,'m -2')
    print(P,'P(N m -2)')
    print(W, 'J')
    print(p,'Watts')
elif choice == 'f':
    print('(pkmghv)Please give all letters for factors you know')
    commands = input('All of them: ')
    p = False
    k = False
    m = False
    g = False
    h = False
    v = False
    for i in commands:
        if i == 'p':
            p = float(input('Gravitational Potential Enegry(J): '))
        if i == 'k':
            k = float(input('Kinetic Enegry(J): '))
        if i == 'm':
            m = float(input('Mass(Kg): '))
        if i == 'g':
            g = float(input('Gravity(N Kg): '))
        if i == 'h':
            h = float(input('Height(m): '))
        if i == 'v':
            v = float(input('Velocity(ms-1): '))
    l = 2
    while l != 0:
        if (p != False) and (m != False) and (g != False) and (h == False):
            h = (p)/(m*g)
        if (p != False) and (h != False) and (g != False) and (p == False):
            m = (p)/(h*g)
        if (p != False) and (m != False) and (h != False) and (g == False):
            g = (p)/(m*h)
        if (h != False) and (m != False) and (g != False) and (p == False):
            p = (h*m*g)

        if (k != False) and (m != False) and (k == False):
            v = ((2*k)/m) ** (0.5)
        if (k != False) and (v != False) and (m == False):
            m = ((2*(k))/(v*v))
        if (v != False) and (m != False) and (k == False):
            k = (0.5)*(v*v)*(m)
        l -= 1
        print('a')
    print('This all results in')
    print(p,'potential gravity(J)')
    print(k,'kinetic J')
    print(m,'Mass(Kg)')
    print(g,'N Kg')
    print(h,'m')
    print(v,'m s-1')
    
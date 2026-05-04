elements_dictionary = {
    "h": 1.0, "hE": 4.0,
    "lI": 6.9, "bE": 9.0, "b": 10.8, "c": 12.0, "n": 14.0, "o": 16.0, "f": 19.0, "nE": 20.2,
    "nA": 23.0, "mG": 24.3, "aL": 27.0, "sI": 28.1, "p": 31.0, "s": 32.1, "cL": 35.5, "aR": 40.0,
    "k": 39.1, "cA": 40.1, "sC": 45.0, "tI": 47.9, "v": 50.9, "cR": 52.0, "mN": 54.9, "fE": 55.9,
    "cO": 58.9, "nI": 58.7, "cU": 63.6, "zN": 65.4, "gA": 69.7, "gE": 72.6, "aS": 74.9, "sE": 79.0,
    "bR": 79.9, "kR": 83.8,
    "rB": 85.5, "sR": 87.6, "y": 88.9, "zR": 91.2, "nB": 92.9, "mO": 95.9, "tC": 98.9, "rU": 101,
    "rH": 103, "pD": 106, "aG": 108, "cD": 112, "iN": 115, "sN": 119, "sB": 122,
    "tE": 128, "i": 127, "xE": 131,
    "cS": 133, "bA": 137, "lA": 139, "cE": 140, "pR": 141, "nD": 144, "pM": 147,
    "sM": 150, "eU": 152, "gD": 157, "tB": 159, "dY": 163, "hO": 165, "eR": 167,
    "tM": 169, "yB": 173, "lU": 175.0,
    "hF": 179, "tA": 181, "w": 184, "rE": 186, "oS": 190, "iR": 192, "pT": 195,
    "aU": 197, "hG": 201, "tL": 204, "pB": 207, "bI": 209, "pO": 210, "aT": 210,
    "rN": 222,
    "fR": 223, "rA": 226, "aC": 227.0, "tH": 232.0, "pA": 231.0, "u": 238.0, "nP": 237.0,
    "pU": 239, "aM": 241, "cM": 244, "bK": 249, "cF": 251.0, "eS": 252.0, "fM": 257.0,
    "mD": 258.0, "nO": 259.0, "lR": 262.0,
    "rF": 261.0, "dB": 262.0, "sG": 263.0, "bH": 264.0, "hS": 265.0, "mT": 268.0, "dS": 271.0,
    "rG": 272.0, "cN": 277.0,
    "nH": 286.0, "fL": 289.0, "mC": 290.0, "lV": 293.0, "tS": 294.0,
    "oG": 294.0
}

element_symbols = [
    "hE","lI","bE","nE","nA","mG","aL","sI","cL","aR","cA","sC","tI","cR","mN","fE","cO","nI","cU","zN",
    "gA","gE","aS","sE","bR","kR","rB","sR","zR","nB","mO","tC","rU","rH","pD","aG","cD","iN","sN","sB",
    "tE","xE","cS","bA","lA","cE","pR","nD","pM","sM","eU","gD","tB","dY","hO","eR","tM","yB","lU",
    "hF","tA","rE","oS","iR","pT","aU","hG","tL","pB","bI","pO","aT","rN","fR","rA","aC","tH","pA","nP",
    "pU","aM","cM","bK","cF","eS","fM","mD","nO","lR","rF","dB","sG","bH","hS","mT","dS","rG","cN","nH",
    "fL","mC","lV","tS","oG",
    "h","b","c","n","o","f","p","s","k","v","y","i","w","u"
]
print('Do you want to find molar mass of element(M) or do you want to find all info from CVmMn(K) or do you want to find all info from Mecanics(P)')
choice = input('m/k: ')
if 1 == 1:
    if choice == 'm':
        elements = {}
        the_element = input('Element?')

        # Will be for Crystilsed water
        call = False
        start = False
        thing = 0
        lend = False
        for different in the_element:
            if different == ".":
                start = thing
                call = True
            thing += 1
        if call == True:
            lend = (the_element[(start):(len(the_element))])
            print(the_element)
            the_element = the_element.replace(lend,"")
            print(the_element)
            place = 0
            time = int(lend[1])
            lend = lend[2:]
            while lend != '':
                element = element_symbols[place]
                try:
                    a = element[1]
                    a = 2
                    kilt = 0
                    filt = 1
                except:
                    a = 1
                    kilt = 0
                    filt = 0
                v = 0
                while v < len(lend) +kilt:
                    if (lend[v:v+a]) == element:
                        lend = lend[:(v)] + lend[(v+kilt):]
                        try:
                            if (lend[(v+1+filt)]).isdigit():
                                if element in elements:
                                    elements[element] += int((lend[(v+1+filt)]))*time
                                else:
                                    elements[element] = int((lend[(v+1+filt)]))*time
                                lend = lend[:(v+1-filt)] + lend[(v+2+filt):]
                            else:
                                if element in elements:
                                    elements[element] += time
                                else:
                                    elements[element] = time
                        except:
                            if element in elements:
                                elements[element] += time
                            else:
                                elements[element] = time
                    v += 1
                place += 1
                lend = lend.replace(element,'')


        # Remove the bracket thingy
        place = 0
        v = 0
        start = 0
        thing = 0
        end = []
        for different in the_element:
            if different == '(':
                start = thing
            if different == ')':
                end.append(the_element[(start):(thing+2)])
            thing += 1
        for lolak in end:
            the_element = the_element.replace(lolak,"")
        for lolack in end:
            place = 0
            time = int(lolak[-1])
            lolack = lolack[:-2]
            lolack = lolack[1:]
            while lolack != '':
                element = element_symbols[place]
                try:
                    a = element[1]
                    a = 2
                    kilt = 0
                    filt = 1
                except:
                    a = 1
                    kilt = 0
                    filt = 0
                v = 0
                while v < len(lolack) +kilt:
                    if (lolack[v:v+a]) == element:
                        lolack = lolack[:(v)] + lolack[(v+kilt):]
                        try:
                            if (lolack[(v+1+filt)]).isdigit():
                                if element in elements:
                                    elements[element] += int((lolack[(v+1+filt)]))*time
                                else:
                                    elements[element] = int((lolack[(v+1+filt)]))*time
                                lolack = lolack[:(v+1-filt)] + lolack[(v+2+filt):]
                            else:
                                if element in elements:
                                    elements[element] += time
                                else:
                                    elements[element] = time
                        except:
                            if element in elements:
                                elements[element] += time
                            else:
                                elements[element] = time
                    v += 1
                place += 1
                lolack = lolack.replace(element,'')





        # Remove everything else
        place = 0
        while the_element != '':
                element = element_symbols[place]
                try:
                    a = element[1]
                    a = 2
                    kilt = 0
                    filt = 1
                except:
                    a = 1
                    kilt = 0
                    filt = 0
                v = 0
                while v < len(the_element) +kilt:
                    if (the_element[v:v+a]) == element:
                        the_element = the_element[:(v)] + the_element[(v+kilt):]
                        try:
                            if (the_element[(v+1+filt)]).isdigit():
                                if element in elements:
                                    elements[element] += int((the_element[(v+1+filt)]))
                                else:
                                    elements[element] = int((the_element[(v+1+filt)]))
                                the_element = the_element[:(v+1-filt)] + the_element[(v+2+filt):]
                            else:
                                if element in elements:
                                    elements[element] += 1
                                else:
                                    elements[element] = 1
                        except:
                            if element in elements:
                                elements[element] += 1
                            else:
                                elements[element] = 1
                    v += 1
                place += 1
                the_element = the_element.replace(element,'')
        print('This is just a list of all elements and how common they appear if you need it')
        print(elements)
        print('The Molar Mass g mol-1 is this much')
        final_mass = 0
        for lalas in elements:
            if lalas in elements_dictionary:
                v1 = elements_dictionary[lalas] 
                v2 = elements[lalas] 
                final_mass += (v1*v2)
        print(final_mass)
    elif choice == 'k':
        print('(MmnCV)Please give all letters for chem you know')
        commands = input('All of them: ')
        M = False
        m = False
        n = False
        C = False
        V = False
        for i in commands:
            if i == 'M':
                M = True
            if i == 'm':
                m = True
            if i == 'n':
                n = True
            if i == 'C':
                C = True
            if i == 'V':
                V = True
        if M == True:
            M = float(input('Molar Mass(moLg-1): '))
        if m == True:
            m = float(input('Mass(g): '))
        if n == True:
            n = float(input('Mol: '))
        if C == True:
            C = float(input('Concentration(molL-1): '))
        if V == True:
            V = float(input('Volume(L): '))
        x = 0
        while x < 6:
            if (M != False) and (m != False):
                n = m/M
            if (n != False) and (m != False):
                M = m/n
            if (M != False) and (n != False):
                m = n*M
            if (C != False) and (n != False):
                V = n/C
            if (V != False) and (n != False):
                C = n/V
            if (C != False) and (V != False):
                n = V*C
            x += 1
        print(M,'g mol -1')
        print(m, 'g')
        print(n,'mol')
        print(C,'mol L -1')
        print(V,'L')
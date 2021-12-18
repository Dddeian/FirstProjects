a = int(input('month = '))
b = int(input('day = '))
c = str
d = str

if a > 12:
    a = a%12
    if a == 1:
        if b < 32:
            c = str('january')
            d = str('winter')
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 31 and b < 60:
            c = str('february')
            d = str('winter')
            b = b - 31
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 59 and b < 91:
            c = str('march')
            if b >= 80:
                d = str('spring')
                b = b - 59
                print(f'It is {b} of {c},the season is {d}.')
            else:
                d = str('winter') 
                b = b - 59
                print(f'It is {b} of {c},the season is {d}.')   
        elif b > 90 and b < 121:
            c = str('april')
            d = str('spring')
            b = b - 90
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 120 and b < 152:
            c = str('may')
            d = str('spring')
            b = b - 120
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 151 and b < 182:
            c = str('june')
            if b >= 172:
                d = str('summer')
                b = b - 151
                print(f'It is {b} of {c},the season is {d}.')
            else:
                d = str('spring')
                b = b - 151
                print(f'It is {b} of {c},the season is {d}.')
        elif b > 181 and b < 213:
            c = str('july')
            d = str('summer')
            b = b - 181
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 212 and b < 243:
            c = str('august')
            d = str('summer')
            b = b - 212
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 242 and b < 274:
            c = str('september')
            if b >= 263:
                d = str('autumn')
                b = b - 242
                print(f'It is {b} of {c},the season is {d}.')
            else:
                d = str('summer')
                b = b - 242
                print(f'It is {b} of {c},the season is {d}.')
        elif b > 273 and b < 305:
            c = str('october')
            d = str('autumn')
            b = b - 273
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 304 and b < 335:
            c = str('november')
            d = str('autumn')
            b = b - 304
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 334 and b < 366:
            c = str('december')
            if b >= 355:
                d = str('winter')
                b = b - 334
                print(f'It is {b} of {c},the season is {d}.')
            else:
                d = str('autumn')
                b = b - 334
                print(f'It is {b} of {c},the season is {d}.')
        elif b > 365:
            b = b%365
            if b < 32:
                c = str('january')
                d = str('winter')
                print(f'It is {b} of {c},the season is {d}.')
            elif b > 31 and b < 60:
                c = str('february')
                d = str('winter')
                b = b - 31
                print(f'It is {b} of {c},the season is {d}.')
            elif b > 59 and b < 91:
                c = str('march')
                if b >= 80:
                    d = str('spring')
                    b = b - 59
                    print(f'It is {b} of {c},the season is {d}.')
                else:
                    d = str('winter')
                    b = b - 59
                    print(f'It is {b} of {c},the season is {d}.')    
            elif b > 90 and b < 121:
                c = str('april')
                d = str('spring')
                b = b - 90
                print(f'It is {b} of {c},the season is {d}.')
            elif b > 120 and b < 152:
                c = str('may')
                d = str('spring')
                b = b - 120
                print(f'It is {b} of {c},the season is {d}.')
            elif b > 151 and b < 182:
                c = str('june')
                if b >= 172:
                    d = str('summer')
                    b = b - 151
                    print(f'It is {b} of {c},the season is {d}.')
                else:
                    d = str('spring')
                    b = b - 151
                    print(f'It is {b} of {c},the season is {d}.')
            elif b > 181 and b < 213:
                c = str('july')
                d = str('summer')
                b = b - 181
                print(f'It is {b} of {c},the season is {d}.')
            elif b > 212 and b < 243:
                c = str('august')
                d = str('summer')
                b = b - 212
                print(f'It is {b} of {c},the season is {d}.')
            elif b > 242 and b < 274:
                c = str('september')
                if b >= 263:
                    d = str('autumn')
                    b = b - 242
                    print(f'It is {b} of {c},the season is {d}.')
                else:
                    d = str('summer')
                    b = b - 242
                    print(f'It is {b} of {c},the season is {d}.')
            elif b > 273 and b < 305:
                c = str('october')
                d = str('autumn')
                b = b - 273
                print(f'It is {b} of {c},the season is {d}.')
            elif b > 304 and b < 335:
                c = str('november')
                d = str('autumn')
                b = b - 304
                print(f'It is {b} of {c},the season is {d}.')
            elif b > 334 and b < 366:
                c = str('december')
                if b >= 355:
                    d = str('winter')
                    b = b - 334
                    print(f'It is {b} of {c},the season is {d}.')
                else:
                    d = str('autumn')
                    b = b - 334
                    print(f'It is {b} of {c},the season is {d}.')                                
    elif a == 2:
        if b < 29:
            c = str('february')
            d = str('winter')
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 28 and b < 60:
            c = str('march')
            if b >=49:
                d = str('spring')
                b = b - 28
                print(f'It is {b} of {c},the season is {d}.')
            else:
                d = str('winter') 
                b = b - 28
                print(f'It is {b} of {c},the season is {d}.')   
        elif b > 59 and b < 90:
            c = str('april')
            b = b - 59 
            print(f'It is {b} of {c},the season is {d}.') 
        elif b > 89 and b < 121:
            c = str('may')
            d = str('spring')
            b = b - 89
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 120 and b < 151:
            c = str('june')
            if b >=141:
                d = str('summer')
                b = b - 120
                print(f'It is {b} of {c},the season is {d}.')
            else:
                d = str('spring')
                b = b - 120
                print(f'It is {b} of {c},the season is {d}.')
        elif b > 150 and b < 182:
            c = str('july')
            b = b - 150
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 181 and b < 213:
            c = str('july')
            d = str('summer')
            b = b - 181
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 212 and b < 243:
            c = str('august')
            d = str('summer')
            b = b - 212
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 242 and b < 274:
            c = str('september')
            if b >= 263:
                d = str('autumn')
                b = b - 242
                print(f'It is {b} of {c},the season is {d}.')
            else:
                d = str('summer')
                b = b - 242
                print(f'It is {b} of {c},the season is {d}.')
        elif b > 273 and b < 305:
            c = str('october')
            d = str('autumn')
            b = b - 273
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 304 and b < 335:
            c = str('november')
            d = str('autumn')
            b = b - 304
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 334 and b < 366:
            c = str('december')
            if b >= 355:
                d = str('winter')
                b = b - 334
                print(f'It is {b} of {c},the season is {d}.')
            else:
                d = str('autumn')
                b = b - 334
                print(f'It is {b} of {c},the season is {d}.')
        elif b > 365:
            b = b%365
            if b < 29:
                c = str('february')
                d = str('winter')
                print(f'It is {b} of {c},the season is {d}.')
            elif b > 28 and b < 60:
                c = str('march')
                if b >=49:
                    d = str('spring')
                    b = b - 28
                    print(f'It is {b} of {c},the season is {d}.')
                else:
                    d = str('winter') 
                    b = b - 28
                    print(f'It is {b} of {c},the season is {d}.')   
            elif b > 59 and b < 90:
                c = str('april')
                b = b - 59 
                print(f'It is {b} of {c},the season is {d}.') 
            elif b > 89 and b < 121:
                c = str('may')
                d = str('spring')
                b = b - 89
                print(f'It is {b} of {c},the season is {d}.')
            elif b > 120 and b < 151:
                c = str('june')
                if b >=141:
                    d = str('summer')
                    b = b - 120
                    print(f'It is {b} of {c},the season is {d}.')
                else:
                    d = str('spring')
                    b = b - 120
                    print(f'It is {b} of {c},the season is {d}.')
            elif b > 150 and b < 182:
                c = str('july')
                b = b - 150
                print(f'It is {b} of {c},the season is {d}.')
            elif b > 181 and b < 213:
                c = str('july')
                d = str('summer')
                b = b - 181
                print(f'It is {b} of {c},the season is {d}.')
            elif b > 212 and b < 243:
                c = str('august')
                d = str('summer')
                b = b - 212
                print(f'It is {b} of {c},the season is {d}.')
            elif b > 242 and b < 274:
                c = str('september')
                if b >= 263:
                    d = str('autumn')
                    b = b - 242
                    print(f'It is {b} of {c},the season is {d}.')
                else:
                    d = str('summer')
                    b = b - 242
                    print(f'It is {b} of {c},the season is {d}.')
            elif b > 273 and b < 305:
                c = str('october')
                d = str('autumn')
                b = b - 273
                print(f'It is {b} of {c},the season is {d}.')
            elif b > 304 and b < 335:
                c = str('november')
                d = str('autumn')
                b = b - 304
                print(f'It is {b} of {c},the season is {d}.')
            elif b > 334 and b < 366:
                c = str('december')
                if b >= 355:
                    d = str('winter')
                    b = b - 334
                    print(f'It is {b} of {c},the season is {d}.')
                else:
                    d = str('autumn')
                    b = b - 334
                    print(f'It is {b} of {c},the season is {d}.')
    elif a == 3:
        if b < 32:
            c = str('march')
            if b >=21:
                d = str('spring')
                b = b 
                print(f'It is {b} of {c},the season is {d}.')
            else:
                d = str('winter') 
                b = b 
                print(f'It is {b} of {c},the season is {d}.')   
        elif b > 31 and b < 62:
            c = str('april')
            b = b - 31
            print(f'It is {b} of {c},the season is {d}.') 
        elif b > 61 and b < 93:
            c = str('may')
            d = str('spring')
            b = b - 61
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 82 and b < 113:
            c = str('june')
            if b >=103:
                d = str('summer')
                b = b - 82
                print(f'It is {b} of {c},the season is {d}.')
            else:
                d = str('spring')
                b = b - 82
                print(f'It is {b} of {c},the season is {d}.')
        elif b > 150 and b < 182:
            c = str('july')
            b = b - 150
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 181 and b < 213:
            c = str('july')
            d = str('summer')
            b = b - 181
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 212 and b < 243:
            c = str('august')
            d = str('summer')
            b = b - 212
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 242 and b < 274:
            c = str('september')
            if b >= 263:
                d = str('autumn')
                b = b - 242
                print(f'It is {b} of {c},the season is {d}.')
            else:
                d = str('summer')
                b = b - 242
                print(f'It is {b} of {c},the season is {d}.')
        elif b > 273 and b < 305:
            c = str('october')
            d = str('autumn')
            b = b - 273
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 304 and b < 335:
            c = str('november')
            d = str('autumn')
            b = b - 304
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 334 and b < 366:
            c = str('december')
            if b >= 355:
                d = str('winter')
                b = b - 334
                print(f'It is {b} of {c},the season is {d}.')
            else:
                d = str('autumn')
                b = b - 334
                print(f'It is {b} of {c},the season is {d}.')
        elif b < 32:
            c = str('january')
            d = str('winter')
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 31 and b < 60:
            c = str('february')
            d = str('winter')
            b = b - 31
            print(f'It is {b} of {c},the season is {d}.')
        elif b > 365:
            b = b%365






    elif a == 4:
        c = str('april')
    elif a == 5:
       c = str('may')
    elif a == 6:
        c = str('june')
    elif a == 7:
        c = str('july')
    elif a == 8:
        c = str('august')
    elif a == 9:
       c = str('september')
    elif a == 10:
        c = str('october')
    elif a == 11:
        c = str('november')
    elif a == 12:
        c = str('december')

if a == 1:
    if b < 32:
        c = str('january')
        d = str('winter')
    elif b > 31 and b < 60:
        c = str('february')
        d = str('winter')
    elif b > 59 and b < 91:
        c = str('march')
        if b >= 70:
            d = str('spring')
        else:
            d = str('winter')    
    elif b > 90 and b < 121:
        c = str('april')
        d = str('spring')
    elif b > 120 and b < 152:
        c = str('may')
        d = str('spring')
    elif b > 151 and b < 182:
        c = str('june')
        if b >= 172:
            d = str('summer')
        else:
            d = str('spring')
    elif b > 181 and b < 213:
        c = str('july')
        d = str('summer')
    elif b > 212 and b < 243:
        c = str('august')
        d = str('summer')
    elif b > 242 and b < 274:
        c = str('september')
        if b >= 263:
            d = str('autumn')
        else:
            d = str('summer')
    elif b > 273 and b < 305:
        c = str('october')
        d = str('autumn')
    elif b > 304 and b < 335:
        c = str('november')
        d = str('autumn')
    elif b > 334 and b < 366:
        c = str('december')
        if b >= 355: 
            d = str('winter')
        else:
            d = str('autumn')

elif a == 2:
    c = str('february')
elif a == 3:
    c = str('march')
elif a == 4:
    c = str('april')
elif a == 5:
    c = str('may')
elif a == 6:
    c = str('june')
elif a == 7:
    c = str('july')
elif a == 8:
    c = str('august')
elif a == 9:
    c = str('september')
elif a == 10:
    c = str('october')
elif a == 11:
    c = str('november')
elif a == 12:
    c = str('december')

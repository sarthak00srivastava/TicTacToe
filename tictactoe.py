lst = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
xolst = ['X', 'O']
xoro = -1


def draw():
    print('-'*9)
    for i in range(3):
        print('| ' + lst[i][0] + ' ' + lst[i][1] + ' ' + lst[i][2] + ' |')
    print('-'*9)


def entry():
    try:
        r, c = map(int, input('Enter the coordinates:').split())
        if lst[r - 1][c - 1] == ' ':
            global xoro
            xoro = (xoro + 1) % 2
            lst[r - 1][c - 1] = xolst[xoro]
            draw()
            result()
        else:
            print('This cell is occupied! Choose another one!')
            entry()
    except ValueError:
        print('You should enter numbers!')
        entry()
    except IndexError:
        print('Coordinates should be from 1 to 3!')
        entry()


def result():
    Xwin = 0
    Owin = 0
    Xc = 0
    Oc = 0
    str_1 = ''.join(lst[0])
    str_2 = ''.join(lst[1])
    str_3 = ''.join(lst[2])
    str_ = str_1 + str_2 + str_3
    lst1 = lst[0]
    lst2 = lst[1]
    lst3 = lst[2]
    for _ in range(3):
        if str_[_ * 3: (_ + 1) * 3] == 'XXX':
            Xwin = Xwin + 1
        elif str_[_ * 3: (_ + 1) * 3] == 'OOO':
            Owin = Owin + 1
        if str_[0 + _] + str_[3 + _] + str_[6 + _] == 'XXX':
            Xwin = Xwin + 1
        elif str_[0 + _] + str_[3 + _] + str_[6 + _] == 'OOO':
            Owin = Owin + 1
    if str_[0] + str_[4] + str_[8] == 'XXX':
        Xwin = Xwin + 1
    elif str_[0] + str_[4] + str_[8] == 'OOO':
        Owin = Owin + 1
    if str_[2] + str_[4] + str_[6] == 'XXX':
        Xwin = Xwin + 1
    elif str_[2] + str_[4] + str_[6] == 'OOO':
        Owin = Owin + 1
    for i in range(3):
        if lst1[i] == 'X':
            Xc = Xc + 1
        elif lst1[i] == 'O':
            Oc = Oc + 1
        if lst2[i] == 'X':
            Xc = Xc + 1
        elif lst2[i] == 'O':
            Oc = Oc + 1
        if lst3[i] == 'X':
            Xc = Xc + 1
        elif lst3[i] == 'O':
            Oc = Oc + 1
    if Xwin == 1 and Owin == 0:
        print('X wins')
        exit()
    elif Owin == 1 and Xwin == 0:
        print('O wins')
        exit()
    elif Xwin == 0 and Owin == 0 and (Xc + Oc) == 9:
        print('Draw')
        exit()
    elif Xwin == 0 and Owin == 0 and (Xc + Oc) < 9:
        entry()

draw()
result()

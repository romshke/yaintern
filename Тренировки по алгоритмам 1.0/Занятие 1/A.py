troom, tcond = map(int, input().split())
mode = input()

match mode:
    case 'freeze': print(tcond if troom > tcond else troom)
    case 'heat': print(tcond if troom < tcond else troom)
    case 'auto': print(tcond)
    case 'fan': print(troom)
    
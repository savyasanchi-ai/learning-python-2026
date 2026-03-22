weight = int(input('weight: '))
unit = input('(L)bs or (K)g')
if unit.upper() == 'L':
    converted = weight * 0.4
    print(f'you are {converted}Kg')
else:
    converted = weight / 0.4
    print(f' you are {converted}Lbs')
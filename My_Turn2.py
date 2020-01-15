numList =  [0, 3, 4, 0, 22, 1]
noZero = [zero for zero in numList if zero > 0]
print(f'No zero in list: {noZero}')

classList = ['ITEC 2560', 'BTEC 1010', 'ITEC 2905']
itec = [itec for itec in classList if 'ITEC' in itec]
print(f'ITEC classes: {itec}')
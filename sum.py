sum=0
while True :
    n=input('Write number: ')
    if n != '':
        sum +=int(n)
    else :
        print('Total is: ',sum)
        input('press any key to exit...')
        exit()

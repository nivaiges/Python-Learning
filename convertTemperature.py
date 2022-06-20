print('Type C to convert Celsius To Fahrenheit or Type F to convert Fahrenheit to Celsius: ')
x = input()
if x.lower() in ['C','c']:
    y = input()
    print('How many degrees?' + y)
    print(y + 'degrees Celsius is ' + ((y*(9/5))+32) + ' in Fahrenheit')
elif x.lower() in ['F','f']:
    y = input()
    print('How many degrees?' + y)
    (y + 'degrees Fahrenheit is ' + ((y-32)*(5/9)))

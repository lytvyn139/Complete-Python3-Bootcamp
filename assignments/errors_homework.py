#TASK1
try:
    for i in ['a','b','c']:
        print(i**2)

except TypeError:
    print('Type error')

#TASK2
try:
    x = 5
    y = 0
    z = x/y

except ZeroDivisionError:
    print('Division by zero error')
finally:
    print('All done !')

#TASK3
def ask():
    while True:
        try:
            n = int(input('Input an iteger: '))
        except:
            print('an Error occured! please try again \n')
            continue
        else:
            break
    print(f'Thank you, your squared number is: {n**2}')
ask()
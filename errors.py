# try
# except
# finally 
# def add(n1,n2):
#     print (n1+n2)
# n1 = 10
# n2 = input("please provide a number")
# add(n1,n2)

#example1
try:
    result = 10 + 10
except:
    print('hey it looks like you arent adding correctly!')
else:
    print('Add went well')    
    print(result)

#example2
try:
    f = open('testfile','r') #w
    f.write('write a test line')

except TypeError:
    print('There was a type error!')
except OSError:
    print('you have and OS erorr!')
except:
    print('all other execptions!')
finally:
    print('I always run')

#example3
def ask_for_int():
    while True:
        try:
            result = int(input('please privide number: '))
        except:
            print('whoops ! thats not a number')
            continue
        else:
            print(f'Yes! thanks for the number {result}')
            break
        finally:
            print('Im gonna ask you again')
ask_for_int()
# x = int(input())
# y = int(input())
# ans = 0
# try:
#     ans = x / y
#     print(ans)
# except ZeroDivisionError:
#     print("Inside Zero Division Error")
# except:
#     print("denominater can not be zero")
# finally:
#     print("This is finally, this works after try and except")


class InvalidTransactionException(Exception):
    pass

def withdraw(x):
    amount =100
    if x > amount :
        raise InvalidTransactionException("Insufficient amount")
    amount -= x
try:
    withdraw(120)
except InvalidTransactionException as e:
    print(e)
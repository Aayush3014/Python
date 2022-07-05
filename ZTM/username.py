username = input("Enter the username: ")
password = input("Enter the password: ")
length=len(password)
secret= length * '*'
print(f'{username} , your password is {secret} and it is  {length} letters long ')

import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
           'q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+']
print("Welcome to password generator!!!!")
n_letters=int(input("how many letters you want in your password\n "))
n_numbers=int(input("how many numbers you want in your password\n"))
n_symbols=int(input("how many symbols you want in your password\n"))
password = " "
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password=password+char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password=password+char
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password=password+char
print(password)
    

    

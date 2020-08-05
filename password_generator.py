import random 
import string
import pyfiglet


def get_random_password():
    
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    return password
    

def get_random_withoutCHAR():
    random_source = string.ascii_letters + string.digits
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    return password

def digit_count(password):
    for i in range(8):
        password += random.choice(random_source)
    password_list = list(password)
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    print (password)

print("*"*100)
a = pyfiglet.figlet_format("soona*panna")
print(a)
print("*"*100)
try:
    print("1.password with special char")
    print ("2.password without special char")
    option = int(input(">>>"))
    count = int(input("how many pass do you want: "))
except ValueError:
    print("")

try:
    if option == 1:
        for c in range(count):
            pass_word = get_random_password()
            random_source = string.ascii_letters + string.digits + string.punctuation
            digit_count(pass_word)
    elif option == 2:
        for c in range(count):
            pass_word = get_random_withoutCHAR()
            random_source = string.ascii_letters + string.digits
            digit_count(pass_word)
    else:
       print("worng selection")
except NameError:
    print("please enter values in number")











                




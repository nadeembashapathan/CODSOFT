#importing random module to get random choice from given choices
import random as r

#importing string module to get the letters, digits and other special characters
import string as s

#initilizing length variable to know the length of the password from User
length=int(input("Enter the length of the password: ")) 

#storing all the letters, digits and special symbols in char named variable
char=s.ascii_letters+s.digits+s.punctuation     

#storing the password in password named variable which is combination of all characters and symbols with condition of provided length of password
password=''.join([r.choice(char)for i in range(length)])          


print(password)

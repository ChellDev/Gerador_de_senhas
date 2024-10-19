""" *Funções
    *Estrutura de lista
    *Uso do "for"
"""
import random
import string

def password_generator(len_pass = 8):
    ascii_options = string.ascii_letters
    number_opotions = string.digits
    punto_options = string.punctuation
    options = ascii_options + number_opotions + punto_options

    password_user = ""

    for i in range(0, len_pass):
        #[ 0,1,2,3,4,5,6,7]
        digit = random.choice(options)
        password_user = password_user + digit
    
    return password_user

choice_user = input("Quantos digitos na senha?")

if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Entrada inválida!")
    quit()

response = password_generator(len_pass = choice_user)
print(f"Senha gerada:\n{response}")
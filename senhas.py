import random
import string

minusculas = string.ascii_lowercase
maiusculas = string.ascii_uppercase
numeros = string.digits
especiais = string.punctuation

todos = minusculas + maiusculas + numeros + especiais

def gerar_senha(y):
    return ''.join(random.choice(todos) for x in range(y))

caracteres = int(input('Quantos caracteres você deseja na sua senha? '))
if caracteres <= 1:
    print('\nNão é possível gerar uma senha com 1 caractere')
else:
    senha = gerar_senha(caracteres)
    print(senha)

__author__ = 'Silvio Luis'

# lendo um número binário
# converter de binário para decimal basta usar a base 2 na conversão para inteiro
dec = int(input("Digite um número Binario: "), 2)
# imprimido o número em decimal
print(dec)

# ufunção que comverte decimal para binario
def binary(numero):
   if numero > 1:
       binary(numero//2)
   print(numero % 2,end = '')

# lendo um número decimal
decimal = int(input("Digite um número Decimal: "))
binary(decimal)


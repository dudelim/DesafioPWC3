# Caso Complexo

def str_endereco(endereco):
  parte_endereco = endereco.split()  # Divide o endereço em partes separadas
  nome_rua = ''
  numero_rua = ''

# Se a primeira parte for um número:
if parte_endereeco[0].isdigit():
  numero_rua = partes[0]  # Primeira parte = número
  nome_rua = ' '.join(partes[1:]) 
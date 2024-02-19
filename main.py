# Caso Complexo
def str_endereco(endereco):
    parte_endereco = endereco.split()  # Divide o endereço 
    nome_rua = ''
    numero_rua = ''

    # Verifica se há vírgula
    if "," in parte_endereco[0]:
        numero_rua, *nome_rua = parte_endereco[0].split(",")  # Divide núm/rua
        nome_rua = ' '.join(nome_rua + parte_endereco[1:])  
   
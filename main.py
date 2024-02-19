# Caso Complexo
def str_endereco(endereco):
    parte_endereco = endereco.split()  # Divide o endereço 
    nome_rua = ''
    numero_rua = ''

    # Verifica se há vírgula
    if "," in parte_endereco[0]:
        numero_rua, *nome_rua = parte_endereco[0].split(",")  # Divide núm/rua
        nome_rua = ' '.join(nome_rua + parte_endereco[1:])  
    else:
        # Verifica se há "No"
        if parte_endereco[-1].lower() == "no":
            numero_rua = parte_endereco[-1] + " " + parte_endereco[-2]  
            nome_rua = ' '.join(parte_endereco[:-2])  
        else:
            numero_rua = parte_endereco[-1]  # Última parte = número
            nome_rua = ' '.join(parte_endereco[:-1])  

    return nome_rua.strip(), numero_rua.strip()

testes = ["4, Rue de la République", "100 Broadway Av", "Calle Sagasta, 26", "Calle 44 No 1991"]

for teste in testes:
    rua, numero = str_endereco(teste)
    print(f"'{teste}' = '{rua}', '{numero}'")

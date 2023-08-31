contagem = {}

frase = input("Informe o texto: ")

#garante que a letra seja minuscula
frase = frase.lower()

for letra in frase:
    if letra != ' ':
        if letra in contagem:
            contagem[letra] = contagem[letra] + 1
        else: 
            contagem[letra] = 1

for chave in contagem:
    print(chave, "->", contagem[chave])
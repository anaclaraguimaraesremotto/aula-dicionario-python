def inverte(dic):
    outro_dic = {}

    for chave in dic:
        valor = dic[chave]
        outro_dic[valor] = chave
    return outro_dic

frutas = {'apple' : 'maçã', 'strawberry' : 'morango',
          'watermelon' : 'melancia', 'orange' : 'laranja',
          'passion fruit' : 'maracujá',
          'peach' : 'pêssego', 'pineapple' : 'abacaxi',
          'lemon' : 'limão', 'avocado' : 'abacate'}

fruta_invertida = inverte(frutas)

print(fruta_invertida)

try: 
    print(fruta_invertida['banana'])
except KeyError as erro:
    print("Chave não encontrada, avise o desenvolvedor")
    #envie um email para anaclaraguimaraesremotto@gmail.com
    #com o conteúdo do erro
    print(erro)
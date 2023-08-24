agenda = {}

agenda['ana'] = "ana@gmail.com"
agenda['beto'] = "beto@yahoo.com"
agenda['cicero'] = "cicero@fiap.com"
agenda['davi'] = "david@gmail.com"

print(agenda)
# {'ana': 'ana@gmail.com', 'beto': 'beto@yahoo.com', 'cicero': 'cicero@fiap.com', 'davi': 'david@gmail.com'}

# substituindo
agenda['beto'] = "roberto@gmail.com"

print(agenda)
# {'ana': 'ana@gmail.com', 'beto': 'roberto@gmail.com', 'cicero': 'cicero@fiap.com', 'davi': 'david@gmail.com'}

# atribuido mais de um email (significado) usando lista
agenda['beto'] = ["roberto@gmail.com", agenda['beto']]

print(agenda)
# {'ana': 'ana@gmail.com', 'beto': ['roberto@gmail.com', 'roberto@gmail.com'], 'cicero': 'cicero@fiap.com', 'davi': 'david@gmail.com'}
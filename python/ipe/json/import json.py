import json

obj = {'chave1':'valor1', 'chave2':'valor2'}
print(obj)
strJSON = json.dumps(obj)
print(strJSON)
obj2 = open('arquivo.json', 'w')
json.dump(obj, obj2)
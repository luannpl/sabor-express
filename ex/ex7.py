pessoa = {'nome': 'Luan', 'idade': '23', 'cidade':'Fortaleza'}

pessoa['nome'] = 'Jesus'
pessoa['profissao'] = 'Desenvolvedor de Software'
print(pessoa)

pessoa.pop('cidade')
print(pessoa)

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)
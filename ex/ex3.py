usuario = 'luaanpl'
senha = 'luanzin123'

usuario_pede = input('Digite o seu nome de usuário: ')
senha_pede = input('Digite sua senha: ')

if usuario_pede == usuario and senha_pede == senha:
    print('Acesso permitido')
else:
    print('Usuário ou senha inválido')
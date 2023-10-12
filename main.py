from Cadastro import Cadastro
pessoas = ['ornã', 'bruna', 'malu', 'eve']
dados = ['nome', 'cpf', 'nº']

supermercado = Cadastro(pessoas, dados)

"""descomente a linha abaixo se deseja cadastrar"""
#supermercado.Cadastrar('arquivo.txt')

supermercado.LerDados('arquivo.txt')
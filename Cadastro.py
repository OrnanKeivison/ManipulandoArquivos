class Cadastro:
    def __init__(self, pessoas, dados):
        self._pessoas = pessoas
        self._dados = dados

    def getPessoas(self):
        return self._pessoas

    def getDados(self):
        return self._dados

    def setPessoas(self, pessoas):
        self._pessoas = pessoas
    
    def setDados(self, dados):
        self._pessoas = dados

    def Cadastrar(self, arquivo):
        arquivo = open(arquivo, 'a')

        for pessoa in self.getPessoas():
            for dado in self.getDados():
                dados_pessoais = input(f'digite seu {dado}:')
                arquivo.write(f'\n{dados_pessoais}')
            print(' ')
            arquivo.write('\n ')
        
        arquivo.close()
    
    def LerDados(self, arquivo):
        arquivo = open(arquivo, 'r')

        for linha in arquivo:
            print(linha, end=" ")

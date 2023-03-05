class Gasto:

    def tipo_escolha_produto(self, tipo_produto):
        if tipo_produto == 1:
            return f'você selecionou Alimento'


        elif tipo_produto == 2:
            return f'Você selecionou Casa'

        elif tipo_produto == 3:
            return f'Você selecionou Gastos diversos'


    def informacoes_produtos(self):
        self.tipo_produto = str(input('Selecione o tipo do produto: [1]Alimentos | [2]Contas de Casa | [3] Gastos Diversos : '))
        self.tipo_produto = self.tipo_escolha_produto(self.tipo_produto)
        self.info = str(input('Infome o produto: '))
        self.produto = self.info
        self.quantidade_produto = int(input('Informe a quantidade: '))
        self.valor_produto = int(input('Informe o valor: '))



    def calculo_quantidade(self):
        self.informacoes_produtos()
        return f'A quantidade comprada é: R${self.quantidade_produto * self.valor_produto} '




info_produto = Gasto()
print(info_produto.calculo_quantidade())







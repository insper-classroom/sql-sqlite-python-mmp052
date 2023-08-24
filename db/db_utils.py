class SQL():
    def __init__(self,conn,nome_tabela):
        self.conn = conn
        self.cursor = conn.cursor()
        self.nome_tabela = nome_tabela

    def cria_tabela(self, colunas:list):
        '''
        colunas : lista de tuplas, onde o primeiro valor é o nome da coluna e o segundo é o tipo
        '''
        query = f'CREATE TABLE IF NOT EXISTS {self.nome_tabela} (ID INTEGER PRIMARY KEY AUTOINCREMENT,'

        for coluna in colunas:
            query += f'{coluna[0]} {coluna[1]}'
            if coluna != colunas[-1]:
                query += ','

        query += ');'
        self.cursor.execute(query)

    def inserir(self, nome_colunas:list, lista_valores:list, varios = 0):
        query = f'INSERT INTO {self.nome_tabela} ('
        query2 = ' VALUES ('

        for i in range(len(nome_colunas)):
            query += f'{nome_colunas[i]}'
            query2 += '?'
            if i != len(nome_colunas) - 1:
                query += ','
                query2 += ','
        query += ')'
        query2 += ')'

        query =f'{query}{query2}'

        self.cursor.executemany(query, lista_valores)

        self.conn.commit()

    def selecionar(self, coluna:str = '*', filtro:str = ''):
        '''
        coluna: nome das colunas que voce quer que retorne ex(nome,idade)
        filtro: valor dos filtros a partir do WHERE ex(nome == "ana" AND idade == 14)
        '''
        if filtro == '':
            self.cursor.execute(f'SELECT {coluna} FROM {self.nome_tabela}')
        else:
            self.cursor.execute(f'SELECT {coluna} FROM {self.nome_tabela} WHERE {filtro}')

        return self.cursor.fetchall()

    def atualizar(self, coluna, valor, coluna_filtro, valor_filtro):
        self.cursor.execute(f'UPDATE {self.nome_tabela} SET {coluna} = ? WHERE {coluna_filtro} == ?',(valor, valor_filtro))

    def deletar(self, coluna, valor):
        self.cursor.execute(f'DELETE FROM {self.nome_tabela} WHERE {coluna} = ?', (valor,))
        self.conn.commit()

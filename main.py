import pandas as pd
from twilio.rest import Client
account_sid = "AC2628af3ef76cd40c0089afb9bfa8d7bf"
auth_token = "efcf79aafdb10f0a995188d8825be60d"
client = Client(account_sid, auth_token)
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'O vendedor {vendedor} bateu a meta ao vender R${vendas} no mês de {mes}.')
        message = client.messages.create(
            to="+5521972795556",
            from_="+16093364135",
            body=f'O vendedor {vendedor} bateu a meta ao vender R${vendas} no mês de {mes}.')
        print(message.sid)
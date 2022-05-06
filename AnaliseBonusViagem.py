import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC1d0e2adf8e93769c111612a4b97509bc"
# Your Auth Token from twilio.com/console
auth_token = "3c9d86be4fbe68d7972443926f7d0253"
client = Client(account_sid, auth_token)

# abrir os seis arquivos em Excel

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():

        # .loc[linha, coluna] ajuda a identificar uma ou mais linhas da tabela
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5587981812358",
            from_="+19803684171",
            body=f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)

# Para cada arquivo:

# verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000

# se for maior do que 55.000 -> Envia um sms com o nome, mês e as vendas do
# vendedor

# caso não seja maior que 55.000 não quero fazer nada

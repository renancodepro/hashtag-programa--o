import pandas as pd
from twilio.rest import Client

# que temos que baixar com pip install

# pandas - integração do python com excel
# openpyxl - mesmo de cima
# twilio - integração do python com sms

# passo a passo de solução

# abrir os seis arquivos em Excel

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():

        # .loc[linha, coluna] ajuda a identificar uma ou mais linhas da tabela
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')




# Your Account SID from twilio.com/console
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675309", 
    from_="+15017250604",
    body="Hello from Python!")

print(message.sid)
# Para cada arquivo:

# verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000

# se for maior do que 55.000 -> Envia um sms com o nome, mês e as vendas do
# vendedor

# caso não seja maior que 55.000 não quero fazer nada

import smtplib

# servidor ----- S M T P - SIMPLE MAIL TRANSFER PROTOCOL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import secreto
from datetime import datetime

now = datetime.now()
horas = now.strftime("%H:%M")

data = datetime.now()
dataAtual = datetime.strftime(data, '%d/%m/%Y')
envio = False


def enviar_email(preco_dolar, preco_euro, preco_ouro, usuario, destino):
    try:

        # 1 - STARTAR O SERVIDOR SMTP
        host = 'smtp.gmail.com'
        port = '587'
        login = secreto.login
        senha = secreto.senha
        server = smtplib.SMTP(host, port)
        server.ehlo()
        server.starttls()
        server.login(login, senha)
        # construir email
        corpo = fr"""
        Olá {usuario}!
        Seja bem-vindo ao sistema de cotação de moedas!
                
        A cotação do DÓLAR no dia {dataAtual}, foi de R$ {preco_dolar}
        A cotação do EURO no dia {dataAtual}, foi de R$ {preco_euro}
        A cotação do OURO no dia {dataAtual}, foi de R$ {preco_ouro}
        
        Essas atualizações são de: {dataAtual} às {horas}.
        
        -Email Automático === Daniel Cardeal
               
"""
        email_msg = MIMEMultipart()
        email_msg['FROM'] = secreto.login
        email_msg['TO'] = destino
        email_msg['Subject'] = f"Cotação Dolar,Euro e Ouro Hoje: {dataAtual}"
        email_msg.attach(MIMEText(corpo, 'plain'))

        # colocar anexo :

        # # anexo
        # # abrir o arquivo em mode leitura e binary
        # caminho = r'E:\Downloads\Vendas.xlsx'
        # anexo = open(caminho, 'rb')
        # # lemos o arquivo no modo binario e jogamos codificado em base 64( que é o que o e-mail precisa)
        # att = MIMEBase('application', 'octet-stream')
        # att.set_payload(anexo.read())
        # encoders.encode_base64(att)
        #
        # # adiciona o cabeçalho no tipo do anexo de email
        # att.add_header('Content-Disposition', 'anexo; filename = Vendas.xlsx')
        #
        # # fecha o arquivo
        # anexo.close()
        # # coloca o anexo no email
        # email_msg.attach(att)

        server.sendmail(email_msg['FROM'], email_msg['TO'], email_msg.as_string())
        envio = True
        server.quit()
    except Exception as er:
        print(er)

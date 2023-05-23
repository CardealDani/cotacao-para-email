from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import envio_de_email
import locale
import time
import pyautogui

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

emails = []
print('=============== COTAÇÃO DOLAR|EURO|OURO ===============\n')

usuario = input('Digite seu nome: ').title()
usuario_email = input('Digite um email válido para receber as cotações: ')

emails.append(usuario_email.strip())

caminho = r'chromedriver.exe'
s = Service(caminho)
navegador = webdriver.Chrome(service=s)
navegador.maximize_window()
navegador.get('https://www.google.com/')
# xpath ---- identificador dos elementos de um site
navegador.find_element \
    ('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys('cotação dolar',
                                                                                               Keys.ENTER)
dolar = navegador.find_element \
    ('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

navegador.get('https://www.google.com/')
navegador.find_element \
    ('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys('cotação euro',
                                                                                               Keys.ENTER)
euro = navegador.find_element \
    ('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

navegador.get("https://www.melhorcambio.com/ouro-hoje")

ouro = navegador.find_element \
    ('xpath', '//*[@id="comercial"]').get_attribute('value')

dolar = float(dolar)
euro = float(euro)
round(dolar, 2)
round(euro, 2)

dolar_real = locale.currency(dolar)
euro_real = locale.currency(euro)
print('Aguarde enquanto calculamos... ')
navegador.close()
print('Enviando email...')
try:
    for email in emails:
        envio_de_email.enviar_email(dolar_real, euro_real, ouro, usuario, usuario_email)
    print('Email enviado!')
    pyautogui.alert('Email enviado com Sucesso!\nVerifique seu Email!')
    print('Servidor encerrando em 3')
    time.sleep(1)
    print('Servidor encerrando em 2')
    time.sleep(1)
    print('Servidor encerrando em 1')
    time.sleep(1)

except:
     print('Ops, aconteceu um erro!\nVerifique o email e tente novamente!')


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

#instalar o chrome dirver atual
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
time.sleep(2)

navegador.get("https://site-teste")# site teste
navegador.find_element('xpath','//*[@id="open-login"]').click()
time.sleep(2)
navegador.find_element('xpath','//*[@id="login-form"]/div[2]/input').send_keys('my_empresa')#empresa
time.sleep(1)
navegador.find_element('xpath','//*[@id="login-form"]/div[3]/input').send_keys('my_user')#usuario
time.sleep(1)
navegador.find_element('xpath','//*[@id="login-form"]/div[4]/input').send_keys('my_password')#senha
time.sleep(2)
#navegador.find_element('xpath','//*[@id="recaptcha-anchor-label"]').click() # try click in captcha
time.sleep(3)
navegador.find_element('xpath','//*[@id="login-submit"]').click()
time.sleep(10)# botao login
navegador.close()

 



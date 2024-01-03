from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--icognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()),options=chrome_options)
    
    return driver

driver = iniciar_driver()
# entrar no site
driver.get("https://cursoautomacao.netlify.app")

# encontrar e clicar no elemento desafios
desafios = driver.find_element(By.XPATH, '//*[@id="navbarsExample04"]/ul[2]/li[2]/a')
desafios.click()
sleep(1)
# Rolar X quantidade em pixels(descer)
driver.execute_script("window.scrollTo(0, 400);")
sleep(1)
# encontrar e digitar no campo especificado
campo_nome = driver.find_element(By.ID, 'dadosusuario')
sleep(1)
campo_nome.send_keys('Marcos Rogério Martins Feitosa')
sleep(1)
# encontrar e clicar no botão 'clique aqui'
botao_clique_aqui = driver.find_element(By.ID, 'desafio2')
sleep(1)
botao_clique_aqui.click()

# dar um scroll para baixo
driver.execute_script("window.scrollTo(0, 600);")
sleep(1)
# encontrar o campo especificado e digitar novamente o nome
validar_nome = driver.find_element(By.ID, 'escondido')
validar_nome.send_keys('Marcos Rogério Martins Feitosa')
sleep(1)
# clicar no botão validar
botao_validar = driver.find_element(By.ID, 'validarDesafio2')
botao_validar.click()

input("")
driver.close()

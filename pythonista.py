from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1280,720', '--icognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()),options=chrome_options)
    
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver, wait

driver, wait = iniciar_driver()

driver.get("https://automatize.netlify.app/")
sleep(1)

campo_email = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='email']")))
sleep(1)
campo_email.send_keys('marcospython@python.com')
sleep(1)

campo_senha = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='senha']")))
sleep(1)
campo_senha.send_keys('1234567')
sleep(1)

botao_enviar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
sleep(1)
botao_enviar.click()

driver.close()

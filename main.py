#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import dotenv
import os


# In[2]:


# Configuração do ChromeDriver usando o caminho absoluto
driver = webdriver.Chrome()


# In[3]:


# Carregue as variáveis de ambiente do arquivo .env
dotenv.load_dotenv('.env')

# Leitura das variáveis de ambiente do arquivo .env
alura_email = os.getenv('ALURA_EMAIL')
alura_password = os.getenv('ALURA_PASSWORD')
linkedin_email = os.getenv('LINKEDIN_EMAIL')
linkedin_password = os.getenv('LINKEDIN_PASSWORD')


# In[4]:


# Abra o site da Alura
driver.get('https://www.alura.com.br/loginForm')

# Aguarde até que o campo de email esteja visível
email_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//input[@name="username"]'))
)
email_input.send_keys(alura_email)

# Aguarde até que o campo de senha esteja visível
password_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//input[@name="password"]'))
)
password_input.send_keys(alura_password)
password_input.send_keys(Keys.RETURN)  # Pressione a tecla "Enter" no campo de senha


# In[8]:


driver.get('https://cursos.alura.com.br/user/charllys-lima')

# Encontre todos os botões com a classe "seeMoreButton" e clique neles
see_more_buttons = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CLASS_NAME, 'seeMoreButton'))
)

for button in see_more_buttons:
    button.click()


# In[9]:


class CursoAlura:
    def __init__(self, nome, link_linkedin):
        self.nome = nome
        self.link_linkedin = link_linkedin

# Lista para armazenar os cursos
cursos = []


# In[12]:


card_courses = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//li[@class="card-list__item"]'))
)

# Iterar e encontrar elementos dentro de cada card
for card in card_courses:
    course_name = card.find_element(By.CLASS_NAME, 'course-card__name')
    linkedin_link = card.find_element(By.CLASS_NAME, 'course-card__linkedin')
    
    print("Nome do Curso:", course_name.text)
    print("Link do LinkedIn:", linkedin_link.get_attribute('href'))

    # Criar um objeto Curso e adicioná-lo à lista de cursos
    curso = CursoAlura(course_name, linkedin_link)
    cursos.append(curso)


# In[14]:


# Abre uma nova guia usando JavaScript
driver.execute_script("window.open('about:blank', 'new_tab')")

# Alterna para a nova guia
driver.switch_to.window("new_tab")

# Agora você pode carregar uma URL na nova guia
driver.get("https://www.linkedin.com/login/")



#!/usr/bin/env python
# coding: utf-8

# In[12]:


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import dotenv
import os


# In[13]:


# Configuração do ChromeDriver usando o caminho absoluto
driverAlura = webdriver.Chrome()

# Defina o tamanho da janela como metade da largura da tela
largura_tela = driverAlura.execute_script("return window.screen.width")
altura_tela = driverAlura.execute_script("return window.screen.height")
driverAlura.set_window_size(largura_tela // 2, altura_tela)

# Mova a janela para a lateral esquerda
driverAlura.set_window_position(0, 0)

driverLinkedin = webdriver.Chrome()

# Defina o tamanho da janela como metade da largura da tela
largura_tela = driverLinkedin.execute_script("return window.screen.width")
altura_tela = driverLinkedin.execute_script("return window.screen.height")
driverLinkedin.set_window_size(largura_tela // 2, altura_tela)

# Calcule a posição X para que a janela fique à direita da tela
largura_janela = driverLinkedin.get_window_rect()['width']
posicao_x = largura_tela - largura_janela

# Mova a janela para a lateral direita
driverLinkedin.set_window_position(posicao_x, 0)


# In[14]:


# Carregue as variáveis de ambiente do arquivo .env
dotenv.load_dotenv('.env')

# Leitura das variáveis de ambiente do arquivo .env
alura_email = os.getenv('ALURA_EMAIL')
alura_password = os.getenv('ALURA_PASSWORD')
linkedin_email = os.getenv('LINKEDIN_EMAIL')
linkedin_password = os.getenv('LINKEDIN_PASSWORD')
linkedin_nickname = os.getenv('LINKEDIN_NICKNAME')


# In[15]:


# Abra o site da Alura
driverAlura.get('https://www.alura.com.br/loginForm')

# Aguarde até que o campo de email esteja visível
email_input = WebDriverWait(driverAlura, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//input[@name="username"]'))
)
email_input.send_keys(alura_email)

# Aguarde até que o campo de senha esteja visível
password_input = WebDriverWait(driverAlura, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//input[@name="password"]'))
)
password_input.send_keys(alura_password)
password_input.send_keys(Keys.RETURN)  # Pressione a tecla "Enter" no campo de senha


# In[16]:


driverAlura.get('https://cursos.alura.com.br/user/charllys-lima')

# Encontre todos os botões com a classe "seeMoreButton" e clique neles
see_more_buttons = WebDriverWait(driverAlura, 10).until(
    EC.visibility_of_all_elements_located((By.CLASS_NAME, 'seeMoreButton'))
)

for button in see_more_buttons:
    button.click()


# In[17]:


class CursoAlura:
    def __init__(self, nome, link_linkedin):
        self.nome = nome
        self.link_linkedin = link_linkedin

# Lista para armazenar os cursos
cursos = []


# In[18]:


card_courses = WebDriverWait(driverAlura, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//li[@class="card-list__item"]'))
)

# Iterar e encontrar elementos dentro de cada card
for card in card_courses:
    course_name = card.find_element(By.CLASS_NAME, 'course-card__name')
    linkedin_link = card.find_element(By.CLASS_NAME, 'course-card__linkedin')
    
    print("Nome do Curso:", course_name.text)
    print("Link do LinkedIn:", linkedin_link.get_attribute('href'))

    # Criar um objeto Curso e adicioná-lo à lista de cursos
    curso = CursoAlura(course_name.text, linkedin_link.get_attribute('href'))
    cursos.append(curso)


# In[19]:


# Abra site do linkedin
driverLinkedin.get("https://www.linkedin.com/login/")

# Aguarde até que o campo de email esteja visível
email_input = WebDriverWait(driverLinkedin, 10).until(
    EC.visibility_of_element_located((By.ID, 'username'))
)
email_input.send_keys(linkedin_email)

# Aguarde até que o campo de senha esteja visível
password_input = WebDriverWait(driverLinkedin, 10).until(
    EC.visibility_of_element_located((By.ID, 'password'))
)
password_input.send_keys(linkedin_password)
password_input.send_keys(Keys.RETURN)  # Pressione a tecla "Enter" no campo de senha



# In[21]:


driverLinkedin.get("https://www.linkedin.com/in/" + str(linkedin_nickname) +"/details/certifications/")

# Role a página para baixo várias vezes para garantir que todo o conteúdo seja carregado
for _ in range(10):
    # Rola a página para o final
    driverLinkedin.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)  # Espere um pouco para o conteúdo carregar


# In[22]:


for curso in cursos:
    try:
        # Tente localizar o elemento com XPath contendo o texto desejado
        span_element = WebDriverWait(driverLinkedin, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//span[text()="' + str(curso.nome) + '"]'))
        )
        print("CURSO JA CADASTRADO")
        print(curso.nome)
    except:
        print("CADASTRANDO CURSO")
        print(curso.nome)
        # Se o elemento não for encontrado, abra um link em outra aba
        driverLinkedin.execute_script('window.open("' + str(curso.link_linkedin) + '", "_blank");')
    
        # Mude o foco para a nova aba
        driverLinkedin.switch_to.window(driverLinkedin.window_handles[1])


        button_save = WebDriverWait(driverLinkedin, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-view-name="profile-form-save"]'))
        )
        button_save.click()

        # Feche a segunda aba
        driverLinkedin.close()

        # Mude o foco de volta para a primeira aba
        driverLinkedin.switch_to.window(driverLinkedin.window_handles[0])

        
        # Recarregue a primeira aba
        driverLinkedin.refresh()
        # Role a página para baixo várias vezes para garantir que todo o conteúdo seja carregado
        for _ in range(10):
            # Rola a página para o final
            driverLinkedin.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)  # Espere um pouco para o conteúdo carregar
        try:
            # Tente localizar o elemento com XPath contendo o texto desejado
            course = WebDriverWait(driverLinkedin, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//span[text()="' + str(curso.nome) + '"]'))
            )
            print("CURSO CADASTRADO COM SUCESSO.")
        except:
            print("FALHA")
            break
print("SINCRONIZACAO FEITA COM SUCESSO!")





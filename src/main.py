import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()
navegador.maximize_window()

# Acessa o site do G1
navegador.get("https://g1.globo.com")

# Salva bloco da última notícia.
ultima_noticia = navegador.find_element(By.CLASS_NAME, 'feed-post-body')

# Busca o título da ultíma notícia
titulo = ultima_noticia.find_element(By.CLASS_NAME,'_evt').text

# Busca a data de publicação da ultíma notícia
data_publicacao = ultima_noticia.find_element(By.CLASS_NAME,'feed-post-datetime').text

# Busca o resumo da ultíma notícia, tem notícias sem resumo e outras com links relacionados ou apenas o texto de resumo da própria notícia
try:
    resumo = ultima_noticia.find_element(By.CLASS_NAME,'bstn-fd-relatedtext').text.strip()
except:
    try:
        resumo = ultima_noticia.find_element(By.CLASS_NAME,'feed-post-body-resumo').text.strip()
    except:
        resumo = 'Matéria sem resumo'


# print(titulo)
# print(data_publicacao)
# print(resumo)

# Salvando em JSON
dados = {
        "titulo": titulo,
        "data_publicacao": data_publicacao,
        "resumo": resumo,
    }

with open("ultima_materia.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

# Salvando em Excel
df = pd.DataFrame([dados])
df.to_excel("ultima_materia.xlsx", index=False)

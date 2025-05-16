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

titulo = navegador.find_element(By.CSS_SELECTOR, "div.bastian-feed-item a.feed-post-link").text.strip()
data_publicacao = navegador.find_element(By.CSS_SELECTOR, "div.feed-post-metadata span.feed-post-datetime").text.strip()
resumo = navegador.find_element(By.CSS_SELECTOR, "div.bstn-related a").text.strip()

print(titulo)
print(data_publicacao)
print(resumo)

dados = {
        "titulo": titulo,
        "data_publicacao": data_publicacao,
        "resumo": resumo,
    }

with open("ultima_materia.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

    # Salva em Excel
df = pd.DataFrame([dados])
df.to_excel("ultima_materia.xlsx", index=False)

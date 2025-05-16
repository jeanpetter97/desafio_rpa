# 📰 Coletor de Última Notícia do G1

Este projeto é um script Python simples que utiliza **Selenium** para acessar o site [G1](https://g1.globo.com), extrair a **última matéria publicada**, e salvar os seguintes dados:

- Título da notícia  
- Data de publicação  
- Resumo (caso exista)  

Os dados são armazenados em dois formatos:
- `ultima_materia.json`
- `ultima_materia.xlsx`

---

## 🚀 Tecnologias Utilizadas

- [Python 3.8+](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/) (para salvar em Excel)
- WebDriver do Google Chrome (Chromedriver)

---

## 🔧 Instalação

1. **Clone o repositório** (ou baixe o `main.py`):
   ```bash
   git clone https://github.com/seu-usuario/projeto-g1-noticia.git
   cd projeto-g1-noticia
   ```

2. **Instale as dependências:**
   ```bash
   pip install selenium pandas openpyxl
   ```

3. **Baixe o ChromeDriver** compatível com sua versão do Google Chrome:  
   👉 [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)  
   E coloque o executável no mesmo diretório do projeto ou adicione ao `PATH`.

---

## ▶️ Como Executar

```bash
python main.py
```

O script irá:

- Abrir o site do G1
- Localizar a última notícia publicada
- Extrair título, data e resumo
- Salvar em:
  - `ultima_materia.json`
  - `ultima_materia.xlsx`

---

## 📂 Estrutura dos Arquivos Gerados

### `ultima_materia.json`
```json
{
  "titulo": "Exemplo de título da última matéria",
  "data_publicacao": "15/05/2025 11h30",
  "resumo": "Resumo da notícia aqui."
}
```

### `ultima_materia.xlsx`

| titulo                        | data_publicacao     | resumo                    |
|------------------------------|---------------------|---------------------------|
| Exemplo de título da matéria | 15/05/2025 11h30     | Resumo da notícia aqui.   |

---

## ❗ Observações

- Algumas matérias não possuem resumo ou possuem diferentes blocos de texto (link relacionado ou descrição direta).
- O script trata automaticamente esses diferentes casos.

---

## 📄 Licença

Este projeto é livre para uso educacional e pessoal.

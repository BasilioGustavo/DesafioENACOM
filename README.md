# ENACOM - Bootcamp Seletivo Data Analytics 2024

Projeto de desenvolvimento de modelos preditivos para geração de energia elétrica no Brasil, de acordo com a [base pública](https://dados.ons.org.br/dataset/geracao-usina-2) do Operador Nacional do Sistema Elétrico (ONS). 

## 🚀 Começando

Essas descrições permitirão que você obtenha um melhor entendimento da estrutura do projeto, possibilitando a operação na sua máquina local para fins de avaliação e teste. 

### **Instalando as dependências necessárias:**

No ambiente em sua máquina, é necessário verificar se as dependências requeridas dentro do arquivo `requirements.txt` disponível acima já existe no seu ambiente. Caso não, ative o seu ambiente e execute

```

pip install -r requirements.txt
```



## **[Dados](/dados/)**

### ⚙️ Fonte de dados

* [ONS](https://dados.ons.org.br/dataset/geracao-usina-2) - Dados brutos (2000-2020)
* [Reamostrados](/dados/reamostrados/) - Dados na frequência mensal
* [Segmentados](/dados/segmentados/) - Dados segmentados por fontes

## **[Notebooks](/notebooks)**

### 🛠️ Construído com

* [Pandas](https://pandas.pydata.org/docs/) - Análise de dados
* [Dask](https://docs.dask.org/en/stable/) - Análise de dados com paralelismo
* [Plotly](https://plotly.com/python/) - Visualização de dados
* [Scikit Learn](https://scikit-learn.org/stable/user_guide.html) - Desenvolvimento de modelos preditivos

### [Concatenação e Reamostragem](/notebooks/concatenar_dados_e_reamostragem.ipynb)
Nesse notebook é realizado o processo de pré-processamento dos dados, partindo da junção dos arquivos separados em base única, além da eliminação de colunas redundantes, e por fim, a reamostragem dos dados.

### [Análise Exploratória](/notebooks/analise_exploratoria.ipynb)
Nesse notebook é apresentado o modo que os dados foram explorados, partindo do dataset bruto e segmentando-os até a definição das entradas dos modelos preditivos.

### [Modelos Preditivos](/notebooks/modelos_preditivos.ipynb)
Nesse notebook são apresentadas as técnicas de predição utilizadas, como também a análise de desempenho dos modelos preditivos.

## ✒️ Autor

* **[Gustavo Basílio](https://github.com/BasilioGustavo)** 




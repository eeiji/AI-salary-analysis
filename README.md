# 📊 Job Market Analysis – Data Science Salaries

Projeto de **análise exploratória e modelagem preditiva** para entender padrões salariais na área de **Data Science e Inteligência Artificial**.

O objetivo é:

* Explorar padrões salariais no dataset
* Identificar outliers e tendências
* Analisar fatores que influenciam salários
* Construir um modelo de **previsão de salário**

---

# 🚀 Tecnologias utilizadas

O projeto foi desenvolvido com:

* **pandas** → manipulação de dados
* **Plotly** → visualização de dados
* **scikit-learn** → criação dos modelos de machine learning
* **Streamlit** → dashboard interativo

---

# 📂 Estrutura do projeto

```
job_market_analysis/

dataset/
   salaries.csv

analysis.py
app.py
README.md
requirements.txt
```

* **analysis.py** → análise exploratória e treinamento dos modelos
* **app.py** → dashboard interativo com Streamlit
* **dataset** → base de dados utilizada

---

# 📈 Análise exploratória dos dados

## Identificação de outliers

Foi utilizado um **gráfico boxplot** para analisar e identificar possíveis outliers no conjunto de dados.

Durante a análise foi identificado um valor extremo:

```
Salary: US$800.000,00
```

Após análise, o valor **não foi removido**, pois pode representar um salário real para cargos altamente especializados ou executivos.

---

# 📊 Principais insights

## Experiência vs salário

A análise mostrou que cargos de nível **Executivo (EX)** **não apresentam a maior mediana salarial**.

Isso pode ocorrer devido a:

* Menor número de registros para esse nível no dataset
* Variações relacionadas à localização da empresa
* Diferenças entre cargos executivos específicos

---

## Cargos mais bem pagos

A análise de salários por cargo mostrou que:

**Analytical Engineering Manager** é o cargo mais bem pago no dataset.

```
Média salarial ≈ US$400.000,00
```

---

## Tamanho da empresa

A análise mostrou que:

* Empresas de **tamanho médio (M)** apresentam os **maiores salários**
* Também possuem **maior quantidade de registros no dataset**

Isso indica que empresas médias possuem forte representatividade no conjunto de dados analisado.

---

# 🤖 Modelos preditivos

Foram testados dois modelos de machine learning utilizando **scikit-learn**:

### 1️⃣ Random Forest

Modelo final utilizado:

**Random Forest**

Esse modelo foi escolhido por capturar relações **não lineares** entre as variáveis.

---

### 2️⃣ K-Nearest Neighbors

Também foi testado o modelo:

**K-Nearest Neighbors**

Porém os resultados obtidos foram **piores**, portanto ele não foi utilizado como modelo final.

---

# 📉 Resultados do modelo

Métricas obtidas:

```
MAE ≈ 40.000 USD
R² ≈ 0.31
```

### Interpretação

**MAE (Mean Absolute Error)**
O modelo apresenta um erro médio de aproximadamente **46 mil dólares** na previsão do salário.

**R² (coeficiente de determinação)**
O modelo explica cerca de **2,8% da variação dos salários**.

Isso indica que existem fatores relevantes que **não estão presentes no dataset**, como:

* Experiência real
* Habilidades técnicas específicas
* Setor da empresa
* Negociação salarial
* Localização mais detalhada

---

# 📉 Análise do gráfico de previsão

## Previsão vs Salário Real

O gráfico compara os **salários reais** com os **salários previstos pelo modelo**.

### Interpretação

* A maioria dos dados está concentrada entre **US$50k e US$250k**, indicando maior quantidade de exemplos nessa faixa.
* Existe uma **tendência positiva**, onde salários reais maiores resultam em previsões maiores.
* Para um mesmo valor de salário real, o modelo pode produzir previsões relativamente diferentes.
* Observa-se **dispersão significativa**, indicando erros relevantes nas previsões.
* Para salários muito altos (acima de ~US$400k), o modelo tende a **subestimar os valores reais**, provavelmente devido à menor quantidade de exemplos nessa faixa salarial.

---

# 🖥 Dashboard interativo

O projeto inclui um dashboard interativo desenvolvido com **Streamlit**.

Para executar localmente:

```bash
streamlit run app.py
```

---

# 📌 Possíveis melhorias

Algumas melhorias futuras incluem:

* Engenharia de features
* Uso de modelos mais avançados (Gradient Boosting / XGBoost)
* Filtragem de cargos raros
* Análise mais detalhada por país
* Aumento da performance do modelo

---

# 🎯 Objetivo do projeto

Este projeto foi desenvolvido para praticar conceitos de **Ciência de Dados**, incluindo:

* Análise exploratória de dados (EDA)
* Visualização de dados
* Machine Learning
* Construção de dashboards interativos

# -*- coding: utf-8 -*-
"""Avocado.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KX_Mulkhs4eTij9eLPWGEPnYvaoetynP
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle

data = pd.read_csv('avocado.csv')

# Identificar a coluna que contém strings
coluna_strings = "type"

# Converter as strings para números inteiros
data[coluna_strings] = data[coluna_strings].map({"conventional": 1, "organic": 2})

# Visualizar o conjunto de dados
print(data)

type = data['type']
pickle.dump(type, open('type.pkl','wb'))
typeLoads = pickle.load(open('type.pkl','rb'))
print(type)

# Dividir os dados em recursos (X) e rótulos (y)
X = data.drop('type', axis=1)  # Substitua 'classe' pelo nome da coluna que contém os rótulos
y = data['type']

# Dividir os dados em um conjunto de treinamento e um conjunto de teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3)

print(X.columns)

#X = pd.get_dummies(X, columns=['type'], prefix=['type'])


# Criar e treinar um modelo de árvore de decisão
clf = DecisionTreeClassifier()
clf = clf.fit(X_treino, y_treino)

# Fazer previsões
preditos = clf.predict(X_teste)

# Avaliar o desempenho do modelo
acuracia = accuracy_score(y_teste, preditos)
print("Acuracia:", acuracia)

# Salvar o modelo treinado
import pickle
pickle.dump(clf, open('model.pkl', 'wb'))

# Carregar o modelo treinado
model = pickle.load(open('model.pkl', 'rb'))

# Fazer previsões com o modelo carregado
novos_dados = pd.DataFrame([[1.34, 6720.9, 2015]])  # Substitua pelos valores que você deseja prever
print(model.predict(novos_dados))
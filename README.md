# meli-probe-agents
Compliance continuo de servidores

Este código foi criado como desafio MELI, onde estão disponíveis dois componentes:

agent.py: obtem informações sobre servidores distribuídos no parque da empresa e envia para uma API de catálogo
api.py: concentra as informações dos agentes distribuídos, recebendo as especificações das máquinas e armazenando localmente em um arquivo .CSV

# Requisitos:

O código, gerado em Python 3, exige a instalação das seguintes bibliotecas:

 -- Flask: framework Web que suporta a API de coleta

Para instalá-la, é necessário executar o comando a seguir:

```python
python3 -m pip install Flask
```

# Etapas para execução:

 - Agentes:
 
 Executar o  comando a seguir:
 
 ```python
 python3 agent.py
 ```
 
 - API:
 
 Executar o comando a seguir:
 
  ```python
 python3 api.py
 ```

## **Table of Contents**
- [](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3b_e_02_anime_stock.html&ref=master#mcetoc_1f4uinjti0)
- [E12 - Anime Stock](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3b_e_02_anime_stock.html&ref=master#mcetoc_1f4uinjti1)
  - [Objetivo](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3b_e_02_anime_stock.html&ref=master#mcetoc_1f4uinjti2)
  - [Preparativos](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3b_e_02_anime_stock.html&ref=master#mcetoc_1f4uinjti3)
    - [Criando banco de dados e tabela](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3b_e_02_anime_stock.html&ref=master#mcetoc_1f4uinjti5)
    - [Estruturando pastas](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3b_e_02_anime_stock.html&ref=master#mcetoc_1f4uinjti5)
  - [Rotas](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3b_e_02_anime_stock.html&ref=master#mcetoc_1f6iaokr40)
    - [Exemplos de entradas e saídas](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3b_e_02_anime_stock.html&ref=master#mcetoc_1f5teqnma2)
    - [Criando rotas](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3b_e_02_anime_stock.html&ref=master#mcetoc_1f4uinjti5)
  - [](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3b_e_02_anime_stock.html&ref=master#mcetoc_1f4uinjti6)
  - [Rota - /animes - GET e POST](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3b_e_02_anime_stock.html&ref=master#mcetoc_1f4uinjti7)
  - [Rota - /animes/ - GET](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3b_e_02_anime_stock.html&ref=master#mcetoc_1f4uinjti9)
  - [](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3b_e_02_anime_stock.html&ref=master#mcetoc_1f4uinjtib)
  - [Rota - /animes/ - PATCH](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3b_e_02_anime_stock.html&ref=master#mcetoc_1f4uinjtic)
  - [](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3b_e_02_anime_stock.html&ref=master#mcetoc_1f4uinjtie)
  - [Rota - /animes/ - DELETE](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3b_e_02_anime_stock.html&ref=master#mcetoc_1f4uinjtif)
- [Entregáveis ](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3b_e_02_anime_stock.html&ref=master#mcetoc_1egvoav555j)
  - [Repositório ](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3b_e_02_anime_stock.html&ref=master#mcetoc_1egvrpv6k1l4)
    - [](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3b_e_02_anime_stock.html&ref=master#mcetoc_1egvrpv6k1l4)

- [Critérios de aceitação ](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/3b_e_02_anime_stock.html&ref=master#mcetoc_1eh146n6m3)
# **E12 - Anime Stock**
Anime Stock é um sistema para o armazenamento de animes.

## **Objetivo**
Trabalhar seus conhecimentos de **Flask, PostgreSQL, Blueprints e Psycopg2**.

## **Preparativos**
### **Criando banco de dados e tabela**
- **Crie** um banco de dados chamado **anime\_stock**

Em seguida, dentro do banco de dados **anime\_stock**,** você deve criar uma **TABELA** seguindo o padrão abaixo:

- **NOME DA TABELA**: **animes**
- **id**: **BIGSERIAL PRIMARY KEY**
- **anime**: **VARCAHR(100) NOT NULL UNIQUE**
- **released\_date**: **DATE NOT NULL**
- **seasons**: **INTEGER NOT NULL**

**OBS:** Siga as especificações da **tabela** conforme o solicitado, caso contrário, iremos desconsiderar sua tabela.

### **Estruturando pastas**
Você deverá seguir a seguinte estrutura de pastas:

├── app

│   ├── \_\_init\_\_.py

│   ├── services

│   │   └── \_\_init\_\_.py

│   └── views

│       └── \_\_init\_\_.py

├── .gitignore

└── requirements.txt
## **Rotas**
### **Exemplos de entradas e saídas**
Todos os exemplos de entradas e saídas estão [**neste link**](https://gitlab.com/cauanf/3a_kenzie_anime).

**OBS:** Os retornos > **NÃO** < precisam seguir na mesma ordem apresentada.

### **Criando rotas**
A conexão com o banco de dados deve ser feita através do PSYCOPG2.

**OBS: Siga os endpoints, status code e assinatura da função conforme solicitado, dessa maneira estamos dentro da convenção API RESTFul. Caso contrário iremos descontar da nota final.**

## **Rota - /animes - GET e POST**
- Especificações da rota:
  - Deve ser enfeitada pela **blueprint** :
    - **@bp\_animes**
  - **Assinatura** da função:
    - **get\_create()**
  - Deverá aceitar os **métodos**:
    - **POST e GET**
- **Rotina e retorno da requsição no método POST**:
  - **Verificação** se as chaves do json mandado pelo usuário são compativeis com a sua tabela do banco de dados.
    - Retorno **CASO AS CHAVES SEJAM INVÁLIDAS**:
      - Um **dicionário** contendo um **lista** das chaves que **são válidas e das chaves inválidas que foram mandadas**.
      - Status code **422**
  - **Criação** da tabela no banco de dados **caso ela não exista**.
  - O **nome** **do anime** deverá ser salvo como **título**.
  - **Inserção** dos dados mandado pela requisição.
    - Retorno **CASO O ANIME JÁ EXISTA NA TABELA DO BANCO DE DADOS**:
      - Um **dicionário** dizendo que o anime já existe no banco de dados.
      - Status code **422**.
    - Retorno **CASO O ANIME NÃO EXISTA NA TABELA DO BANCO DE DADOS**:
      - Um **dicionário** com os dados do anime criado.
      - Status code **201**.
- **Rotina e retorno da requsição no método GET**:
  - **Seleção** de todos os dados dessa tabela.
    - Retorno **CASO A TABELA ESTEJA VAZIA OU NÃO EXISTA**:
      - Um **dicionário** com uma **lista** vazia.
      - Status code **200**.
    - Retorno **CASO TENHA DADOS NA TABELA**:
      - Um **dicionário** com uma **lista** de **dicionários**.
      - Status code **200**.

## **Rota - /animes/<int:anime\_id> - GET**
- Especificações da rota:
  - Deve ser enfeitada pela **blueprint** :
    - **@bp\_animes**
  - **Assinatura** da função:
    - **filter()**
  - Deverá aceitar o **método**:
    - **GET**
  - Rotina deverá ser:
    - **Seleção** de um dado da tabela filtrado pelo **id**.
  - Retorno:
    - Caso haja dados na tabela deverá retornar: 
      - Um **dicionário** de **dicionário**.
      - Status code **200**.
    - Caso **não** haja dados na tabela, **não exista** o respectivo **id** ou a **tabela não exista** deverá retornar:
      - Um **dicionário**.
      - Status code **404**.

## **Rota - /animes/<int:anime\_id> - PATCH**
- Especificações da rota:
  - Deve ser enfeitada pela **blueprint** :
    - **@bp\_animes** 
  - **Assinatura** da função:
    - **update()**
  - Deverá aceitar o **método**:
    - **PATCH**
  - Rotina deverá ser:
    - **Verificação** se as chaves do json mandado pelo usuário são compativeis com a sua tabela do banco de dados.
      - Retorno **CASO AS CHAVES SEJAM INVÁLIDAS**:
        - Um **dicionário** contendo um **lista** das chaves que **são válidas e das chaves inválidas que foram mandadas**.
        - Status code **422**
    - Caso tenha a chave **anime** o valor deverá ser salvo como **título**.
    - **Atualização** dos dados do **id** mandado pela url da requisição com os dados da recebidos.
  - Retorno **CASO O ANIME EXISTA**:
    - Um **dicionário** com os dados atualizados.
    - Status code **200**.
  - Retorno **CASO O ANIME** ou **TABELA NÃO EXISTAM**:
    - Um **dicionário**.
    - Status code **404**.

## **Rota - /animes/<int:anime\_id> - DELETE**
- Especificações da rota:
  - Deve ser enfeitada pela **blueprint** :
    - **@bp\_animes**
  - **Assinatura** da função:
    - **delete()**
  - Deverá aceitar o **método**:
    - **DELETE**
  - Rotina deverá ser:
    - **Verificação** se o **id** passado existe.
  - Retorno **CASO O ID EXISTA**:
    - Uma **string** -> **no content**.
    - Status code **204**.
  - Retorno **CASO O ID** ou **TABELA NÃO EXISTA**:
    - Um **dicionário**.
    - Status code **404**.
-----
# **Entregáveis** 
## **Repositório** 
- Link do **repositório** do **GitLab** 
- **Código fonte:** 
  - Diretório app. 
- **Privacidade** 
  - Incluir **ka-br-out-2020-correcoes** como reporter. 
### -----
# **Critérios de aceitação** 

|**Pts** |**Dado** |**Quando** |**É esperado** |
| :-: | :-: | :-: | :-: |
|2|database e tabela|Verificado|Que siga o formato solicitado|
|2|blueprint|Verificado|Que siga o formato solicitado|
|1|estrutura de pastas|Verificado|Que siga o formato solicitado|
|1|psycopg2|Verificado|Que faça todas as operações solicitadas no banco de dados |
|2|Rota get e post|Feita a requisição|Que retorne o esperado|
|2|Rota update delete|Feita a requisição|Que retorne o esperado|

**Divirta-se! 🦊**


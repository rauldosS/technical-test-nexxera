![Thumbnail GitHub](https://user-images.githubusercontent.com/8989346/123303345-171fc980-d4f4-11eb-84ae-cb0e49bfb126.png)

# Technical Test Nexxera Group

Teste Técnico - Grupo de Programadores Python Nexxera

## 📍 Prepare-se para usar a API

Nossa API de transações de contas digitais permite que você trabalhe diretamente com recursos de dados 
relacionados às atividades bancárias do seu aplicativo. A API de contas digitais usa protocolos padrão `HTTP` em que as cargas úteis JSON serão retornadas em resposta às solicitações `HTTP`. É implementado internamente com base nos princípios `RESTful`.

## 🛠️ Abrir e rodar o projeto

**Instruções necessárias para abrir e executar o projeto**

- Clone esse repositório
- Crie um virtualenv com Python 3
- Ative o virtualenv
- Instale as dependências
- Rode as migrações

1. Clone o repositório e entre na pasta:
```shell
git clone https://github.com/rauldosS/technical-test-nexxera.git
cd technical-test-nexxera
```

2. Crie um ambiente virtual:
> Linux
```shell
python -m venv <virtual env path>
```

> Windows
```shell
python -m venv env
```

3. Ative o ambiente virtual que você acabou de criar:
> Linux
```shell
python -m venv <virtual env path>
```

> Windows
```shell
.\env\Scripts\activate
```

4. Instale os pacotes de desenvolvimento local:
```shell
pip install -r requirements.txt
```

5. Execute as migrações:
```shell
python manage.py migrate
```

Rode o servidor de desenvolvimento:
```shell
python manage.py runserver
```

### 📍 Execução no ambiente Windows
![alt text](https://github.com/rauldosS/rest-api-django/blob/main/images/0.png?raw=true)

### 📍 Informação de recursos

| Informação | Descrição |
| ------------------- | ------------------- |
| Formato de resposta | JSON |
| Formato de envio | JSON |
| Requer autenticação | Não |
| Taxa limitada | Não |

### 📍 URL base (API Overview)

O URL base usado para a API é formatado conforme mostrado abaixo:

```shell
http://127.0.0.1:8000/api/
```

Ao acessar a URL base uma página chamada Api Overview contendo as configurações e lista de requisições aceitas será apresentadas.

## ⚙️ Parâmetros

| Nome | Requerido | Descrição |
| ------------------- | ------------------- | ------------------- |
| function | opcional | Filtro para extrato das transações pela função Crédito ou Débito |
| account | opcional | Filtro para extrato das transações pelo identificador numérico da Conta virtual |

## 📍 Cabeçalhos

Uma HTTP típica para a API inclui os seguintes cabeçalhos:

```shell
Content-Type: application/json; charset=utf8
```

- <b>Content-Type</b>: cada solicitação deve incluir um `Content-Type` cabeçalho.

```shell
Content-Type: application/json; charset=utf8
```

## 🔨 Consumo da API

### Todas as transações
```shell
/api/transaction-list
```

> Utilize o parâmetro `account` com o valor do `identificador da conta` para consultar o extrato de uma conta específica:
```shell
/api/transaction-list/?account=2
```

> Utilize o parâmetro `function` com o valor do `tipo de transação` para consultar o extrato do tipo Crédito ou Débito:
    > Tipos disponíveis `C` e `D` sendo respectivamente identificadores de Crédito e Débito.

```shell
/api/transaction-list/?function=D
```

> Utilize os parâmetros `account` e `function` separados por `&` para realizar os filtros a cima juntos:
```shell
/api/transaction-list/?account=1&function=D
```
```shell
/api/transaction-list/?account=1&function=D
```

### Detalhes da Transação
> URL base

```shell
/api/transaction-detail
```

> v.g. detalhes da transação 1
```shell
/api/transaction-detail/1
```

### Criar transação
```shell
/api/transaction-create
```

- No corpo da requisição adicione o JSON com os dados da transação a ser criada:

```json
{
    "account": 1,
    "description": "Books",
    "value": 505,
    "function": "C"
}
```

### Atualizar transação

> URL base

```shell
/api/transaction-update
```

> v.g. atualizando transação 5

```shell
/api/transaction-update/5
```

- No corpo da requisição adicione o JSON com os dados da transação a ser atualizada:

```json
{
    "account": 1,
    "description": "Books",
    "value": 505,
    "function": "C"
}
```

## Consumo através do Insomnia REST
## Consumo através do Django Rest framework

## ✔️ Técnicas e tecnologias utilizadas

**Faça uma lista de tecnologias e técnicas utilizadas (a justificativa e descrição são opcionais)**:

- `Linguagem de programação`: Python
- `Frameworks`: Django
    - `Django REST framework`: é um kit de ferramentas poderoso e flexível para a construção de APIs da Web.
        - `Function Based Views`: Visualizações regulares baseadas em funções.

## 📚 Mais informações
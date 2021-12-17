![Thumbnail GitHub](https://user-images.githubusercontent.com/8989346/123303345-171fc980-d4f4-11eb-84ae-cb0e49bfb126.png)

# Technical Test Nexxera Group

Teste Técnico - Grupo de Programadores Python Nexxera

## 🔗 Prepare-se para usar a API

Nossa API de transações de contas digitais permite que você trabalhe diretamente com recursos de dados 
relacionados às atividades bancárias do seu aplicativo NIX. A API de contas digitais usa `HTTP` protocolos padrão em que as JSON cargas úteis serão retornadas em resposta às `HTTP` solicitações. É implementado internamente com base nos princípios `RESTful`.

## informação de recursos

| Informação | Descrição |
| ------------------- | ------------------- |
| Formato de resposta | JSON |
| Requer autenticação | Não |
| Taxa limitada | Não |


## Parâmetros

| Nome | Requerido | Descrição |
| ------------------- | ------------------- | ------------------- |
| function | opcional | Filtro para extrato das transações pela função Crédito ou Débito |
| account | opcional | Filtro para extrato das transações pelo identificador numérico da Conta virtual |

### URL base

O URL base usado para a API é formatado conforme mostrado abaixo:

```bash
http://127.0.0.1:8000/api/
```

Ao acessar a URL base será exibido uma página chamada Api Overview contendo as configurações e lista de requisições aceitas.

### Exemplos de aplicação dos parâmetros

- Consultando transações por função específica

> Transações função Débito (function=D)
```bash
http://127.0.0.1:8000/api/transactions/<b>?function=D</b>
```
> Transações função Crédito (function=C)
```bash
http://127.0.0.1:8000/api/transactions/?function=C
```

> Transações conta específico (account=1)
```bash
http://127.0.0.1:8000/api/transactions/?account=1
```

> Transações conta específico & função Débito (account=1, function=D)
```bash
http://127.0.0.1:8000/api/transactions/?account=1&function=D
```

## Cabeçalhos

Uma HTTP típica para a API inclui os seguintes cabeçalhos:

```bash
Content-Type: application/json; charset=utf8
```

- <b>Content-Type</b>: cada solicitação deve incluir um `Content-Type` cabeçalho.

## 🔨 Funcionalidades do projeto

## ✔️ Técnicas e tecnologias utilizadas

**Faça uma lista de tecnologias e técnicas utilizadas (a justificativa e descrição são opcionais)**:

- `Funcionalidade 1`: descrição da funcionalidade 1
- `Funcionalidade 2`: descrição da funcionalidade 2
    - `Funcionalidade 2a`: descrição da funcionalidade 2a relacionada à funcionalidade 2
- `Funcionalidade 3`: descrição da funcionalidade 3

## 🛠️ Abrir e rodar o projeto

**Apresente as instruções necessárias para abrir e executar o projeto**

## 📚 Mais informações do curso
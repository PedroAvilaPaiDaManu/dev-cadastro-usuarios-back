Descrição do Projeto:
O projeto é uma API RESTful desenvolvida em Python usando o framework FastAPI e o banco de dados Microsoft SQL Server. A API permite realizar operações CRUD (Create, Read, Update, Delete) em uma tabela de usuários, armazenando informações como email, nome, sobrenome, telefone, UF, CEP, cidade e idade.

Requisitos:

Python 3.7 ou superior
Microsoft SQL Server (ou SQL Server Express) instalado e configurado
ODBC driver para SQL Server (se estiver usando um sistema operacional Windows)

Configure a conexão com o banco de dados:

Abra o arquivo "postgres_conn.py" na pasta raiz do projeto.
Edite as variáveis "server", "database", "username" e "password" para refletir as informações de conexão com o seu banco de dados SQL Server.
Inicie o servidor FastAPI:

uvicorn main:app --host 0.0.0.0 --port 8000

A API estará disponível em http://localhost:8000/.
Endpoints:

Criar Usuário:

Método: POST
URL: http://localhost:8000/users/
Payload:

```
{
    "email": "exemplo@email.com",
    "name": "Nome",
    "last_name": "Sobrenome",
    "phone": "1234567890",
    "uf": "AM",
    "cep": "69000-000",
    "city": "Manaus",
    "age": 25
}

```

![image](https://github.com/PedroAvilaPaiDaManu/dev-cadastro-usuarios-back/assets/121688647/b8da0eb9-3298-4a17-ac1a-f30f35b57372)


Descrição: Cria um novo usuário com as informações fornecidas no payload. Retorna uma resposta JSON indicando se o cadastro foi realizado com sucesso ou não.


Listar Usuários:

Método: GET
URL: http://localhost:8000/users/
Descrição: Retorna uma lista de todos os usuários cadastrados no banco de dados. Se não houver usuários cadastrados, retorna uma resposta JSON indicando que nenhum usuário foi encontrado.


Atualizar Usuário:

Método: PUT
URL: http://localhost:8000/users_edit/
Headers: O email do usuário a ser atualizado deve ser fornecido no header "email".
Payload (apenas os campos que serão atualizados):

```
{
    "email": "exemplo@email.com",
    "name": "Nome",
    "last_name": "Sobrenome",
    "phone": "1234567890",
    "uf": "AM",
    "cep": "69000-000",
    "city": "Manaus",
    "age": 25
}
```

Descrição: Atualiza as informações do usuário com o email fornecido no header "email". Retorna uma resposta JSON indicando se a atualização foi realizada com sucesso ou não.

Observações:

A API realiza validações para garantir que o cadastro seja autorizado apenas para o estado do Amazonas (UF: AM) e para maiores de 18 anos.
Certifique-se de que as configurações do banco de dados (server, database, username, password) estejam corretas no arquivo "postgres_conn.py".
O arquivo "requirements.txt" contém todas as dependências necessárias para executar a aplicação. Certifique-se de que as dependências foram instaladas corretamente usando o comando "pip install -r requirements.txt".
Para a execução em um ambiente Windows, é necessário garantir que o ODBC driver para SQL Server esteja instalado e configurado corretamente. Caso contrário, a conexão com o banco de dados pode falhar.
O código do projeto está organizado em três arquivos principais: "main.py" para as rotas e lógica da aplicação, "postgres_conn.py" para a conexão com o banco de dados, e "models.py" para a definição do modelo de dados do usuário.
Certifique-se de executar o comando "uvicorn" usando o parâmetro "--host 0.0.0.0" para que a API seja acessível a partir de outros dispositivos na rede local (se necessário). Caso contrário, a API estará disponível apenas em localhost.
Lembre-se de que a API precisa ser executada juntamente com um banco de dados SQL Server configurado corretamente para armazenar as informações dos usuários.

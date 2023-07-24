import pyodbc
from fastapi import HTTPException
import aiohttp
import pandas as pd
import json


def get_connect():
    server = 'localhost\SQLEXPRESS'
    database = 'db-pedro'
    username = 'pedro_avila'
    password = '123'

    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    try:

        connection = pyodbc.connect(connection_string)
        print("Conexão bem-sucedida!")

        return connection

    except Exception as e:
        print(f"Erro ao conectar ao SQL Server: {e}")
        return None


def insert_lines(data):
    conn = get_connect()
    cursor = conn.cursor()
    email = data['email']
    name = data['name']
    last_name = data['last_name']
    phone = data['phone']
    cep = data['cep']
    uf = data['uf']
    city = data['city']
    age = data['age']

    if age > 18:
        query = f"""INSERT INTO [db-pedro].dbo.users (email, name, last_name, city, phone,cep, uf, age) VALUES ('{email}', '{name}', '{last_name}', '{city}', '{phone}' ,'{cep}', '{uf}','{age}')"""
        cursor.execute(query)
        conn.commit()
        conn.close()
        return "Cadastro realizado com sucesso"
    else:

        return False


async def get_cep_data(cep: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://viacep.com.br/ws/{cep}/json/') as response:
            if response.status == 200:
                cep_data = await response.json()
                uf = cep_data.get('uf')
                return uf, cep_data

            raise HTTPException(status_code=response.status,
                                detail="CEP não encontrado.")


def get_header():
    h = {
        "Content-Type": "application/json"}
    return h


def atualizar(data):
    query = 'UPDATE [db-pedro].dbo.users SET '
    conn = get_connect()
    cursor = conn.cursor()
    email = data.get('email')
    for key, value in data.items():
        if key == 'age':
            query = query + f"{key}= {value},"

        else:
            query = query + f"{key}='{value}', "

    query = query[:len(query) - 2]
    query = query + f" WHERE email = '{email}'"

    cursor.execute(query)
    conn.commit()
    conn.close()


def list_users():
    conn = get_connect()
    query = f"SELECT * FROM [db-pedro].dbo.users"
    df = pd.read_sql_query(query, con=conn)
    conn.close()

    if len(df) == 0:
        return False
    retorno = df.to_json(orient='records')
    retorno = json.loads(retorno)
    return retorno

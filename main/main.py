from fastapi import FastAPI, HTTPException, Request, Header
from postgres_conn import get_cep_data, insert_lines, list_users, atualizar
from fastapi.responses import JSONResponse
from models import User


app = FastAPI()


@app.post("/users/", response_model=User)
async def create_user(user: User):

    try:
        uf = await get_cep_data(user.cep)

        print(uf)

        if uf[0] != 'AM':
            response = {
                "FL_STATUS": False,
                "error": "Cadastro autorizado somente para o estado do Amazonas (AM)"
            }
            return JSONResponse(content=response, status_code=200)
        if user.age < 18:
            response = {
                "FL_STATUS": False,
                "error": "Cadastro autorizado somente para Maiores de 18 anos"
            }
            return JSONResponse(content=response, status_code=200)

        success = insert_lines(user.dict())
        if not success:
            response = {
                "FL_STATUS": False,
                "error": "Erro ao cadastrar"
            }
            return JSONResponse(content=response, status_code=200)
        response = {
            "FL_STATUS": True,
            "mensagem": "Cadastro realizado com sucesso"
        }
        return JSONResponse(content=response, status_code=200)

    except Exception as ex:
        response = {
            "FL_STATUS": False,
            "error": str(ex)
        }
    return JSONResponse(content=response, status_code=400)


@app.get("/users/")
def get_users():
    try:
        users = list_users()
        if not users:
            raise HTTPException(
                status_code=404, detail="Nenhum usuário encontrado.")
        return users

    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))


@app.put("/users_edit/", response_model=User)
async def edit_user(user: User, request: Request, email: str = Header(None)):
    data = await request.json()
    uf = await get_cep_data(user.cep)

    if uf[0] != 'AM':
        response = {
            "FL_STATUS": False,
            "error": "Cadastro autorizado somente para o estado do Amazonas (AM)"
        }
        return JSONResponse(content=response, status_code=200)
    if user.age < 18:
        response = {
            "FL_STATUS": False,
            "error": "Cadastro autorizado somente para Maiores de 18 anos"
        }
        return JSONResponse(content=response, status_code=200)

    try:
        atualizar(data)
        retorno = {"FL_STATUS": True}
        return JSONResponse(retorno, status_code=200)
    except Exception as ex:
        response = {"FL_STATUS": False,
                    "error": str(ex.args[0])
                    }
        return JSONResponse(response, status_code=400)

from http import HTTPStatus

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.categoria import router as categoria_router
from backend.routes.produto import router as produto_router
from backend.routes.promocao import router as promocao_router

app = FastAPI(title='Apollo Solutions')

app.include_router(produto_router)
app.include_router(promocao_router)
app.include_router(categoria_router)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Olá mundo'}

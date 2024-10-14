<a id="readme-top"></a>
# Apollo Solutions

<div align="center">
  <p align="center">
    Projeto feito para o processo seletivo da empresa Apollo Solutions
</div>



<details>
  <summary>Conteúdo</summary>
  <ol>
    <li>
      <a>Sobre o projeto</a>
      <ul>
        <li><a>Tecnologias utilizadas</a></li>
      </ul>
    </li>
    <li>
      <a>Executando o projeto</a>
      <ul>
        <li><a>Pré-requisitos</a></li>
        <li><a>Executando</a></li>
      </ul>
    </li>
  </ol>
</details>



### Tecnologias utilizadas

* <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg" width="50" height="50" alt="Javascript"/>
* <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/npm/npm-original-wordmark.svg" width="50" height="50" alt="npm"/>        
* <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/react/react-original-wordmark.svg" width="50" height="50" alt="React"/>
* <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" width="50" height="50" alt="Python"/>
* <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original-wordmark.svg" width="50" height="50" alt="Pytest"/>
* <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original-wordmark.svg" width="60" height="60" alt="FastAPI"/>
* <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/poetry/poetry-original.svg" width="50" height="50" alt="Poetry"/>
* <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original-wordmark.svg" width="50" height="50" alt="PostgreSQL"/>
* <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlalchemy/sqlalchemy-original-wordmark.svg" width="50" height="50" alt="SQLAlchemy"/>
* <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original-wordmark.svg" width="50" height="50" alt="Docker"/>
          

<p align="right">(<a href="#readme-top">topo</a>)</p>



## Executando o projeto

Como executar o projeto localmente

### Pré-requisitos

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)

### Executando

1. Clone o repositório
   ```sh
   git clone https://github.com/mugubr/apollo-solutions.git
   ```
2. No diretório ```/backend```, crie um arquivo ```.env``` com as seguintes variáveis de ambiente
   ```sh
    DATABASE_URL="postgresql+psycopg://app_user:app_password@localhost:5432/app_db"
    SECRET_KEY = 'chave'
    ALGORITHM = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
   ```

3. Execute o arquivo ```docker-compose.yaml```, localizado na raiz do projeto
   ```sh
   docker-compose up --build
   ```
4. Após os containers estarem rodando, acesse a documentação da API  em ```https://localhost:8000/docs``` ou ```https://localhost:8000/redoc```
   

5. As telas estarão disponíveis em ```https://localhost:3000/``` (Lista de Produtos) e ```https://localhost:3000/novo``` (Adicionar Produto)


<p align="right">(<a href="#readme-top">topo</a>)</p>


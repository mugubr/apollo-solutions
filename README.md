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
4. Após os containers estarem ativos, acesse a documentação da API  em ```https://localhost:8000/docs``` ou ```https://localhost:8000/redoc```
   

5. As telas estarão disponíveis em ```https://localhost:3000/``` (Lista de Produtos) e ```https://localhost:3000/novo``` (Adicionar Produto)


<p align="right">(<a href="#readme-top">topo</a>)</p>


## Respostas
**1. Quais seriam as suas primeiras melhorias caso possuísse mais tempo de implementação?**

  Acredito que a primeira melhoria seria a adição das telas referentes à atualização de produtos, listagem de categorias (com a funcionalidade de exclusão das mesmas), cadastro/atualização de categorias e a tela referente às promoções (com funcionalidades de cadastro, atualização e exclusão das mesmas), pois várias dessas funcionalidades já se encontram implementadas, a nível de backend.
  Adicionar testes unitários e de integração no backend e frontend, garantindo a estabilidade da aplicação ao longo do tempo, também seria uma prioridade.

**2. Pensando na sua solução, como seria a manutenção em caso da adição de novas
categorias de produtos? O que precisaria ser alterado?**

  A única alteração necessária seria a implementação de uma tela para o cadastro dessas novas categorias, pois a funcionalidade já existe, a nível de backend.

**3. Caso fosse necessário, quais alterações precisariam ser feitas para suportar atualizações na
porcentagem de desconto da categoria de produto, de modo que, sempre que a porcentagem
de desconto fosse alterada, o novo preço fosse refletido em todos os produtos da mesma?**

   Os preços promocionais já são atualizados dinamicamente, dependendo do valor de porcentagem de desconto por categoria de produto, então a única necessidade seria a implementação de uma tela referente às promoções (com funcionalidades de cadastro, atualização e exclusão das mesmas).


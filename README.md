# 📦 REST API com Flask

Este repositório contém uma API RESTful desenvolvida com **Python** e **Flask**, seguindo boas práticas de organização de código, com foco em operações **CRUD** (Create, Read, Update, Delete). É ideal para servir como backend de aplicações web ou mobile.

## 🚀 Funcionalidades

- ✅ Endpoints RESTful com Flask  
- 📄 Estrutura modular (models, schemas, resources)  
- 🔄 Operações CRUD completas  
- 🧪 Validação de dados com Marshmallow  
- 🗃️ Persistência com SQLAlchemy (banco relacional)  
- 🛠️ Pronta para extensão e integração com frontend  

## 🧱 Tecnologias utilizadas

- [Python 3](https://www.python.org/)  
- [Flask](https://flask.palletsprojects.com/)  
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)  
- [SQLAlchemy](https://www.sqlalchemy.org/)  
- [Marshmallow](https://marshmallow.readthedocs.io/)  

## 📁 Estrutura do projeto

```
restapi_flask/
├── app.py             # Arquivo principal da aplicação
├── models.py          # Modelos do banco de dados
├── schemas.py         # Schemas para validação dos dados
├── resources/         # Endpoints da API organizados por recurso
├── config.py          # Configurações do app
├── requirements.txt   # Dependências do projeto
```

## 🧪 Como rodar o projeto localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/KledsonV/restapi_flask.git
   cd restapi_flask
   ```

2. Crie um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplicação:
   ```bash
   flask run
   ```

5. Acesse no navegador ou via Postman:
   ```
   http://localhost:5000/
   ```

## 🤝 Como contribuir

1. Faça um fork do projeto  
2. Crie uma branch:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça as alterações desejadas  
4. Faça commit:
   ```bash
   git commit -m "feat: nova funcionalidade"
   ```
5. Envie para o seu fork:
   ```bash
   git push origin minha-feature
   ```
6. Abra um Pull Request 🧃

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 💡 Autor

Desenvolvido por [Kledson Vinicius](https://github.com/KledsonV)

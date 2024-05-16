## Microservice architecture web app for education and testing

Small web-app for education and test purposes. 
Perfomed as microservice architecture app, therefore ***Very simple** to readjust under your own needs.*

You can run, test and wide this app for your purposes.

- Switch to developer branch.
- adjust your .env files (investigate docker-compose.yml for paths)
- Run **make up**
- Run **make filldb**
- test on "https://localhost"
- Run **make down**

in containers:
- db: postgres + alembic for migrations + adminer(server: educ_postgres_service:5432)
- db_service: async FastAPI + SQLModel
- nginx_service: ngnix as proxy, pure html+css+js as frontend over https


### ALEMBIC:

if you want to initialize and adjust alembic by yourself, do:
- **docker-compose exec educ_db_service alembic init -t async migrations**
- then follow instructions in *https://testdriven.io/blog/fastapi-sqlmodel/*

Now in repo the async alembic version is fully adjusted and ready to use.
if you want to change your tables:
- readjust your models (models.py)
- readjust your data (db_data.py)
- in main *Makefile* change the number of revision
- launch ***make migratedb*** then ***make filldb*** (**while app is running!**)


After the migration you may want to fill app by automatically generated data. 
for that purpose fill lists in db_data.py, then adjust init_db in database.py, and finally run:
- **docker-compose exec educ_db_service python3 filling_data.py**

### HTTPS
Now there are self-made SSL-certificates and apporpriate nginx-configuration. Due to this, the connection *https://localhost* will be insecure. Just go into advanced and follow the site.
If you want to deploy app in production, change them with CA-certificates and readjust your nginx.conf.


### REACT
There is React frame implemented.
To start development using React **by yourself** follow theese steps:
1) Create folder for your service.
2) Create **Dockerfile** inside this folder with content of **react_service/Dockerfile**
3) Launch ***docker run -it --rm -v "$PWD":/app:rw react_builder npx create-react-app my-react-app***
4) In appeared folder **my-react-app** create another **Dockerfile** with content of **my-react-app/Dockerfile**
5) Launch ***docker build -t react_app_dev --target dev .***
5) Launch ***docker run --rm -it -p 3000:3000 -v $PWD:/app react_app_dev***
6) Now you can access your react app from browser on **localhost:3000**
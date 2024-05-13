In progress.

You can run, test and wide this app for your purposes.

- Switch to developer branch.
- adjust your .env files (investigate docker-compose.yml for paths)
- Run "docker-compose up"
- test on "localhost:8080"

in containers:
- db: postgres + alembic for migrations + adminer(server: educ_postgres_service:5432)
- db_service: async FastAPI + SQLModel
- nginx_service: ngnix as proxy, pure html+css+js as frontend


ALEMBIC:
to initialize alembic, do:
- **docker-compose exec educ_db_service alembic init -t async migrations**
- then follow instructions in *https://testdriven.io/blog/fastapi-sqlmodel/*

if you want to change your tables, then when your app is running, in *docker-compose* directory:
- **docker-compose exec educ_db_service alembic revision --autogenerate -m "revision_number"**
- **docker-compose exec educ_db_service alembic upgrade head**

After the migration you may want to fill app by automatically generated data. 
for that purpose fill lists in db_data.py, then adjust init_db in database.py, and finally run:
- **docker-compose exec educ_db_service python3 filling_data.py**
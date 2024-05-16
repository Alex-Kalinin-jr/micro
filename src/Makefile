REVISIONNUMBER=five

all: up

fill: migratedb filldb

clearall: clearnginx cleardb clearpostgres clearreact


clearnginx:
	-docker stop nginx_service
	-docker rm nginx_service
	-docker rmi src_educ_nginx_service

cleardb:
	-docker stop educ_db_service
	-docker rm educ_db_service
	-docker rmi src_educ_db_service

clearpostgres:
	-docker stop educ_postgres_service
	-docker rm educ_postgres_service
	-docker rmi educ_postgres_service

clearreact:
	-docker stop src_react_service
	-docker rm educ_react_service
	-docker rmi educ_react_service

migratedb:
	-docker-compose exec educ_db_service alembic upgrade head
	-docker-compose exec educ_db_service alembic revision \
	--autogenerate -m "revision_number_$(REVISIONNUMBER)"

filldb:
	-docker-compose exec educ_db_service alembic upgrade head
	-docker-compose exec educ_db_service python3 filling_data.py

up:
	-docker-compose up

down:
	-docker-compose down


	


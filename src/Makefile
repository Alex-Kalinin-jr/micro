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
	-docker rmi src_react_service

migratedb:
	-docker-compose exec educ_db_service alembic upgrade head
	-docker-compose exec educ_db_service alembic revision \
	--autogenerate -m "revision_number_$(REVISIONNUMBER)"

filldb:
	-docker-compose exec educ_db_service alembic upgrade head
	-docker-compose exec educ_db_service python3 filling_data.py

up:
	-docker-compose up

upfirsttime:
	docker build --build-arg USER_UID=$(id -u) --build-arg USER_GID=$(id -g) -t react_builder ./react_service
	docker run --rm -v $(PWD)/react_service:/app:rw react_builder
	docker-compose up


down:
	-docker-compose down





all: clearnginx cleardb clearpostgres

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

filldb:
	-docker-compose exec educ_db_service alembic upgrade head
	-docker-compose exec educ_db_service python3 filling_data.py

# micro

In progress. Switch to **develop** branch for actual version

You can run, test and wide this app for your purposes.

- Switch to developer branch.
- adjust your .env files (investigate docker-compose.yml for paths)
- Run "docker-compose up"
- test on "localhost:8080"

in containers:
- db: postgres + adminer(server: educ_postgres_service:5432)
- db_service: async FastAPI + SQLModel
- nginx_service: ngnix as proxy, pure html+css+js as frontend

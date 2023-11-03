export DOCKER_DEFAULT_PLATFORM=linux/amd64


start:
	docker compose -f docker-compose.yaml up -d
	sleep 2
	docker exec app sh -c "alembic revision --autogenerate -m 'database_init' && alembic upgrade head"
up:
	docker compose -f docker-compose.yaml up -d
	docker exec app sh -c "alembic upgrade head"
down:
	docker compose -f docker-compose.yaml down --remove-orphans
stop:
	docker compose -f docker-compose.yaml stop
migrate:
	docker exec app sh -c "alembic revision --autogenerate -m 'database_init' && alembic upgrade head"
clear pw:
	docker exec app sh -c "rm -R passwords && mkdir passwords"
test:
	docker exec app sh -c "pytest -s -v tests/*"
help:
	@echo "help  -- print this help"
	@echo "start -- start docker stack"
	@echo "stop  -- stop docker stack"
	@echo "ps    -- show status"
	@echo "build  -- build image"
	@echo "clean -- clean all artifacts"
	@echo "test  -- run tests using docker"
	@echo "dockershell -- run bash inside docker"
	@echo "shell_plus -- run django shell_plus inside docker"
	@echo "bootstrap --build containers, run django migrations, load fixtures and create the a superuser"

build:
	docker-compose build --no-cache web

start:
	docker-compose up -d

up:
	docker-compose up web

psql:
	docker-compose exec postgres psql -U postgres

load-dump:
	docker-compose exec postgres sh psql -U postgres < /docker-entrypoint-initdb.d/dump.sql

stop:
	docker-compose stop

ps:
	docker-compose ps

clean: stop
	docker-compose rm --force -v

only_test:
	docker-compose run --rm web pytest

pep8:
	docker-compose run --rm web flake8

test: pep8 only_test

dockershell:
	docker-compose run --rm web sh

migrations:
	docker-compose run --rm web python3 manage.py makemigrations

migrate:
	docker-compose run --rm web python3 manage.py migrate

shell_plus:
	docker-compose run --rm web python3 manage.py shell_plus

.PHONY: help start stop ps clean test dockershell shell_plus only_test pep8

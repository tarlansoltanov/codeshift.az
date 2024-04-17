compose-dev = docker-compose.yml
compose-prod = docker/docker-compose.prod.yml

service :=
language := en

.PHONY: run

run-dev:
	@echo "Runinng Development"
	docker compose -f $(compose-dev) up -d

run:
	@echo "Runinng Production"
	docker compose -f $(compose-dev) -f $(compose-prod) up -d

logs:
	@echo "Logs"
	docker compose -f $(compose-dev) -f $(compose-prod) logs $(service) -f

restart:
	@echo "Restarting Service"
	docker compose -f $(compose-dev) -f $(compose-prod) restart $(service)

stop:
	@echo "Stopping Service"
	docker compose -f $(compose-dev) -f $(compose-prod) stop $(service)

clean:
	@echo "Cleaning Service"
	docker compose -f $(compose-dev) -f $(compose-prod) down $(service)

clean-all:
	@echo "Cleaning Service All"
	docker compose -f $(compose-dev) -f $(compose-prod) down -v $(service)

shell:
	@echo "Service Shell"
	docker compose -f $(compose-dev) -f $(compose-prod) exec $(service) /bin/bash

migrate:
	@echo "Django Migrate"
	docker compose -f $(compose-dev) -f $(compose-prod) exec web python manage.py migrate

makemigrations:
	@echo "Django Make Migrations"
	docker compose -f $(compose-dev) -f $(compose-prod) exec web python manage.py makemigrations

createsuperuser:
	@echo "Django Create Super User"
	docker compose -f $(compose-dev) -f $(compose-prod) exec web python manage.py createsuperuser

collectstatic:
	@echo "Django Collect Static Files"
	docker compose -f $(compose-dev) -f $(compose-prod) exec web python manage.py collectstatic --no-input

makemessages:
	@echo "Django Makemessage files"
	docker compose exec web python manage.py makemessages -l $(language)

compilemessages:
	@echo "Django Compile Message files"
	docker compose exec web python manage.py compilemessages --ignore django

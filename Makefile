#!/bin/bash

APP = GameErauntsia
VERSION := $(shell cat ./VERSION)
DOCKER_REPO_NGINX = gamerauntsia/${APP}_nginx:${VERSION}
DOCKER_REPO_APP = gamerauntsias/${APP}_app:${VERSION}
USER_ID = $(shell id -u)
GROUP_ID= $(shell id -g)
user==www-data

help: ## laguntza hau
	@echo
	@echo 'erabiltzeko: make [aginduaren izena]'
	@echo
	@echo 'aginduak'
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[$$()% a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)	
	@echo
	@echo

build: ## Docker irudia sortu
	DOCKER_BUILDKIT=1 docker compose --env-file .env build

build-force: ## forcker irudia sortu systema garbitik
	DOCKER_BUILDKIT=1 docker compose --env-file .env build --force-rm --no-cache

restart: ## Kontenedoreak geratu eta martxan ipini
	$(MAKE) stop && $(MAKE) run

run: ## Kontenedoreak abiatu
	docker compose -f docker-compose.yml -f docker-compose.override.yml up -d

stop: ## Kontenedoreak gelditu
	docker compose down

ssh: ## Kontenedorean sartu
	docker compose exec web sh

superuser:
	docker compose exec web python3 manage.py createsuperuser
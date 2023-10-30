### Defensive settings for make:
#     https://tech.davis-hansson.com/p/make/
SHELL:=bash
.ONESHELL:
.SHELLFLAGS:=-xeu -o pipefail -O inherit_errexit -c
.SILENT:
.DELETE_ON_ERROR:
MAKEFLAGS+=--warn-undefined-variables
MAKEFLAGS+=--no-builtin-rules

CURRENT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

PROJECT_NAME=ploneconf2023
STACK_NAME=ploneconf2023-peiomena-tangrama-com-br

# We like colors
# From: https://coderwall.com/p/izxssa/colored-makefile-for-golang-projects
RED=`tput setaf 1`
GREEN=`tput setaf 2`
RESET=`tput sgr0`
YELLOW=`tput setaf 3`

help: ## This help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: docker-develop-build
docker-develop-build:  ## Build all develop images without using cache
	@docker-compose --profile develop build --no-cache

.PHONY: docker-develop-up
docker-develop-up:  ## Run all develop images (detached mode)
	@docker-compose --profile develop up -d

.PHONY: docker-develop-down
docker-develop-down:  ## Stop and delete all develop images
	@docker-compose --profile develop down

.PHONY: docker-production-build
docker-production-build:  ## Build all production images without using cache
	@docker-compose --profile production build --no-cache

.PHONY: docker-production-up
docker-production-up:  ## Run all production images (detached mode)
	@docker-compose --profile production up -d

.PHONY: docker-production-down
docker-production-down:  ## Stop and delete all production images
	@docker-compose --profile production down

.PHONY: start-project
django-start-project:  ## Create new django project
	@cd src/
	@django-admin startproject gamerauntsia
	@echo "Django project created"
	@cp $(PWD)/utils/settings.py $(PWD)/src/gamerauntsia/gamerauntsia/
	@echo "Django project settings updated"

.PHONY: django-start-app
django-start-app:   ## Create new django app, app name must be specified (make django-start-app appname=<your_app_name>)
	@echo "Start django app"
	@docker-compose --profile develop up -d
	@docker exec -d gamerauntsia_web_dev python ./app/bin/manage.py startapp $(appname)
	@echo "Django app created"

.PHONY: docker-logs
docker-logs:   ## Visualize docker-compose services logs
	@docker-compose logs

.PHONY: init-volume-dir
init-volume-dir:   ## Initializer volume directories for docker
	@mkdir data
	@mkdir data/certbot
	@mkdir data/certbot/www
	@mkdir data/certbot/conf
	@mkdir data/db
	@mkdir data/mediafiles
	@mkdir data/staticfiles
.PHONY: all help start stop build test bash clean logs artifacts
.DEFAULT_GOAL := start

ifeq ($(ENV),)
	ENV:=local
endif
COMPOSE=docker-compose -f docker-compose.$(ENV).yml

# target: all - Default target. Does nothing.
all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

# target: help - Display callable targets.
help:
	@egrep "^# target:" [Mm]akefile

# target: start - Starts dev server with db, api and frontend
start:
	$(COMPOSE) start

# target: stop - Stop and remove containers, volumes and networks
stop:
	$(COMPOSE) stop

# target: build - Builds docker images
build: artifacts
	$(COMPOSE) up --no-start --build app

# target: test - Runs tests
test:
	$(COMPOSE) run --rm app python manage.py validate_templates
	$(COMPOSE) run --rm app python manage.py test --noinput -v 2 --exclude-tag=integration

# target: test-integration - Runs integrations tests
test-integration:
	$(COMPOSE) run --rm app python manage.py test --noinput -v 2  --tag=integration

# target: bash - Runs /bin/bash in App container for development
bash:
	$(COMPOSE) exec app /bin/bash

# target: clean - Stops and removes all containers
clean:
	$(COMPOSE) down --volume

# target: logs - Shows logs for db, frontend and app
logs:
	$(COMPOSE) logs --follow

up:
	$(COMPOSE) up -d

# target: create artifacts to image
artifacts:
	chmod +x services/build.sh
	chmod +x services/params.sh
	./services/build.sh

# Default to local environment if not explicitly set
APP_ENV ?= local

# Docker Compose command with correct env file
DC = docker compose --env-file .env.$(APP_ENV)

# make setup
.PHONY: local test clean

# Start app with environment-specific configuration
local:
	# remove containers + volumes
	@ENV=$(APP_ENV) $(DC) down -v

	# clean everything
	@docker system prune -af --volumes

	# rebuild and run app
	@ENV=$(APP_ENV) $(DC) up --build app

# Run test container with environment-specific config
test:
	@ENV=$(APP_ENV) $(DC) down -v
	@docker system prune -af --volumes
	@ENV=$(APP_ENV) $(DC) run --rm app sh -c "pytest -s tests"

# Clean volumes and images
clean:
	@$(DC) down -v
	@docker system prune -af --volumes

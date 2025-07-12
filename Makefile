# Default to local environment if not explicitly set
APP_ENV ?= local

# Docker Compose command with correct env file
DC = docker compose --env-file .env.$(APP_ENV)

# make setup
.PHONY: local test clean

# Start app with environment-specific configuration
local:
	# remove containers + volumes
	@$(DC) down -v

	# clean everything
	@docker system prune -af --volumes

	# rebuild and run app
	@$(DC) up --build app

# Run test container with environment-specific config
test:
	@$(DC) down -v
	@docker system prune -af --volumes
	@$(DC) run --rm app sh -c "pytest -s -p no:cacheprovider tests"

# Clean volumes and images
clean:
	@$(DC) down -v
	@docker system prune -af --volumes

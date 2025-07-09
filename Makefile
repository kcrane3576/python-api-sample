# Declare targets that are not filenames
.PHONY: local test clean

# Run development app
local:
	# swap to dev environment
	@ln -sf .env.local .env

	# remove containers + volumes
	@docker compose down -v

	# clean everything
	@docker system prune -af --volumes

	# rebuild and run app
	@docker compose up --build app

# Run tests
test:
	@ln -sf .env.test .env
	@docker compose down -v
	@docker system prune -af --volumes
	@docker compose run --rm test

# Clean everything
clean:
	@docker compose down -v
	@docker system prune -af --volumes

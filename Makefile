# Declare targets that are not filenames
.PHONY: local test clean

# Run development app
local:
	@ln -sf .env.local .env          	# swap to dev environment
	@docker compose down -v         	# remove containers + volumes
	@docker system prune -af --volumes  # clean everything
	@docker compose up --build app  	# rebuild and run app

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

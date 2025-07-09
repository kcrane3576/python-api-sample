# python-api-sample

## docker
### app
```shell
    docker compose down -v && \
    docker system prune -af && \
    docker compose up --build app
```
### tests
```shell
    docker compose down -v && \
    docker system prune -af && \
    docker compose run --rm test
```

## branching
```shell
    git checkout main && \
    git pull origin main && \
    git checkout -b init && \
    git merge main
```


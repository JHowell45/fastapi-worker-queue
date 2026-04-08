set shell := ["powershell.exe", "-c"]

[private]
default:
    @just --list

# Git

alias gc := git-commit
alias gp := git-push
alias gcp := git-commit-push

# Docker

alias b := build
alias u := up
alias d := down
alias r := restart
alias l := logs
alias cm := create-migration
alias um := upgrade-migration

[group("git")]
git-commit msg:
    git add *
    git commit -m "{{ msg }}"

[group("git")]
git-push:
    git push

[group("git")]
git-commit-push msg:
    git add *
    git commit -m "{{ msg }}"
    git push

[group("docker")]
build:
    docker-compose build

[group("docker")]
up:
    docker-compose up -d

[group("docker")]
down:
    docker-compose down

[group("docker")]
restart:
    docker-compose down
    docker-compose build
    docker-compose up -d

[group("docker")]
logs:
    docker-compose logs -f

[group("db")]
create-migration msg:
    docker-compose exec app alembic revision --autogenerate -m "{{ msg }}"

[group("db")]
upgrade-migration:
    docker-compose exec app alembic upgrade head

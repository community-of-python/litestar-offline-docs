default: install lint check-types test

install:
    poetry install

lint:
    poetry run ruff check .
    poetry run ruff format .

check-types:
    poetry run mypy .

test *args:
    poetry run pytest {{args}}

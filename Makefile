APP = restapi

format:
	@bandit -r . -x '/.venv/','/__tests__'
	@black .
	@flake8 . --exclude .venv
	@pytest -v --disable-warnings

compose:  flake
	@sudo docker build -t flask_app .
	@sudo docker compose up -d
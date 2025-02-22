APP = restapi

flake:
	@flake8 . --exclude .venv
	@pytest -v --disable-warnings

compose:  flake
	@docker build -t flask_app .
	@docker compose up -d
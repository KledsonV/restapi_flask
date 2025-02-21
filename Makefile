APP = restapi

flake:
	@flake8 . --exclude .venv

compose:  #flake ( dependence )
	docker build -t flask_app .
	docker compose up -d
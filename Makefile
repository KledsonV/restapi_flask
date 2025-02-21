APP = restapi

flake:
	@flake8 . --exclude .venv

compose:  #flake ( dependence )
	@docker-compose build
	@docker-compose up
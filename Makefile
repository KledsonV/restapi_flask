APP = restapi

format:
	@bandit -r . -x '/.venv/','/__tests__'
	@black .
	@flake8 . --exclude .venv
	@pytest -v --disable-warnings

compose:  format
	@sudo docker build -t flask_app .
	@sudo docker compose up -d

setup-dev:
	@sudo kind create cluster --config kubernetes/config/config.yaml
	@sudo kubectl apply -f https://kind.sigs.k8s.io/examples/ingress/deploy-ingress-nginx.yaml
	@sudo kubectl wait --namespace ingress-nginx \
		--for=condition=ready pod \
		--selector=app.kubernetes.io/component=controller \
		--timeout=270s
	@sudo helm \
	 upgrade \
	 --install \
	 --set auth.rootPassword="root" \
	 mongodb /kubernetes/charts/mongodb
	@sudo kubectl wait \
		--for=condition=ready pod \
		--selector=app.kubernetes.io/component=mongodb \
		--timeout=270s

teardown-dev:
	@sudo kind delete clusters kind
run:
	FLASK_DEBUG=true \
		./venv/bin/flask run
venv:
	virtualenv -p python3 venv
	./venv/bin/pip install -r requirements.txt

IMAGE_TAG=niveskz/weather

docker-build:
	docker build -t $(IMAGE_TAG) .

docker-run: docker-build
	docker run -it --rm -p 5000:5000 $(IMAGE_TAG)

docker-background: docker-build		
	docker run --restart=unless-stopped -d -p 5000:5000 $(IMAGE_TAG)
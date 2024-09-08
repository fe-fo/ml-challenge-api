fastapi dev api.py

docker build . -t ml-challenge-api:v1.0.0

docker run --rm --network host --name api  ml-challenge-api:v1.0.0

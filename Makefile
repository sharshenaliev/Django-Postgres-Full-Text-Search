build:
	docker compose up -d --build

migrate:
	docker compose exec app python manage.py migrate

loaddata:
	docker compose exec app python manage.py loaddata db.json

createsuperuser:
	docker compose exec app python manage.py createsuperuser

test:
	docker compose exec app pytest -v
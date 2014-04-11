run:
	@echo Starting $(PROJECT_NAME) ...
	python manage.py runserver 0.0.0.0:8000


test:
	python manage.py test accounts

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_dir := $(patsubst %/,%,$(dir $(mkfile_path)))

build:
	docker-compose run server python manage.py migrate
run:
	docker-compose up -d
test:
	docker-compose run server pytest -W ignore api/tests/
update_db:
	docker-compose run server python manage.py populate_db
create_user:
	docker-compose run server python manage.py createsuperuser
clean:
	docker-compose down

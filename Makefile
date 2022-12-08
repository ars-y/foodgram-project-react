MANAGE_PATH='./backend'

define find.functions
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
endef

help: ## вывод доступных команд
	@echo 'The following commands can be used.'
	@echo ''
	$(call find.functions)

setup: ## mkmigrations migrate suser run
setup: mkmigrations migrate suser run

mkmigrations: ## makemigrations
mkmigrations:
	cd $(MANAGE_PATH); python3 manage.py makemigrations

migrate: ## migrate
migrate:
	cd $(MANAGE_PATH); python3 manage.py migrate

suser: ## createsuperuser
suser:
	cd $(MANAGE_PATH); python3 manage.py createsuperuser

run: ## runserver
run:
	cd $(MANAGE_PATH); python3 manage.py runserver

clean: ## очистка кэша
clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$\)" | xargs rm -rf
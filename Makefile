.venv/bin/activate: requirements.txt
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt
	.venv/bin/python manage.py tailwind install

clean:
	rm -rf __pycache__
	rm -rf .venv
	rm -rf theme/__pycache__
	rm -rf theme/static_src/node_modules

run: .venv/bin/activate
	.venv/bin/python manage.py runserver

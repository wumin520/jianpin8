
default: install
install:
	python3 -m venv .virtualenv
	./ve pip install -r requirements.txt
run:
	chmod -R +x bin && bin/run serve --port=5000

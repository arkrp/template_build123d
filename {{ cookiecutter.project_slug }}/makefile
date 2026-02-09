run: venv main.py
	venv/bin/python main.py
venv:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt
clean:
	rm -rf venv
.PHONY: run clean

run: venv main.py
	venv/bin/python main.py
venv:
	python3 -m venv venv
	if [ -f ".offline" ]; then\
		echo "installing venv in offline mode";\
		venv/bin/pip install --no-index -r soft_requirements.txt;\
	else\
		echo "installing venv in online mode";\
		venv/bin/pip install -r requirements.txt;\
	fi
offline:
	touch .offline
	echo "Now in offline mode, --no-index will be given to pip. To change it back type 'make online'."
online:
	rm .offline
clean:
	rm -rf venv
.PHONY: run clean

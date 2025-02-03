install:
	pip install --upgrade pip &&\
		pipi install -r requirements.txt

test:
	#python -m pytest -v test_hello.py

format:
	black *.py 

lint:
	pylint --disable=R,C *.py 

all: install lint test
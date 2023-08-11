srcs = $(addprefix wordward/,__init__.py connect.py generate.py util.py wordlist)
tests = $(wildcard test/*.py)


.coverage: $(srcs) $(tests) pyproject.toml
	poetry run coverage run -m pytest

htmlcov/index.html: .coverage
	poetry run coverage html

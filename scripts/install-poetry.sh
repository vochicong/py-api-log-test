set -ex

curl -SL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && ln -s /opt/poetry/bin/poetry /usr/local/bin/

poetry config virtualenvs.create false

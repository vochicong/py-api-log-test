set -ex

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
cd /usr/local/bin && \
ln -s /opt/poetry/bin/poetry && \
poetry config virtualenvs.create false
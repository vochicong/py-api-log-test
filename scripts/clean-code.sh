set -ex
shopt -s globstar

autoflake --in-place --remove-unused-variables \
    --imports=lib,requests \
    **/*.py
isort --atomic -m 3 .

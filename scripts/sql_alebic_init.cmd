@echo off
PUSHD ..\hw12

alembic init migrations

alembic revision --autogenerate -m "Init"

POPD
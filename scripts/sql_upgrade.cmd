@echo off
PUSHD ..

alembic revision --autogenerate -m "Updates"
alembic upgrade head 

POPD
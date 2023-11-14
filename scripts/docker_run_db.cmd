@echo off

docker run --name pg-hw12 -p 5432:5432 --env-file ../.env -d postgres


                    


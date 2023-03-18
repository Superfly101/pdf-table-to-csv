# Description

Read table from pdf and convert to csv file and store in a postgres database

## Requirements
To run script the following needs to be installed:
- [Java 8+](https://www.java.com/en/download/manual.jsp)
- [Python 3.8+](https://www.python.org/downloads/)
- [Postgres](https://www.postgresql.org/download)

## Install python packages
```bash
pip install -r requirements.txt
```

## Create new user
Connect to postgres server
```bash 
CREATE USER {name} WITH PASSWORD {password};
```


## Create database 
```bash 
CREATE DATABASE {database_name} OWNER {user};
```
Lastly, replace `database` `user` `password` in script with the one created.

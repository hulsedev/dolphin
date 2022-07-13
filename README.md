# Dolphin

Dolphin are [apparently curious animals](https://faunafacts.com/animals/curious-animals/), so are we at Hulse, and we need some fresh data! We'll be collecting data about personal computer activity, and more specifically data about CPU, Disk, Memory, and Energy consumptions.

## Getting Started
Once you're connected to the postgres shell, run the following commands:
```postgresql
CREATE DATABASE "dolphin";
CREATE USER postgres WITH PASSWORD 'postgres';
ALTER ROLE postgres SET client_encoding TO 'utf8';
ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
ALTER ROLE postgres SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE dolphin TO postgres;
```
> Find more info about setting postgresql with django [here](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-20-04).

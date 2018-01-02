#!/bin/sh

# Restart Service
/Applications/Postgres.app/Contents/Versions/latest/bin/pg_ctl stop -D ~/Library/Application\ Support/Postgres/var-9.6
/Applications/Postgres.app/Contents/Versions/latest/bin/pg_ctl start -D ~/Library/Application\ Support/Postgres/var-9.6

# drop database
/Applications/Postgres.app/Contents/Versions/latest/bin/dropdb administration

# create database
/Applications/Postgres.app/Contents/Versions/latest/bin/createdb -O MacBookPro administration

# list databases
/Applications/Postgres.app/Contents/Versions/latest/bin/psql -l

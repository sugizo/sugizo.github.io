#!/bin/sh

# Restart MySQL Service
sudo /Applications/XAMPP/xamppfiles/xampp stopmysql
sudo /Applications/XAMPP/xamppfiles/xampp startmysql

# drop database
/Applications/XAMPP/xamppfiles/bin/mysql -u root --password="" -e "DROP DATABASE IF EXISTS administration;"

# create database
/Applications/XAMPP/xamppfiles/bin/mysql -u root --password="" -e "CREATE DATABASE IF NOT EXISTS administration;"

# show databases
/Applications/XAMPP/xamppfiles/bin/mysql -u root --password="" -e "SHOW DATABASES;"

# show tables
/Applications/XAMPP/xamppfiles/bin/mysql -u root --password="" -e "SHOW TABLES FROM administration;"

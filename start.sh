#!/bin/sh

. /home/site/bin/activate 
/usr/bin/python /home/site/web2py/anyserver.py -s gunicorn -i 0.0.0.0 -p 80

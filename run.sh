#!/bin/bash

echo 'Running server on 127.0.0.1:8000'
source venv/bin/activate
screen -d -m -S oanevsms python3 manage.py runserver
echo 'Run screen -r oanevsms to see logs'
deactivate
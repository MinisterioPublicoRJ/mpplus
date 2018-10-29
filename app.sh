#!/bin/bash
# GUNICORN_CMD_ARGS = variável de configuração do Gunicorn
gunicorn mpplus.wsgi:application --bind=0.0.0.0:8080 --log-file -
#!/bin/bash

# script to start proxy server

set -e

envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
nginx -g 'daemon off;'  # runs server in the foreground


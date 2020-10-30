# ProdServerConfig

## Overview:

This is a script to automatically set up a simple nginx server for your website

## Why would you find that useful?

When you are done developing your flask/django/.. web app in your local machine, you want to deploy it on a production server. You'll need a real web server like nginx, as opposed to your dev server. This script help you setup nginx to work with your wsgi(like gunicorn). You may also find install_ssl.py useful for setting up a ssl certificate for your website, otherwise your website will be shown as insecure in chrome browser.

## Prerequisites

* Install nginx
```
sudo apt-get install nginx
```

* Python 2/3

## Usage

* Setup nginx  
```
python nginx.py [WEB_DOMAIN without www, like google.com] [PROJECT_NAME]
```

Once you execute the above command, you may set up your wsgi to bind with the file /tmp/PROJECT_NAME.sock


* Setup ssl certificate(do this after setup nginx)  
```
python install_ssl.py
```

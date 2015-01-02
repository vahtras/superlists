Provisioning a new site
=======================

## Required packages:

* nginx
* python
* git
* pip
* virtualenv

e.g., on Ubuntu

    sudo apt-get install nginx git python python-pip
    pip install virtualenv

##  Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg. staging.my-domain.com

** Upstart Job

* see gunicorn-supstart.template.conf
* repalce SITENAME with, eg, staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
|-- sites
    |-- SITENAME
        |-- database
        |-- source
        |-- static
        |-- virtualenv
        
            



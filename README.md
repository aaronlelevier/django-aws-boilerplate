# django-aws-boilerplate

Boilerplate project for running a Django app in AWS with:

- [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
- EC2

	- Nginx - reverse-proxy, serves static assets
	- Gunicorn - upstream Python webserver

- RDS in MySQL

## Setup

This project uses Python 3

Use a `virtualenv` and `pip install -r requirements.txt` in the project directory.


## Database

### install mysql package

```
sudo apt install mysql-client-core-5.7
```

Local setup

```
mysql -u root

create user 'user'@'localhost' IDENTIFIED BY 'password';

create database mydb;

grant all privileges on * . * to 'user'@'localhost';

\q
```

## Python webserver

Run locally via [gunicorn](https://gunicorn.org/) with

```
$ gunicorn djangoaws.wsgi
```

## Prod

Ubuntu 16.04 LTS - AWS EC2 quickstart image

### Instance

set Security Group

- Inbound Rules - "My IP"

### Install steps

Install Python and MySQL client required packages

```
sudo apt-get update

sudo apt-get install python3-pip python3-venv nginx libmysqlclient-dev -y
```

### Test Nginx is being served

set Security Group

- Inbound Rules - Port 80 "anywhere"

ref: [www.nginx.com/blog/nginx-plus-on-amazon-ec2-getting-started/](https://www.nginx.com/blog/nginx-plus-on-amazon-ec2-getting-started/)


### Configure project

Environment Variables have to be added for Gunicorn. Make a file called this and fill in with one's own values

**# /home/ubuntu/djangoaws_project/.rds-config**

```
RDS_NAME=
RDS_USERNAME=
RDS_PASSWORD==
RDS_HOST=
RDS_PORT=
```

```
source .rds-config
```

Clone repo, create virtualenv and install requirements

```
git clone https://github.com/aaronlelevier/django-aws-boilerplate.git djangoaws_project

cd djangoaws_project

python3 -m venv venv

. venv/bin/activate

pip install -r requirements/prod.txt
```

#### Gunicorn

Log dir setup

```
sudo mkdir /var/log/gunicorn
sudo chown -R ubuntu:ubuntu -R /var/log/gunicorn/
```

Installing and starting

```
sudo cp gunicorn.service /etc/systemd/system/gunicorn.service

# starting
sudo systemctl start gunicorn
sudo systemctl enable gunicorn

# restarting
sudo systemctl daemon-reload
sudo systemctl restart gunicorn

# check status
sudo systemctl status gunicorn
```

Restart Nginx with current config. Gunicorn service must be running on the `.sock` prior to this step

```
sudo cp /home/ubuntu/djangoaws_project/djangoaws.conf /etc/nginx/sites-enabled/default

sudo nginx -t

sudo systemctl restart nginx
```

### Starting and Stoping

#### EC2 instance

Gunicorn - worked with current config script

Nginx - started on server init automatically

## License

MIT

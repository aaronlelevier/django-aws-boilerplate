# djangoaws

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

### Install steps

```
sudo apt-get update

sudo apt-get install python3-pip

sudo apt-get install python3-venv

sudo apt-get install nginx
```

MySQL client required packages

```
sudo apt-get install libmysqlclient-dev
```

Clone repo, create virtualenv and install requirements

```
git clone https://github.com/aaronlelevier/djangoaws_project.git

cd djangoaws_project

python3 -m venv venv

. venv/bin/activate

pip install -r requirements/prod.txt
```

#### Gunicorn

Log dir setup

```
sudo mkdir /var/log/gunicorn
```

Installing and starting

```
copy gunicorn.service file to /etc/systemd/system/gunicorn.service

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

### Notes

*Not yet known where these go in the install steps*

Start gunicorn on a socket

```
gunicorn --daemon djangoaws.wsgi -b unix:/home/ubuntu/djangoaws_project/djangoaws/djangoaws.sock
```

Collect static assets for serving by the Nginx location

```
./manage.py collectstatic --noinput
```

## License

MIT
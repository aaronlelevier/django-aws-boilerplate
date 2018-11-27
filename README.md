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

### Centos packages

```
sudo yum install git

```

### Python

```
sudo easy_install pip

sudo install virtualenv

virtualenv pip
```


## License

MIT
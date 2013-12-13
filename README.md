# Python Quick Start Guide

This guide will walk you through deploying a Python Django CRUD application on Deis.

## Prerequisites

* A [User Account](http://docs.deis.io/en/latest/client/register/) on a [Deis Controller](http://docs.deis.io/en/latest/terms/controller/).
* A [Deis Formation](http://docs.deis.io/en/latest/gettingstarted/concepts/#formations) that is ready to host applications

If you do not yet have a controller or a Deis formation, please review the [Deis installation](http://docs.deis.io/en/latest/installation/) instructions.

## Setup your workstation

* Install [RubyGems](http://rubygems.org/pages/download) to get the `gem` command on your workstation
* Install [Foreman](http://ddollar.github.com/foreman/) with `gem install foreman`
* Install [Python](http://www.python.org/getit/) (we still recommend 2.7.x for library compatibility)
* Install [Django](https://www.djangoproject.com/)

## Clone your Application

If you want to use an existing application, no problem.  You can also use the Deis sample application located at <https://github.com/bengrunfeld/example-python-django-crud-app>.  Clone the example application to your local workstation:

    $ git clone git@github.com:bengrunfeld/example-python-django-crud-app.git.git
    $ cd example-python-django-crud-app

## Prepare your Application

To use a Python application with Deis, you will need to conform to 3 basic requirements:

 1. Use [Pip](http://pypi.python.org/pypi/pip) to manage dependencies
 2. Use [Foreman](http://ddollar.github.com/foreman/) to manage processes
 3. Use [Environment Variables](https://help.ubuntu.com/community/EnvironmentVariables) to manage configuration inside your application

If you're deploying the example application, it already conforms to these requirements.

#### 1. Use Pip to manage dependencies

Pip requires that you explicitly declare your dependencies using a [requirements.txt](http://www.pip-installer.org/en/latest/cookbook.html) file. Here is a very basic example:

	Django==1.6
	dj-database-url==0.2.2
	dj-static==0.0.5
	gunicorn==18.0
	psycopg2==2.5.1
	static==0.4

We highly recommend isolating your dependencies inside a Python [virtualenv](https://python-guide.readthedocs.org/en/latest/dev/virtualenvs/):

    $ virtualenv venv                        # create the virtualenv
    New python executable in venv/bin/python
    Installing setuptools............done.
    Installing pip...............done.
    $ source venv/bin/activate               # activate the virtualenv
    
You can then install dependencies on your local workstation with `pip install -r requirements.txt`:

	(venv)$ pip install -r requirements.txt 
	Downloading/unpacking dj-static==0.0.5 (from -r requirements.txt (line 3))
	Downloading dj-static-0.0.5.tar.gz
	Running setup.py egg_info for package dj-static

#### 2. Use Foreman to manage processes

Deis relies on a [Foreman](http://ddollar.github.com/foreman/) `Procfile` that lives in the root of your repository.  This is where you define the command(s) used to run your application.  Here is an example `Procfile`:

    web: gunicorn django_crud_app.wsgi

This tells Deis to run `web` workers using the command `gunicorn django_crud_app.wsgi`. You can test this locally by running `foreman start`.

	(venv)$ foreman start
	

You should now be able to access your application locally at <http://localhost:5000>.

#### 3. Use Environment Variables to manage configuration

Deis uses environment variables to manage your application's configuration, especially database configuration. For example, the following are used to connect your **Django app** to an **Amazon RDS Instance**.

	DJ_ENGINE: postgresql_psycopg2
	DJ_PASS: somepass
	DJ_USER: someuser
	DJ_HOST: id.somehost.us-west-2.rds.amazonaws.com
	DJ_NAME: somedb
	DJ_PORT: 5432

## Create a new Application

Per the prerequisites, we assume you have access to an existing Deis formation. If not, please review the Deis [installation instuctions](http://docs.deis.io/en/latest/gettingstarted/installation/).

Use the following command to create an application on an existing Deis formation.

    $ deis create --formation=<formationName> --id=<appName>
	Creating application... done, created <appName>
	Git remote deis added
    
If an ID is not provided, one will be auto-generated for you.

## Deploy your Application

Use `git push deis master` to deploy your application.

	$ git push deis master
	Counting objects: 65, done.
	Delta compression using up to 4 threads.
	Compressing objects: 100% (40/40), done.
	Writing objects: 100% (65/65), 15.95 KiB, done.
	Total 65 (delta 19), reused 61 (delta 18)
	       Python app detected
	-----> No runtime.txt provided; assuming python-2.7.4.
	-----> Preparing Python runtime (python-2.7.4)

Once your **Django** application has been deployed, you will need to sync the database before you can open it. To do this, run `deis run 'python manage.py syncdb'`.

You can then use `deis open` to view it in a browser. To find out more info about your application, use `deis info`.

## Scale your Application

To scale your application's [Docker](http://docker.io) containers, use `deis scale` and specify the number of containers for each process type defined in your application's `Procfile`. For example, `deis scale web=8`.

	$ deis scale web=8
	Scaling containers... but first, coffee!
	done in 16s
	
	=== <appName> Containers
	
	--- web: `gunicorn django_crud_app.wsgi`
	web.1 up 2013-12-12T23:04:56.242Z (dev2-runtime-1)
	web.2 up 2013-12-13T18:23:26.635Z (dev2-runtime-1)
	web.3 up 2013-12-13T18:23:26.653Z (dev2-runtime-1)
	web.4 up 2013-12-13T18:23:26.668Z (dev2-runtime-1)
	web.5 up 2013-12-13T18:23:26.684Z (dev2-runtime-1)
	web.6 up 2013-12-13T18:23:26.699Z (dev2-runtime-1)
	web.7 up 2013-12-13T18:23:26.714Z (dev2-runtime-1)
	web.8 up 2013-12-13T18:23:26.731Z (dev2-runtime-1)


## Configure your Application

Deis applications are configured using environment variables. To connect to a 3rd-party database like **Amazon RDS**, you'll need to set your login credentials using environment variables.

	$ deis config:set DJ_NAME=notesdb
	=== <appName>
	DJ_USER: opuser
	DJ_PASS: thispassword
	DJ_NAME: notesdb
	DJ_HOST: dbid.somehost.us-west-2.rds.amazonaws.com
	DJ_PORT: 5432
	DJ_ENGINE: postgresql_psycopg2

`deis config:set` is also how you connect your application to other backing services like queues and caches. You can use `deis run` to execute one-off commands against your application for things like database administration, initial application setup and inspecting your container environment. `deis run env` will return all of your environment variables that have been set in Deis.

	$ deis run ls -la
	total 60
	drwxr-xr-x  6 root root 4096 Dec 12 23:04 .
	drwxr-xr-x 69 root root 4096 Dec 13 18:30 ..
	-rw-rw-r--  1 root root   26 Dec 12 22:11 .gitignore
	drwxr-xr-x  3 root root 4096 Dec 12 23:03 .heroku
	drwxr-xr-x  2 root root 4096 Dec 13 18:26 .profile.d
	-rw-r--r--  1 root root   57 Dec 12 23:04 .release
	-rw-r--r--  1 root root   35 Dec 12 23:04 Procfile
	-rw-r--r--  1 root root  826 Dec 12 23:04 README.md
	drwxr-xr-x  2 root root 4096 Dec 13 18:26 django_crud_app
	-rw-r--r--  1 root root  258 Dec 12 23:04 manage.py
	drwxr-xr-x  4 root root 4096 Dec 12 23:04 notes
	-rw-r--r--  1 root root   94 Dec 12 23:04 requirements.txt
	-rw-r--r--  1 root root   13 Dec 12 23:04 runtime.txt

## Troubleshoot your Application

To view your application's log output, including any errors or stack traces, use `deis logs`.

    $ deis logs
	Dec 13 18:27:28 ip-172-31-28-70 djangoapp[web.7]: 2013-12-13 18:27:28 [13] [INFO] Using worker: sync
	Dec 13 18:27:28 ip-172-31-28-70 djangoapp[web.7]: 2013-12-13 18:27:28 [18] [INFO] Booting worker with pid: 18
	Dec 13 18:27:39 ip-172-31-28-70 djangoapp[web.8]: 2013-12-13 18:27:39 [14] [INFO] Starting gunicorn 18.0
	Dec 13 18:27:39 ip-172-31-28-70 djangoapp[web.8]: 2013-12-13 18:27:39 [14] [INFO] Listening at: http://0.0.0.0:10008 (14)

## Additional Resources

* [Get Deis](http://deis.io/get-deis/)
* [GitHub Project](https://github.com/opdemand/deis)
* [Documentation](http://docs.deis.io/)
* [Blog](http://deis.io/blog/)

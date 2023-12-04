# NMRR 3.x Installation Process

## INTRODUCTION

* This document describes a step by step installation process for installing NMRR 3.x using familiar `pip install` processes through the Python Packaging Index (PyPI).

* These instructions support the manual installation process for NMRR software version 3.x (a.k.a., __nmrr__ located at https://github.com/usnistgov/nmrr).

* More information about the Configurable Data Curation System (CDCS) of modular applications exists in the form of a [system manual](https://cdcs.nist.gov/cdcs-documentation/index.html) at http://cdcs.nist.gov.

## Notes for Particular Installation Platforms

* The default path of installation steps was written originally for installation on Windows systems.
* However, the steps were organized to be as general as possible with sufficient context information to be installed smoothly and easily on Non-Windows systems.
* The system has been successfully installed by a number of folks now on Non-Windows platforms such as Mac and Linux variants using this procedure with the following considerations kept in mind.
* To apply the given PyPI process to a Linux environment to get a basic installation going, there are only slight modifications to should be performed.
* Specific differences you should be aware of when installing on Linux or Mac are as follows:

  1. **Supporting Utilities:** The specific supporting utilities that are downloaded (i.e., redis, celery, mongo) - the install links for all those point to generic locations where you should just choose the ones appropriate to your platform.

  2. **Virtual Environment:** The specific python virtual environment may be varied, but it doesn't have to be.
     1. That is, you can install `Pyenv` on Windows, Linux or Mac. So, those commands should remain identical.
     2. If you decide to use a different one, just substitute any desired python virtual environment application and the instructions inside of it should remain the same.
     3. If you use an alternative application for creating and using python virtual environments, then merely use the appropriate equivalent commands for each command involving the python virtual environment.
     4. Mostly, the commands used for the python virtual environment have to do with:
       1. creating it (`pyenv virtualenv`),
       2. activating it (`pyenv activate <nmrr_virtual_environment_name>`),
       3. deactivating it (`pyenv deactivate`).
         * NOTE: Corresponding commands for related utilities often use very similar or identical commands.

  3. **Command Shell:** The commands executed in this installation occur in a windows command shell, in the case of Linux or Mac, they would be in the standard scripting shell (which is usually some kind of bash variant).

  4. **Command-Line Syntax:** The command-line syntax for one or two steps may need slight modification in Linux or Mac. For example, on Windows, when one starts the redis-server application, one refers to the executable as "redis-server.exe" and uses a path that goes to the default windows redis configuration file. These parameter-names would probably have a slightly different name (such as 'redis_server' and a different configuration-file-path-name) in the Linux or Mac environments, but other than that, the essential command and intent should be the same in each case.

  5. **Skip Windows-Only Step:** There's a step in the Windows install process that is Windows-specific, toward the end, where a given package (celery) needed to be updated (uninstalled/reinstalled) for a slightly different version because of a well-known Windows-specific bug/dependency in that community-library. That step is labeled as "Windows-only". So, just skip that step when installing for Linux or Mac.

* Other than the above cases, the rest of the process should be able to be executed as is.


### Parameter Values

1. Readers of this document are expected to make appropriate adjustments where their system's parameters differ from those described in this process.
2. Particularly for security-sensitive settings, such as usernames and passwords, readers are strongly encouraged:
	1. **DO** select parameter values which are secure and relevant to their installation.
	2. **DO NOT** use the example default parameter values provided here (which are insecure).
3. The default parameter values and examples used throughout this document are only provided for the purposes of illustrating the installation process steps as concretely as possible.


#### Some example default values of important installation parameters are shown here:


| Installation Parameter                     | Example Installation Parameter Value |
| :------------------------------------------| :-------------------------------------------:|
| NMRR application installation platform     | Windows operating system                     |
| NMRR application installation path         | c:\nmrr                             |
| NMRR application IP address                | 127.0.0.1                                    |
| NMRR application port number               | 8000                                         |
| NMRR virtual environment name              | nmrr_env                            |
| NMRR Superuser username                    | mgi_superuser                                |
| NMRR Superuser email                       | user_email@example.com                   |
| NMRR Superuser password                    | mgi_superuser_pwd                            |
| MongoDB administrative username            | mdb_admin_user                               |
| MongoDB administrative password            | mdb_admin_pwd                                |
| MongoDB non-administrative username        | mdb_user                                     |
| MongoDB non-administrative password        | mdb_pwd	                                    |
| Redis configuration file                   | c:\Program Files\Redis\redis.windows.conf    |

* **Note:** Sometimes this information is used in more than one place/step in the installation process.

#### This document will use the following __abstract settings__ in the instructions that follow:

| Installation Parameter                     | Parameter Value Used In This Document|
| ------------------------------------------ | :-------------------------------------------:|
| NMRR application installation path         | `<install_path>`                             |
| NMRR application IP address                | `<ip_address>`                               |
| NMRR application port number               | `<port_number>`                              |
| NMRR virtual environment name              | `<nmrr_virtual_environment_name>`            |
| NMRR Superuser username                    | `<nmrr_superuser_username>`                  |
| NMRR Superuser email                       | `<nmrr_superuser_email>`                     |
| NMRR Superuser password                    | `<nmrr_superuser_password>`                  |
| MongoDB administrative username            | `<mongodb_admin_username>`                   |
| MongoDB administrative password            | `<mongodb_admin_password>`                   |
| MongoDB non-administrative username        | `<mongodb_nonadmin_username>`                |
| MongoDB non-administrative password        | `<mongodb_nonadmin_password>`	            |
| Redis configuration file                   | `<redis_configuration_filename>`	            |

### Assumptions

* This installation process is being performed on a __Windows platform__.
	* If one is installing the NMRR on an operating system other than Windows, then
	  one must be sure to make the necessary modifications to each command or instruction.
		* e.g., such as using a different command terminal than the Windows platform command-line terminal.
	* With only small modifications, this process should also easily work on additional platforms where Python and Django are generally supported.
* The reader who is performing this installation process is familiar with basic tasks in that environment such as:
	* Updating environment variables (e.g., PATH).
	* Opening a command-line terminal (e.g., cmd.exe).
	* Following installation instructions for installing each application.
* The system on which this installation process is being performed has an __Internet connection__.
* Installation steps mostly involve typing or entering various commands at a command-line terminal (e.g., cmd.exe).
	* Some steps will require that additional tasks be performed (such as downloading and extracting files, executing installers, etc.).

### Conventions

* Certain steps described in these procedures should only take place within a __Python virtual environment__ in which the NMRR application is created.
	* Commands that **should** happen in __only virtual-environment__ command-line terminal windows will be prefixed with **'$$'**.
	* All other commands that should NOT occur in a virtual-environment (but which often occur in the __system-level-environment__) command-line terminal window will be prefixed with **'$'**.

## INSTALLATION INSTRUCTIONS

###	1. Install supporting applications on your host system.

* Python 3.8: https://www.python.org/downloads/release/python-380/ (NOTE: this will be installed via a virtual environment)
* MongoDB 6.0: https://www.mongodb.com/download-center#community
* Redis 7.0: https://redis.io/download
* Celery    : NOTE: This is installed below via `pip install`.
* gettext   : This utility is necessary for supporting internationalization in NMRR 3.x systems.
    - On Linux,
      - $$ `apt-get install gettext`
    -On Windows,
		  - https://mlocati.github.io/articles/gettext-iconv-windows.html

###	2. Configure the execution environment.

* Update the environment variable, __PATH__, to include the installation paths of each of the above-installed applications, respectively.

###	3. Open terminal window #1 and perform the first set of installation commands.

#### Open a terminal window.

```shell
$ cmd.exe
```

#### Install Pyenv


* NOTE: This enables you to install the NMRR software in Python virtual environments.

- Download and install [Pyenv](https://github.com/pyenv/pyenv#installation) and 
[Pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv#installation)
  
* Install a version of Python supported by the CDCS (see `python_requires` in [setup.py](https://github.com/usnistgov/core_main_app/blob/master/setup.py)):

```shell
$ pyenv install 3.8
```

* Then run the following commands:
```shell
$(base) pyenv virtualenv 3.8 <nmrr_virtual_environment_name>
$(base) pyenv activate <nmrr_virtual_environment_name>
```

* Example:
```shell
$(base) pyenv install 3.8
$(base) pyenv virtualenv 3.8 nmrr_env
$(base) pyenv activate nmrr_env
$(nmrr_env) 
```

#### Install the latest version of pip installation utility inside the newly-created virtual-environment.

```
$$ python -m pip install --upgrade pip
```

#### Download, extract, and configure nmrr from git repository.

* Download https://github.com/usnistgov/nmrr/archive/master.zip to the <install_path>\ directory.
* Extract nmrr-master.zip to form the following base installation directory: <install_path>\nmrr-master\ .
* Then move into that base install directory.

```shell
$$ cd nmrr-master
```

#### Create configuration file directory for MongoDB.

```shell
$$ mkdir conf
```

#### Create data directory for MongoDB.

```shell
$$ mkdir data\db
```

#### Create <install_path>\nmrr-master\conf\mongodb.conf file with the following content:

* NOTE: This instruction asks the user to:
	1. Create a new file, mongodb.conf, in the <install_path>\nmrr-master\conf\ directory.
	2. Ensure that the given file has the following content.
	3. Save that file as the primary MongoDB configuration file.

* General File Contents:

```
net:
   bindIp: <ip_address>
security:
   authorization: enabled
storage:
   dbPath: <install_path>/nmrr-master/data/db
```

* Example:

```
net:
   bindIp: 127.0.0.1
security:
   authorization: enabled
storage:
   dbPath: c:/nmrr/nmrr-master/data/db
```

#### Install NMRR supporting and core software packages.

```shell
$$ pip install --no-cache-dir -r requirements.txt
$$ pip install --no-cache-dir -r requirements.core.txt
```

#### Start MongoDB server.
```shell
$$ mongod --config conf\mongodb.conf
```

###	4. Open terminal window #2 and perform the next set of installation commands.

#### Open terminal window.

```shell
$ cmd.exe
```

#### Open virtual environment and move to the release installation directory.

* Command:
```shell
$ pyenv activate <nmrr_virtual_environment_name>
$$ cd <install_path>\nmrr-master\
```
* Example:
```shell
$ pyenv activate nmrr_env
$$ cd <install_path>\nmrr-master\
```

#### Create MongoDB administrative user.

* Command:

**NOTE:** Enter your own mongodb administrative username and password here. See the example below.

```shell
$$ mongo --port 27017

	use admin
	db.createUser(
	{
	user: "<mongodb_admin_username>",
	pwd: "<mongodb_admin_password>",
	roles: [ { role: "userAdminAnyDatabase", db: "admin"},"backup","restore"]
	}
	)
	exit
```

* Example:

```shell
$$ mongo --port 27017

	use admin
	db.createUser(
	{
	user: "mdb_admin_user",
	pwd: "mdb_admin_pwd",
	roles: [ { role: "userAdminAnyDatabase", db: "admin"},"backup","restore"]
	}
	)
	exit
```

* NOTES:
	* From within MongoDB's shell, type (or copy/paste!) each line, hitting the <ENTER> key after each one.
	* When done entering these commands, the user will be logged out from MongoDB.


#### Create MongoDB non-administrative user.

* Command:

	* Enter your own mongodb usernames and passwords for administrative and non-administrative accounts, respectively, here. Please see the example below.

```shell
$$ mongo --port 27017 -u "<mongodb_admin_username>" -p "<mongodb_admin_password>" --authenticationDatabase admin
	use mgi
	db.createUser(
	{
	 user: "<mongodb_nonadmin_username>",
	 pwd: "<mongodb_nonadmin_password>",
	 roles: ["readWrite"]
	}
	)
	exit
```


* Example:

```shell
$$ mongo --port 27017 -u "mdb_admin_user" -p "mdb_admin_pwd" --authenticationDatabase admin
	use mgi
	db.createUser(
	{
	 user: "mdb_user",
	 pwd: "mdb_pwd",
	 roles: ["readWrite"]
	}
	)
	exit
```

* NOTES:
	* From within MongoDB's shell, type (or copy/paste!) each line, hitting the <ENTER> key after each one.
	* When done entering these commands, the user will be logged out from MongoDB.

#### Edit and save <install_path>\nmrr-master\nmrr\settings.py file.

Some values of the `settings.py` file are set using environment
variables. Here is a list of expected environment variables:

| Variable | Description |
| ----------- | ----------- |
| DJANGO_SECRET_KEY     | [Secret Key](https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/#secret-key) for Django (should be a "large random value") |
| ALLOWED_HOSTS         | Comma-separated list of hosts (e.g. ALLOWED_HOSTS=127.0.0.1,localhost), see [Allowed Hosts](https://docs.djangoproject.com/en/2.2/ref/settings/#allowed-hosts) for more info.|
| SERVER_URI            | URI of the server (e.g. for local deployment, http://127.0.0.1:8000) |
| SERVER_NAME           | Name of the server (e.g. NMRR) |
| MONGO_HOST            | MongoDB host |
| MONGO_PORT            | MongoDB port (default port: 27017)|
| MONGO_USER            | User for MongoDB |
| MONGO_PASS            | User password for MongoDB |
| MONGO_DB              | Name of the Mongo database (e.g. nmrr) |
| POSTGRES_HOST         | Postrges Host |
| POSTGRES_PORT         | Postgres Port (default port: 5432)|
| POSTGRES_USER         | User for Postgres |
| POSTGRES_PASS         | User password for Postgres |
| POSTGRES_DB           | Name of the Postgres database (e.g. nmrr) |
| REDIS_HOST            | Redis host |
| REDIS_PORT            | Redis Port (default port: 6379) |
| REDIS_PASS            | Password for Redis|

Not all variables are required, depending on the server configuration
(e.g. if the development server uses a sqlite3 database, instead of
postgres, environment variables for postgres won't be required).
For development purposes, custom settings are provided in: `nmrr/dev_settings.py`.
Those settings also require to set a few environment variables. To do
so, copy the `.env.dev.example` into a `.env` file at the same location.
This `.env` should not be pushed to the repository. You can update the
values of the `.env` with values that work for your own configuration.
For mongodb:
```
MONGO_USER=<mongodb_nonadmin_username>
MONGO_PASS=<mongodb_nonadmin_password>
```
Example:
```
MONGO_USER=mdb_user
MONGO_PASSWORD=mdb_pwd
```

To run django commands, using a custom settings file, you can use the
following syntax:
```shell
python manage.py <command> --settings=<custom_settings>
```
Example: start the server with development settings
```shell
python manage.py runserver --settings=nmrr.dev_settings
```
Or set the `DJANGO_SETTINGS_MODULE` environment variable:
```shell
export DJANGO_SETTINGS_MODULE=<custom_settings>
python manage.py <command>
```
Example:
```shell
export DJANGO_SETTINGS_MODULE=nmrr.dev_settings
python manage.py runserver
```

NOTES:
- For development purposes, additional packages are required and bundled with the 
  [core_main_app](https://github.com/usnistgov/core_main_app) package. To install these
  development packages, run:
	```
	$$ pip install core_main_app[develop]
	```
- the key differences between the main `settings.py` file and the
`dev_settings.py` file is that the development version overrides the
databases setting to use sqlite3 instead of postgres, and sets the
`DEBUG` setting to `True`.
- settings for deployment in production can be written the same way
as the development settings of this repository, by adding and overriding
the main settings file. Additional information about writing a
settings file for production can be found here:
https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

#### Start Redis server.

* Command:
```shell
$$ redis-server <redis_configuration_filename>
```

* Example:
```shell
$$ redis-server "c:\Program Files\Redis\redis.windows.conf"
```

* NOTES:
	* When redis-server starts, it will create a background process and will return to the command terminal prompt, allowing one to reuse that terminal to run other commands


#### Start celery.

```shell
$$ celery --app=nmrr worker -E -l info
$$ celery --app=nmrr beat -l info
```

###	5. Open terminal window #3 and perform the last set of installation commands.

```shell
$ cd <install_path>\nmrr-master\
$ pyenv activate nmrr_env

$$ python manage.py migrate
$$ python manage.py collectstatic --noinput
$$ python manage.py compilemessages
$$ python manage.py createsuperuser
```
* Command:
	* When prompted, fill in the following info:
		* username      : <nmrr_superuser_username>
		* email         : <nmrr_superuser_email>
		* password (x2) : <nmrr_superuser_password>

* Example:
	* When prompted, fill in the following info:
		* username      : mgi_superuser
		* email         : user_email@example.com
		* password (x2) : mgi_superuser_pwd

#### Run the system.

* Command:
```shell
$$ python manage.py runserver <ip_address>:<port_number>
```

* Example:
```shell
$$ python manage.py runserver 127.0.0.1:8000
```

###	6. Open system URL in a browser.

* Command:
	* open: http://<ip_address>:<port_number>

* Example:
	* open: http://127.0.0.1:8000

###	7. Login with superuser credentials.

* NOTE: The default from the top is username=mgi, password=mgi.

## Appendix A: Starting up a fully-installed system from a shutdown state

### Ensure MongoDB, Redis, and Celery are running in command-line windows.

#### in terminal window #1

```shell
$$ mongod --config conf\mongodb.conf
```

#### in terminal window #2

```shell
$$ redis-server "c:\Program Files\Redis\redis.windows.conf"
```

* NOTES:
	* The above is the syntax for a Window's Redis install. This may be different on other operating systems.
	* When redis-server starts, it will create a background process and will return to the command terminal prompt, allowing one to reuse that terminal to run other commands

```shell
$$ celery --app=nmrr worker -E -l info
$$ celery --app=nmrr beat -l info
```

#### in terminal window #3

#### Run the system.

* Command:
```shell
$$ python manage.py runserver <ip_address>:<port_number>
```

* Example:
```shell
$$ python manage.py runserver 127.0.0.1:8000
```

### Open browser: http://<ip_address>:<port_number>

* Command:
	* open: http://<ip_address>:<port_number>

* Example:
	* open: http://127.0.0.1:8000

### Login with superuser credentials.

* Command: login with:
	* username: <nmrr_superuser_username>
	* password: <nmrr_superuser_password>

* Example: login with:
	* username: mgi_superuser
	* password: mgi_superuser_pwd

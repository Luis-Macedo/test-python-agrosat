
# Farm Project - Backend


## Requirements

 - Python 3.8
 
## RUN

First, clone the repository:
```shell
$ git clone https://bitbucket.org/agrosatelite/farm-project.git
```

After, install python development package:

Ubuntu.
```shell
$ sudo apt-get install python-dev
```

Fedora.
```shell
$ sudo dnf install python3-devel
```

Inside the project directory, you need to create your virtual enviroment and active it:
```shell
$ python -m venv pyenv
$ source pyenv/bin/activate
```

Upgrade pip:
```shell
$ pip install -U pip
```

Run the command to install the env requirements:
```shell
$ pip install -r requirements.txt
```

### Install Spatialite suport.

Ubuntu.
```shell
$ sudo apt-get install libsqlite3-mod-spatialite
```

Fedora.
```shell
$ sudo dnf install libspatialite
```

### Install GDAL development libraries:

Ubuntu.
```shell
sudo apt-add-repository ppa:ubuntugis/ubuntugis-unstable
sudo apt-get update
sudo apt-get install libgdal-dev gdal-bin
```

Fedora.
```shell
$ sudo dnf install gdal-devel gdal
```

Install GDAL libary:
```shell
pip install GDAL==$(gdal-config --version) --global-option=build_ext --global-option="-I/usr/include/gdal"
```

### Running Django setup:

Run the migrations:
```shell
$ python manage.py migrate
```

Create your Django User:
```shell
$ python manage.py createsuperuser
```
Start the application:
```shell
$ python manage.py runserver
```
Look the swagger accessing *http://localhost:8000*
Look the django-admin accessing *http://localhost:8000/admin* and use your superuser email and password.

--- 

# Complete the Farm Project

1. Add the following fields to the FARM model:
    * [x] Municipality
    * [x] State
    * [x] A relation between FARM and OWNER (one farm needs to have one and only one owner. The owner can have zero or many farms).

2. Add restrictions so that it is not possible to create farms:
    * [x] Without owner
    * [x] Without municipality
    * [x] Without state
    * [x] Without name

3. Make it possible to search a farm by:
    * [x] The owner's name
    * [x] The owner's document number/identification
    * [x] The farm's name
    * [x] Municipality 
    * [x] State 
    * [x] The ID of the farm.

4. Edit the GET (details) of FARM so that it returns:
    * [x] All fields of the model

5. Edit the GET (list) of FARM so that it returns:
    * [x] Name, owner id, centroid, area, municipality and state

## Hints
1. To test your code you can use the swagger to make requests
2. To test geometry fields you can pass geojson data. You can create geojson data on *[http://geojson.io/](http://geojson.io/)*  (using just the geometry field in the geojson).


## Workshop: Satellite Image Processing with the Open Datacube 1.8.2

The Open Data Cube provides an easy to use Python enviroment to work with analysis ready earth observation data.
This workshop comprises the following content:

### Content

0. Setting the development enviorment.
1. Gentle introduction to remote sensing and satellite image processing
2. Landsat 8 Scene Adquisition
2. Landsat 8 scene Indexation/Ingestion
3. First Application

0 is available on this readme. 1 - 4 are available on the jupyter notebooks or through the [wiki](https://github.com/DonAurelio/open-datacube-workshop/wiki).

### Requirements

* Docker 
* Docker Compose

### Setting the development enviorment.

Clone this repository and get into the **open-datacube-workshop** foder.

```sh 
git clone https://github.com/DonAurelio/open-datacube-workshop.git && cd open-datacube-workshop
```

Start containers

```sh
docker-compose up -d 
```

Inspect runnig containes

```sh
docker-compose ps
```

Get into the **cube** container

```sh
docker-compose exec cube bash
```

#### Create datacube database

With the following command, the opendatacube API will create all the tables needed to track the information regarding satelite images.

```sh 
cube@579ffee39db6:~$ datacube system init 
Initialising database...
Created.
```

#### Check if datacube system is ready

With the following command we will check if the open datacube API can reach the database and its working properly.

```sh 
cube@579ffee39db6:~$ datacube system check 
Version:       1.6.1+0.gee3c3d81.dirty
Config files:  /home/cube/.datacube.conf
Host:          cube_db:5432
Database:      datacube
User:          datacube
Environment:   None
Index Driver:  default

Valid connection:	YES
```

#### Configure Jupyter

Prevent jupyter notebook to ask for a password

```sh
cube@579ffee39db6:~$ mkdir /home/cube/.jupyter
cube@579ffee39db6:~$ echo c.NotebookApp.token = \'\' > /home/cube/.jupyter/jupyter_notebook_config.py
```

Start jupyter notebooks

```sh 
cube@579ffee39db6:~$ jupyter notebook --no-browser --port=8888 --ip=0.0.0.0 --allow-root
```

#### Get into the Tutorial

Follow [http://localhost:8888/tree/notebooks/tutorial](http://localhost:8888/tree/notebooks/tutorial) to get into the notebooks comprising the tutorial. The tutorial is also available on the [wiki](https://github.com/DonAurelio/open-datacube-workshop/wiki).

#### Manage Containers

Exit within the container

```sh
cube@579ffee39db6:~$ exit
```

Stop containers

```sh
docker-compose stop
```

Start containers

```sh
docker-compose start
```

Destroy containers 

```sh
docker-compose down -v --remove-orphans
```


## Credits

This documentation was elaborated based on the experiences acquired at the Colombian Open Data Cube Project developed by Universidad de los Andes, Bogotá, Colombia.

<!-- # References  -->

<!-- 1. [View Landsat 8 imagery for a chosen time period](http://geoscienceaustralia.github.io/digitalearthau/notebooks/09_Workflows/RetrieveLandsat8ViewAndExport.html)
2. [netCDF4 module](https://unidata.github.io/netcdf4-python/netCDF4/index.html)
3. [Lesson 1. Export Numpy Arrays to Geotiff Format Using Rasterio and Python](https://www.earthdatascience.org/courses/earth-analytics-python/multispectral-remote-sensing-in-python/export-numpy-array-to-geotiff-in-python/)
4. [Calculate NDVI using rasterio](http://www.loicdutrieux.net/pyLandsat/NDVI_calc.html)
5. [Coordinate Reference Systems](https://docs.qgis.org/testing/en/docs/gentle_gis_introduction/coordinate_reference_systems.html)
6. [Open Datacube Jupyter Notebooks](https://datacube-core.readthedocs.io/en/stable/user/guide.html)
7. [Lesson 1. Clean Remote Sensing Data in Python - Clouds, Shadows & Cloud Masks](https://www.earthdatascience.org/courses/earth-analytics-python/multispectral-remote-sensing-modis/cloud-masks-with-spectral-data-python/)
 -->
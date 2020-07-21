# Setting Open Datacube 1.8.2 for the Tutorial

Clone this repository and get into the **open-datacube-workshop/version_1.8.2** foder.

```sh 
git clone https://github.com/DonAurelio/open-datacube-workshop.git && cd open-datacube-workshop/version_1.8.2
```

Start containers

```sh
docker-compose up -d 
```

Inspect runnig containes

```sh
docker-compose ps
```

Get into the **datacube** container

```sh
docker-compose exec datacube bash
```

#### Create datacube database

With the following command, the opendatacube API will create all the tables needed to track the information regarding satelite images indexed in the cube.

```sh 
datacube@487239d46d68:~$ datacube system init 
Initialising database...
Created.
Checking indexes/views.
Done.
```

#### Check if datacube system is ready

Check if the open datacube API can reach the database and its working properly.

```sh 
datacube@487239d46d68:~$ datacube system check 
Version:       1.8.2
Config files:  
Host:          database:5432
Database:      datacube
User:          datacube
Environment:   None
Index Driver:  default

Valid connection:	YES
```

#### Start Jupyter

Start jupyter notebooks

```sh 
cube@579ffee39db6:~$ jupyter notebook --no-browser --port=8888 --ip=0.0.0.0 --allow-root
```

#### Get into the Tutorial

Use the following link [http://localhost:8881/tree/notebooks](http://localhost:8888/tree/notebooks) and follow the jupyter notebooks. 

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


<!-- # References  -->

<!-- 1. [View Landsat 8 imagery for a chosen time period](http://geoscienceaustralia.github.io/digitalearthau/notebooks/09_Workflows/RetrieveLandsat8ViewAndExport.html)
2. [netCDF4 module](https://unidata.github.io/netcdf4-python/netCDF4/index.html)
3. [Lesson 1. Export Numpy Arrays to Geotiff Format Using Rasterio and Python](https://www.earthdatascience.org/courses/earth-analytics-python/multispectral-remote-sensing-in-python/export-numpy-array-to-geotiff-in-python/)
4. [Calculate NDVI using rasterio](http://www.loicdutrieux.net/pyLandsat/NDVI_calc.html)
5. [Coordinate Reference Systems](https://docs.qgis.org/testing/en/docs/gentle_gis_introduction/coordinate_reference_systems.html)
6. [Open Datacube Jupyter Notebooks](https://datacube-core.readthedocs.io/en/stable/user/guide.html)
7. [Lesson 1. Clean Remote Sensing Data in Python - Clouds, Shadows & Cloud Masks](https://www.earthdatascience.org/courses/earth-analytics-python/multispectral-remote-sensing-modis/cloud-masks-with-spectral-data-python/)
 -->
## Workshop: Satellite Image Processing with the Open Datacube

About 710 Earth Observation satellites are orbiting the Earth. "The satellites collect about 1,200 scenes (images) that take up about 1 terabyte of data every day". The **Open Datacube (ODC)** initiative tackles the problem of organize, query and retrieve massive spatio-temporal data in a homogeneous way. We can then, query a satellite image like in the example depicted bellow:

```python
import datacube

dc = datacube.Datacube(app="Hello World")

xarr = dc.load(
    # Satellite 
    product="LS8_OLI_LASRC",
    # Area to be requested 
    latitude=(3,4),
    longitude=(-70, -69),
    # The query return the images that were obtained 
    # in the time range specified
    # Time format (YYYY-MM-DD)
    time=("2018-01-01","2018-12-31"),
    # Image spectrac bands
    measurements=['blue']
)
```

The Open Data Cube provides an easy to use Python enviroment to work with analysis ready earth observation data.
On this workshop you will learn to use the open datacube through jupyter notebooks and a ready to use open datacube environment based on docker containers.
For this workshop you can follow the open datacube 1.6.1 (version_1.6.1) or the 1.8.2 (version_1.8.2) tutorial.
This workshop comprises the following content:

### Content

0. Setting the development enviorment.
1. Gentle introduction to remote sensing and satellite image processing.
2. Satellite Image Adquisition.
2. Satellite Image Indexation/Ingestion into the datacube.
3. Retrieve an image from the datacube and perform the Normalized Vegetation Index (NDVI) analysis. 

### Requirements

For this workshop it is necessary to have the following requirements installed.  

* Docker 
* Docker Compose

<!-- # References  -->

<!-- 1. [View Landsat 8 imagery for a chosen time period](http://geoscienceaustralia.github.io/digitalearthau/notebooks/09_Workflows/RetrieveLandsat8ViewAndExport.html)
2. [netCDF4 module](https://unidata.github.io/netcdf4-python/netCDF4/index.html)
3. [Lesson 1. Export Numpy Arrays to Geotiff Format Using Rasterio and Python](https://www.earthdatascience.org/courses/earth-analytics-python/multispectral-remote-sensing-in-python/export-numpy-array-to-geotiff-in-python/)
4. [Calculate NDVI using rasterio](http://www.loicdutrieux.net/pyLandsat/NDVI_calc.html)
5. [Coordinate Reference Systems](https://docs.qgis.org/testing/en/docs/gentle_gis_introduction/coordinate_reference_systems.html)
6. [Open Datacube Jupyter Notebooks](https://datacube-core.readthedocs.io/en/stable/user/guide.html)
7. [Lesson 1. Clean Remote Sensing Data in Python - Clouds, Shadows & Cloud Masks](https://www.earthdatascience.org/courses/earth-analytics-python/multispectral-remote-sensing-modis/cloud-masks-with-spectral-data-python/)
 -->
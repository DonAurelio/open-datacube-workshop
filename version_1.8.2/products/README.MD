# Products

This folder contains som product definition files, datasets metadata generation scripsts, and ingestion configuration files for every product. All products shown here are Suerface Reflectance corrected products (Level 2).

More product definition files can be finded in the [Open Datacube Respository](https://github.com/opendatacube/datacube-dataset-config/blob/master/products/ls_usgs_sr_scene.yaml).

Ingestion configurations files can be generated with the following tools. [Create a Ingestion Configuration
](http://ec2-52-201-154-0.compute-1.amazonaws.com/data_cube_manager/ingestion).

Other dataset config files, metadata generation scripts and ingestion config files can be found [here](https://github.com/opendatacube/datacube-dataset-config).

# TODO

- [x] Test LS8_OLI_LASRC
- [ ] Test LS5_TM_LEDAPS
- [ ] Test LS7_ETM_LEDAPS
- [ ] Test S1_SAR_GAMMA0
- [ ] Update dataset metadata generation scrips to generate metadata in eo3 format instead of eo. Datacube documentation recommends this update in the [documentation](https://datacube-core.readthedocs.io/en/latest/ops/dataset_documents.html#dataset-metadata-doc-eo3).
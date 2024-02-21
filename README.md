# HOPSWORKS-UC1-M34

M34 DeepCube demonstration. With EarthNet minicuber and sample DeepLearning Model forward run. The demonstration is split into notebooks that guide you in the use of the minicuber and the spin up of the streamlit web based forecasting app.


## FINAL DEMO UC1

### Installation
For Final Demo UC1, use
```
conda create -n minicuber python=3.10
conda activate minicuber
conda install gdal cartopy xarray netcdf4 -c conda-forge

# INSTALL HOPSWORKS, JUPYTER ETC.

# IF TORCH NOT INSTALLED:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# INSTALL MINICUBER
pip install git+https://github.com/earthnet2021/earthnet-minicuber.git@hops

# INSTALL TOOLKIT
pip install earthnet folium h5netcdf
```

### Running the final demonstration notebook

Access:
```
FINAL_DEMO_UC1.ipynb
```


## Previous Installation

For Notebook 1 & 2, use
```
conda create -n uc1demo python=3.10 gdal cartopy -c conda-forge
conda activate uc1demo
pip install -r requirements.txt --index-url https://download.pytorch.org/whl/cpu
pip install scipy matplotlib seaborn netCDF4 xarray zarr dask shapely pillow pandas s3fs dask s3fs folium fsspec boto3 psycopg2 pystac-client stackstac planetary-computer rasterio[s3] rioxarray odc-algo segmentation-models-pytorch folium ipykernel ipywidgets sen2nbar earthnet-minicuber
# Install Hopsworks + Hopsworks Python Package
```

For Notebook 3, use
```
conda create -n uc1app python=3.10 -c conda-forge
conda activate uc1app
pip install -r forecasting_app/requirements.txt
pip install -e forecasting_app/.
# Install Hopsworks + Hopsworks Python Package
```

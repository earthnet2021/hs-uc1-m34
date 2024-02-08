# HOPSWORKS-UC1-M34

M34 DeepCube demonstration. With EarthNet minicuber and sample DeepLearning Model forward run. The demonstration is split into notebooks that guide you in the use of the minicuber and the spin up of the streamlit web based forecasting app.

## Installation

For Notebook 1 & 2, use
```
conda create -n uc1demo python=3.10 gdal cartopy -c conda-forge
conda activate uc1demo
pip install -r requirements.txt
pip install earthnet-minicuber
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

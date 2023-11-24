'import earthnet_minicuber
import rasterio
import dask
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as clr
import datetime
import folium
import timeit
import ee
import sys
from hops import hdfs


# It"s unclear how to authenticate into EE in a HopsWorks job. So no Cloud Marsk on this benchmark
basespecs = {
    "lon_lat": (43.598946, 3.087414), # center pixel
    "xy_shape": (128,128), # width, height of cutout around center pixel
    "resolution": 30, # in meters.. will use this together with grid of primary provider..
    "time_interval": "2018-01-01/2018-01-31",
    "providers": [
        {
            "name": "s2",
            "kwargs": {"bands": ["B02", "B03", "B04", "B05", "B06", "B07", "B8A"],#, "B09", "B11", "B12"], 
            "best_orbit_filter": True, "brdf_correction": True, "cloud_mask": False, "aws_bucket": "element84"}
        },
        {
            "name": "s1",
            "kwargs": {"bands": ["vv", "vh","mask"], "speckle_filter": True, "speckle_filter_kwargs": {"type": "lee", "size": 9}} 
        },
        {
            "name": "ndviclim",
            "kwargs": {"bands": ["mean", "std"]}
        },
        {
            "name": "srtm",
            "kwargs": {"bands": ["dem"]}
        },
        {
            "name": "esawc",
            "kwargs": {"bands": ["lc"]}
        },
        {
            "name": "era5",
            "kwargs": {
                "bands": ["t2m", "pev", "slhf", "ssr", "sp", "sshf", "e", "tp"], 
                "aggregation_types": ["mean", "min", "max"], 
                "zarrpath": "/Net/Groups/BGI/scratch/DeepCube/UC1/era5_africa/era5_africa_0d1_3hourly.zarr",
                "zarrurl": "https://storage.de.cloud.ovh.net/v1/AUTH_84d6da8e37fe4bb5aea18902da8c1170/uc1-africa/era5_africa_0d1_3hourly.zarr",
            }
        },
#         {
#             "name": "sg",
#             "kwargs": {
#                 "vars": ["bdod", "cec", "cfvo", "clay", "nitrogen", "phh2o", "ocd", "sand", "silt", "soc"],
#                 "depths": {"top": ["0-5cm", "5-15cm", "15-30cm"], "sub": ["30-60cm", "60-100cm", "100-200cm"]}, 
#                 "vals": ["mean"],
#                 "dirpath": "/Net/Groups/BGI/work_2/Landscapes_dynamics/downloads/soilgrids/Africa/"
#             }
#         },
#         {
#             "name": "geom",
#             "kwargs": {"filepath": "/Net/Groups/BGI/work_2/Landscapes_dynamics/downloads/Geomorphons/geom/geom_90M_africa_europe.tif"}
#         },
        {
            "name": "alos",
            "kwargs": {}
        },
        {
            "name": "cop",
            "kwargs": {}
        }
        ]
}

def do_cubing(n=16, numcores=4):
    project_root_path = hdfs.project_path()
    sampled_minicubes_path = project_root_path + "minicubes/same/"
    csv_samples_path = project_root_path + "Jupyter/same_minicube.csv"

    print("Minicubes will be saved to "+ sampled_minicubes_path)
    csv_samples = hdfs.copy_to_local(csv_samples_path)
    print(csv_samples)

    earthnet_minicuber.Minicuber.create_minicubes_from_dataframe("same", csv_samples, n = n, numcores = numcores, basespecs=basespecs)
    hdfs.copy_to_hdfs("same", sampled_minicubes_path, overwrite=True)

def write_to_file(data):
    project_root_path = hdfs.project_path()
    benchmark_text_path = project_root_path + "minicubes/"
    with open("benchmark.txt", "w") as f:
        f.write(data+"\n")
    hdfs.copy_to_hdfs("benchmark.txt", benchmark_text_path, overwrite=True)
    
    
# time minicube creation
timed16 = timeit.timeit("do_cubing(n=16, numcores=4)","from __main__ import do_cubing", number=3)
print(timed16)
print(sys.stdout.write(str(timed16)))
write_to_file(str(timed16))

timed32 = timeit.timeit("do_cubing(n=32, numcores=8)","from __main__ import do_cubing", number=3)
print(timed32)
print(sys.stdout.write(str(timed32)))
write_to_file(str(timed32))

timed56 = timeit.timeit("do_cubing(n=56, numcores=14)","from __main__ import do_cubing", number=3)
print(timed56)
print(sys.stdout.write(str(timed56)))
write_to_file(str(timed56))'
#!/usr/bin/env python

"""
Author: Lori Garzio on 11/14/2024
Last modified: 11/7/2025
Download GLORYS12V1 (Global Ocean Physics Reanalysis) datasets
https://data.marine.copernicus.eu/product/GLOBAL_MULTIYEAR_PHY_001_030/description
cmems_mod_glo_phy_my_0.083deg_P1M-m: monthly averages
"""

import copernicusmarine as cmems
import pandas as pd

extent = [-78, -65, 35, 45]

start = "2025-03-01T00:00:00"
end = "2025-05-31T00:00:00"
startstr = pd.to_datetime(start).strftime("%Y%m%d")
endstr = pd.to_datetime(end).strftime("%Y%m%d")
dsid = "cmems_mod_glo_phy_my_0.083deg_P1M-m"  # cmems_mod_glo_phy_my_0.083deg_P1M-m cmems_mod_glo_phy_myint_0.083deg_P1M-m

cmems.subset(
    dataset_id=dsid,
    variables=["bottomT"],
    minimum_longitude=-78,
    maximum_longitude=-65,
    minimum_latitude=35,
    maximum_latitude=45,
    start_datetime=start,
    end_datetime=end,
    output_filename=f'{dsid}-{startstr}_{endstr}.nc',
    output_directory='/Users/garzio/Documents/rucool/Saba/NOAA_SOE/data/cmems_data/glorys'
)

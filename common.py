import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from netCDF4 import Dataset

# tropics = np.logical_and(lat > -23.43666, lat < 23.43666)


def get_solar_data():
    data = Dataset('data/Solar_forcing_1st_mill.nc', 'r')
    t = data.variables['time'][:]
    TSI = data.variables['TSI'][:, 0, 0]
    data.close()
    return t.filled(), TSI.filled()


def get_volcanic_data():
    data = Dataset('data/Volc_Forc_AOD_1st_mill.nc', 'r')
    t = data.variables['time'][:]
    AOD = data.variables['AOD'][:, 0, 0]
    data.close()
    return t.filled(), AOD.filled()

_, TSI = get_solar_data()
_, AOD = get_volcanic_data()


def get_geodata(number):
    filename = 'data/T2M_R{}_ym_1stMill.nc'.format(number)
    data = Dataset(filename)
    t = data.variables['time'][:]
    lon = data.variables['lon'][:]
    lat = data.variables['lat'][:]
    T2m = data.variables['T2m'][:, :, :]
    data.close()
    return t.filled(), lon.filled(), lat.filled(), T2m.filled()

_, lon, lat, T1 = get_geodata(1)
_, _, _, T2 = get_geodata(2)


def plot_forcing():
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(TSI)
    plt.subplot(2, 1, 2)
    plt.plot(AOD)


def plot_geodata(t_index, data):
    plt.figure()
    plt.imshow(data[t_index, :, :], cmap='jet')
    
def normalize(x):
    return (x-np.mean(x))/np.std(x)

def filter_ts(AOD_min = -1e10, AOD_max = 1e10, TSI_min = -1e10, TSI_max = 1e10):
    return np.logical_and(
                np.logical_and(AOD >= AOD_min, AOD < AOD_max),
                np.logical_and(TSI >= TSI_min, TSI < TSI_max)
            )

def filter_lon(lon_min = -1e10, lon_max = 1e10):
    return np.logical_and(lon >= lon_min, lon < lon_max)

def filter_lat(lat_min = -1e10, lat_max = 1e10):
    return np.logical_and(lat >= lat_min, lat < lat_max)
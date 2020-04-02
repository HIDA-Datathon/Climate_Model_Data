import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from netCDF4 import Dataset

tropics = np.logical_and(lat > -23.43666, lat < 23.43666)


def get_solar_data():
    data = Dataset('data/Solar_forcing_1st_mill.nc', 'r')
    t = data.variables['time'][:]
    TSI = data.variables['TSI'][:, 0, 0]
    data.close()
    return t, TSI


def get_volcanic_data():
    data = Dataset('data/Volc_Forc_AOD_1st_mill.nc', 'r')
    t = data.variables['time'][:]
    AOD = data.variables['AOD'][:, 0, 0]
    data.close()
    return t, AOD


def get_geodata(number):
    filename = 'data/T2M_R{}_ym_1stMill.nc'.format(number)
    data = Dataset(filename)
    t = data.variables['time'][:]
    lon = data.variables['lon'][:]
    lat = data.variables['lat'][:]
    T2m = data.variables['T2m'][:, :, :]
    data.close()
    return t, lon, lat, T2m


def plot_forcing():
    t, TSI = get_solar_data()
    t, AOD = get_volcanic_data()

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(t, TSI)
    plt.subplot(2, 1, 2)
    plt.plot(t, AOD)


def plot_geodata(t_index, data):
    plt.figure()
    plt.imshow(data[t_index, :, :], cmap='jet')

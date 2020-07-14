import xarray as xr
import numpy as np

def get_data_set(data,var_name,xarr0):

    ncoords=[]
    xdims =[]
    xcords={}
    for x in xarr0.coords:
        if(x!='time'):
            ncoords.append( ( x, xarr0.coords[x]) )
            xdims.append(x)
            xcords[x]=xarr0.coords[x]
    variables ={var_name: xr.DataArray(data, dims=xdims,coords=ncoords)}
    output=xr.Dataset(variables, attrs={'crs':xarr0.crs})
    for x in output.coords:
        output.coords[x].attrs["units"]=xarr0.coords[x].units

    return output

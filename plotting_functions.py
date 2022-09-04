import matplotlib.pyplot as plt
import numpy as np
from dea_tools.plotting import rgb

def plot_rgb_ndvi(ds, figure_title):
    
    n_timesteps = len(ds.time)
    ax_x_size = len(ds.x)
    ax_y_size = len(ds.y)

    aspect_ratio = ax_x_size/ax_y_size
    
    fig_x_size = 2*np.ceil(2.5*aspect_ratio)
    fig_y_size = 2.5*np.ceil(n_timesteps)

    vmin, vmax = ds[["nbart_red", "nbart_green", "nbart_blue"]].to_array().quantile((0.02, 0.98)).values

    fig, ax = plt.subplots(n_timesteps, 2, figsize=(fig_x_size, fig_y_size))
    
    fig.suptitle(figure_title, fontsize=16, y=0.92)

    for i in range(n_timesteps):

        ax1, ax2 = ax[i]
        ds_timestep = ds.isel(time=i)

        rgb(ds_timestep, ax=ax1, robust=False, vmin=vmin, vmax=vmax)

        ds_timestep.NDVI.plot(ax=ax2, vmin=0, vmax=1)

        title = np.datetime_as_string(ds.isel(time=1).time.values, unit='D')

        for ax_i in ax[i]:
            ax_i.set_aspect('equal')
            ax_i.set_xticks([])
            ax_i.set_yticks([])
            ax_i.set_xlabel("")
            ax_i.set_ylabel("")
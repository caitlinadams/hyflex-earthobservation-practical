import matplotlib.pyplot as plt
import numpy as np
from dea_tools.plotting import rgb


def plot_rgb_ndvi(ds, figure_title):

    # Get the dimensions of the data for plotting
    n_timesteps = len(ds.time)
    ax_x_size = len(ds.x)
    ax_y_size = len(ds.y)

    # Calculate the aspect ratio for the plot
    aspect_ratio = ax_x_size / ax_y_size

    # Calculate the size the figure will need to be to plot all the timesteps
    fig_x_size = 2 * np.ceil(2.5 * aspect_ratio)
    fig_y_size = 2.5 * np.ceil(n_timesteps)

    # Get the 2nd and 98th percentile values for the data and set these as the  minimum and maximum values for plotting
    vmin, vmax = (
        ds[["nbart_red", "nbart_green", "nbart_blue"]]
        .to_array()
        .quantile((0.02, 0.98))
        .values
    )

    # Create the figure, with a row for each time steps, and two columns
    fig, ax = plt.subplots(n_timesteps, 2, figsize=(fig_x_size, fig_y_size))

    # Add the title to the figure
    fig.suptitle(figure_title, fontsize=16, y=0.92)

    # Create the visualisation for each timestep
    for i in range(n_timesteps):

        ax1, ax2 = ax[i]
        ds_timestep = ds.isel(time=i)

        # Use the RGB plotting function from Digital Earth Australia for the first plot in each row
        rgb(ds_timestep, ax=ax1, robust=False, vmin=vmin, vmax=vmax)

        # Plot the NDVI values for the second plot in each row
        ds_timestep.NDVI.plot(ax=ax2, vmin=0, vmax=1)

        # Set the title as the date for the timestep
        title = np.datetime_as_string(ds.isel(time=i).time.values, unit="D")

        # Clean up the figure by removing x and y labels and axis ticks
        for ax_i in ax[i]:
            ax_i.set_title(title)
            ax_i.set_aspect("equal")
            ax_i.set_xticks([])
            ax_i.set_yticks([])
            ax_i.set_xlabel("")
            ax_i.set_ylabel("")

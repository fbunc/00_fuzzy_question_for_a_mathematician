import all_functions  as cf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from IPython.display import display
#We like black background
plt.rcParams.update({
        "lines.color": "black",
        "patch.edgecolor": "black",
        "text.color": "white",
        "axes.facecolor": "black",
        "axes.edgecolor": "black",
        "axes.labelcolor": "black",
        "xtick.color": "black",
        "ytick.color": "black",
        "grid.color": "black",
        "figure.facecolor": "black",
        "figure.edgecolor": "black",
        "savefig.facecolor": "black",
        "savefig.edgecolor": "black"})
def generate_curve(N, M, Delta_r_o, T_o):
    omega = np.exp(2*np.pi*1j/T_o)
    r = np.zeros(N)
    for k in range(N):
        if k % M == 0:
            r[k] = r[k-1] + Delta_r_o
        else:
            r[k] = r[k-1]
    Z = r * omega**np.arange(N)
    return Z

def cartesian_coordinates(Z):
    u = np.real(Z)
    v = np.imag(Z)
    w = np.log(np.abs(Z))/np.log(2)
    return u, v, w


def plot_curve(u, v, w, line=False, scatt=True, figsize=(16, 16), M_color=12, axis_on=False,
               axis_color='black', axis_text_color='white', axis_line_color='white', axis_tick_color='white',cmap='hsv',show_plt=True):
   
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')
    colors = np.arange(len(u)) % M_color / M_color  # Generate colors based on index mod M_color
    
    if line:
        ax.plot(u, v, w, color='gray')  # You can customize the line color here

    if scatt:
        ax.scatter(u, v, w, c=colors, cmap=cmap)  # Use colors for scatter plot

    if axis_on:
        ax.axis('on')
        ax.xaxis.set_pane_color(axis_color)
        ax.yaxis.set_pane_color(axis_color)
        ax.zaxis.set_pane_color(axis_color)
        ax.xaxis._axinfo['grid'].update(color=axis_line_color, linestyle='-', linewidth=1)
        ax.yaxis._axinfo['grid'].update(color=axis_line_color, linestyle='-', linewidth=1)
        ax.zaxis._axinfo['grid'].update(color=axis_line_color, linestyle='-', linewidth=1)
        ax.xaxis.set_tick_params(colors=axis_tick_color)
        ax.yaxis.set_tick_params(colors=axis_tick_color)
        ax.zaxis.set_tick_params(colors=axis_tick_color)
        ax.xaxis.label.set_color(axis_text_color)
        ax.yaxis.label.set_color(axis_text_color)
        ax.zaxis.label.set_color(axis_text_color)
        ax.title.set_color(axis_text_color)

    else:
        ax.axis('off')

    if show_plt==True:
        plt.show()
    



# # Example usage:
# N = 10000*10
# M = 1
# M_color=13
# Delta_r_o = 1/M
# phi=0.5*(1+np.sqrt(5))
# T_o=phi


# Z = generate_curve(N, M, Delta_r_o, T_o)
# u, v, w = cartesian_coordinates(Z)
# plot_curve(u, v, w, line=True, scatt=True,axis_on=True,M_color=M_color,cmap='coolwarm')


# N = 10000*3
# M = 13
# M_color=13
# Delta_r_o = 1/M
# phi=0.5*(1+np.sqrt(5))
# T_o=phi#1.005454588412977
# Z = generate_curve(N, M, Delta_r_o, T_o)
# u, v, w = cartesian_coordinates(Z)
# plot_curve(u, v, w, line=False, scatt=True,axis_on=False,M_color=M_color,cmap='coolwarm')


N = 10**4
M = 1
M_color=13
Delta_r_o = 1/M
phi=0.5*(1+np.sqrt(5))
T_o=2+phi-1
Z = generate_curve(N, M, Delta_r_o, T_o)
u, v, w = cartesian_coordinates(Z)
plot_curve(u, v, w, line=True, scatt=True,axis_on=True,M_color=M_color,cmap='hsv')



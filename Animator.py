import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import sys
sys.path.append('../..')  # add parent directory
import numpy as np
import satelliteParam as P


class Animator:
    '''
        Create bodies animation
    '''
    def __init__(self):
        self.flagInit = True
        self.flagTraceInit = True

        self.fig_inertial, self.ax_inertial = plt.subplots()
        self.fig_satframe, self.ax_satframe = plt.subplots()

        self.handle_inertial = []
        self.handle_inertial_trace = []

        self.handle_satframe = []

        self.ax_inertial.axis([-5, 5, -5, 5])
        self.ax_inertial.axis('equal')

        self.ax_satframe.axis([-5, 5, -5, 5])
        self.ax_satframe.axis('equal')

        self.coord_hist = []


    def update(self, sat_coord, wrench_coord):
        # Process inputs to function
        self.drawBodies_inertial(sat_coord=sat_coord, wrench_coord=wrench_coord)
        self.drawBodies_satframe(sat_coord=sat_coord, wrench_coord=wrench_coord)
        # self.ax.axis('equal')

        # After each function has been called, initialization is over.
        if self.flagInit == True:
            self.flagInit = False

    def drawBodies_inertial(self, sat_coord, wrench_coord):

        satellite_xy = (sat_coord.item(0), sat_coord.item(1))
        earth_xy = (0, 0)
        wrench_xy = (wrench_coord.item(0), wrench_coord.item(1))

        self.coord_hist.append(satellite_xy)
        if len(self.coord_hist) > P.trace_memory:
            self.coord_hist = self.coord_hist[1:]
            self.flagTraceInit = False

        if self.flagInit == True:

            # Define earth drawing
            self.handle_inertial.append(mpatches.Circle(earth_xy, radius=P.radius_earth, fc='blue',
                                                ec='limegreen'))

            # Define satellite drawing
            self.handle_inertial.append(mpatches.Circle(satellite_xy, radius=P.radius_satellite,
                                                fc='yellow',
                                               ec='black'))

            # Define wrench drawing
            self.handle_inertial.append(mpatches.Circle(wrench_xy, radius=P.radius_wrench, fc="red",
                                               ec="black"))

            self.ax_inertial.add_patch(self.handle_inertial[0])
            self.ax_inertial.add_patch(self.handle_inertial[1])
            self.ax_inertial.add_patch(self.handle_inertial[2])

        else:
            self.handle_inertial[1].center = satellite_xy
            self.handle_inertial[2].center = wrench_xy

        if self.flagTraceInit:
            self.handle_inertial_trace.append(mpatches.Circle(satellite_xy,
                                                     radius=P.radius_satellite_trace, fc='black'))
            self.ax_inertial.add_patch(self.handle_inertial_trace[-1])
        else:
            self.handle_inertial_trace[0].center = satellite_xy
            self.handle_inertial_trace = self.handle_inertial_trace[1:] + [
                self.handle_inertial_trace[0]]


    def drawBodies_satframe(self, sat_coord, wrench_coord):

        satellite_xy_satframe = (0,0)  # fix satellite at center of image
        wrench_xy_inertial = wrench_coord - sat_coord
        theta = np.arctan2(sat_coord[1], sat_coord[0])
        wrench_coord_satframe = self.rotation_matrix(theta).T @ wrench_xy_inertial
        wrench_xy_satframe = (wrench_coord_satframe.item(0), wrench_coord_satframe.item(1))

        earth_coord_inertial = -sat_coord
        earth_coord_satframe = self.rotation_matrix(theta).T @ earth_coord_inertial
        earth_xy_satframe = (earth_coord_satframe.item(0), earth_coord_satframe.item(1))

        if self.flagInit == True:

            # Define earth drawing
            self.handle_satframe.append(mpatches.Circle(earth_xy_satframe, radius=P.radius_earth,
                                                 fc='blue',
                                                ec='limegreen'))

            # Define satellite drawing
            self.handle_satframe.append(mpatches.Circle(satellite_xy_satframe,
                                                    radius=P.radius_satellite,
                                               fc='yellow',
                                               ec='black'))

            # Define wrench drawing
            self.handle_satframe.append(mpatches.Circle(wrench_xy_satframe, radius=P.radius_wrench,
                                                fc="red",
                                               ec="black"))

            self.ax_satframe.add_patch(self.handle_satframe[0])
            self.ax_satframe.add_patch(self.handle_satframe[1])
            self.ax_satframe.add_patch(self.handle_satframe[2])

        else:
            self.handle_satframe[0].center = earth_xy_satframe
            self.handle_satframe[2].center = wrench_xy_satframe

    def rotation_matrix(self, theta):
        return np.array([[np.cos(theta), -np.sin(theta)],
                         [np.sin(theta),  np.cos(theta)]])





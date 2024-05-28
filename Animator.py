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
        self.flagInit = True                  # Used to indicate initialization
        self.flagTraceInit = True
        self.fig, self.ax = plt.subplots()    # Initializes a figure and axes object
        self.handle = []                      # Initializes a list object that will
                                              # be used to contain handles to the
                                              # patches and line objects.
        self.handle_trace = []

        self.ax.axis([-5, 5, -5, 5])
        self.ax.axis('equal')

        self.coord_hist = []


    def update(self, coord):
        # Process inputs to function
        self.drawBodies(coord)
        # self.ax.axis('equal')

        # After each function has been called, initialization is over.
        if self.flagInit == True:
            self.flagInit = False

    def drawBodies(self, coord):

        satellite_xy = coord
        earth_xy = (0, 0)

        self.coord_hist.append(satellite_xy)
        if len(self.coord_hist) > P.trace_memory:
            self.coord_hist = self.coord_hist[1:]
            self.flagTraceInit = False

        if self.flagInit == True:

            # Define earth drawing
            self.handle.append(mpatches.Circle(earth_xy, radius=P.radius_earth, fc='blue',
                                                ec='limegreen'))

            # Define satellite drawing
            self.handle.append(mpatches.Circle(satellite_xy, radius=P.radius_satellite, fc='yellow',
                                               ec='black'))

            self.ax.add_patch(self.handle[0])
            self.ax.add_patch(self.handle[1])

        else:
            self.handle[1].center = satellite_xy

        if self.flagTraceInit:
            self.handle_trace.append(mpatches.Circle(satellite_xy,
                                                     radius=P.radius_satellite_trace, fc='black'))
            self.ax.add_patch(self.handle_trace[-1])
        else:
            self.handle_trace[0].center = satellite_xy
            self.handle_trace = self.handle_trace[1:] + [self.handle_trace[0]]






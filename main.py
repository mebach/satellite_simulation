import numpy as np
from Animator import Animator
import satelliteParam as P
import matplotlib.pyplot as plt
from satelliteDynamics import satelliteDynamics

animator = Animator()
dynamics = satelliteDynamics()

def main():

    t = P.t_start
    while t < P.t_end:
        t_next_plot = t + P.t_plot
        while t < t_next_plot:
            sat_state, wrench_state = dynamics.update(t)
            t = t + P.Ts

        sat_coord = sat_state[0:2]
        wrench_coord = wrench_state[0:2]

        animator.update(sat_coord, wrench_coord)
        t = t + P.t_plot
        plt.pause(0.0001)

if __name__ == '__main__':
    main()

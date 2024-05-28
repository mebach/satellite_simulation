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
            state = dynamics.update(t)
            t = t + P.Ts

        animator.update((state.item(0), state.item(1)))
        t = t + P.t_plot
        plt.pause(0.0001)

if __name__ == '__main__':
    main()

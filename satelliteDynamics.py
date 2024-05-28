import numpy as np
import random
import sys
sys.path.append('../..')  # add parent directory
import satelliteParam as P


class satelliteDynamics:
    def __init__(self):
        # Initial state conditions
        self.state = np.array([
            [P.x0_satellite],
            [P.y0_satellite],
            [P.xdot0_satellite],
            [P.ydot0_satellite]
        ])
        self.Ts = P.Ts

    def update(self, t):

        self.rk4_step()  # propagate the state by one time sample

        return self.state

    def f(self, state):

        x = state.item(0)
        y = state.item(1)
        xdot = state.item(2)
        ydot = state.item(3)

        R = x*x + y*y

        print(x,y)

        xddot = -(P.G*P.m_earth)/(R**(3/2)) * x
        yddot = -(P.G*P.m_earth)/(R**(3/2)) * y

        statedot = np.array([[xdot],
                         [ydot],
                         [xddot],
                         [yddot]])

        return statedot

    def rk4_step(self):
        # Integrate ODE using Runge-Kutta RK4 algorithm
        F1 = self.f(self.state)
        F2 = self.f(self.state + self.Ts / 2 * F1)
        F3 = self.f(self.state + self.Ts / 2 * F2)
        F4 = self.f(self.state + self.Ts * F3)
        self.state += self.Ts / 6 * (F1 + 2 * F2 + 2 * F3 + F4)


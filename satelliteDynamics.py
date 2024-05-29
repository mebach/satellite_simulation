import numpy as np
import random
import sys
sys.path.append('../..')  # add parent directory
import satelliteParam as P


class satelliteDynamics:
    def __init__(self):
        # Initial state conditions
        self.sat_state = np.array([
            [P.x0_satellite],
            [P.y0_satellite],
            [P.xdot0_satellite],
            [P.ydot0_satellite]
        ])

        self.wrench_state = np.array([
            [P.x0_satellite],
            [P.y0_satellite],
            [P.xdot0_satellite],
            [P.ydot0_satellite-0.05]
        ])

        self.Ts = P.Ts

    def update(self, t):

        self.sat_state = self.rk4_step(self.sat_state)  # propagate the state by one time sample
        self.wrench_state = self.rk4_step(self.wrench_state)
        # self.maneuver(t, "retrograde")

        return self.sat_state, self.wrench_state

    def f(self, state):

        x = state.item(0)
        y = state.item(1)
        xdot = state.item(2)
        ydot = state.item(3)

        R = x*x + y*y

        xddot = -(P.G*P.m_earth)/(R**(3/2)) * x
        yddot = -(P.G*P.m_earth)/(R**(3/2)) * y

        statedot = np.array([[xdot],
                         [ydot],
                         [xddot],
                         [yddot]])

        return statedot

    def rk4_step(self, state):
        # Integrate ODE using Runge-Kutta RK4 algorithm
        F1 = self.f(state)
        F2 = self.f(state + self.Ts / 2 * F1)
        F3 = self.f(state + self.Ts / 2 * F2)
        F4 = self.f(state + self.Ts * F3)
        state += self.Ts / 6 * (F1 + 2 * F2 + 2 * F3 + F4)

        return state

    def maneuver(self, t, man_type):
        velocity = np.array([[self.state.item(2)],[self.state.item(3)]])
        uvVelocity = velocity/np.linalg.norm(velocity)
        if man_type == "prograde":
            if t > 7 and t < 7.005:
                velocity += uvVelocity * 0.05

            self.state[2] = velocity[0]
            self.state[3] = velocity[1]

        if man_type == "retrograde":
            if t > 7 and t < 7.005:
                velocity -= uvVelocity * 0.05

            self.state[2] = velocity[0]
            self.state[3] = velocity[1]



# Simulation Parameters
t_start = 0
t_end   = 100
Ts      = 0.001
t_plot  = 0.02

# Initial conditions
x0_satellite = 1.0
y0_satellite = 0.0
xdot0_satellite = 0.0
ydot0_satellite = 4.0

# Dynamic Parameters
m_satellite = 1
m_earth = 10
m_wrench = 0.01
G = 1

# Animation Parameters
radius_earth = 0.5
radius_satellite = 0.04
radius_satellite_trace = 0.01
radius_wrench = 0.01
trace_memory = 175
import numpy as np
import time
from pyarena.world.graph_world import GraphWorld
from pyarena.plots.graph_planning import GraphPlanning
from pyarena.planning.ipp_bnb import IPPBnB


# world
size = np.array([5,5])
kwargsWorld = {'size': size}
mworld = GraphWorld(**kwargsWorld)

# Plot
kwargsPlot = {'world': mworld}
mplot = GraphPlanning(**kwargsPlot)

# Planning
kwargsPlanning = {'world': mworld}
mplanning = IPPBnB(**kwargsPlanning)

# Planning parameters
start = np.array([0,0]).reshape(2,1)
goal = np.array([3,3]).reshape(2,1)
budget = 13
horizon = 2
moving_horizon_path = []
i=0

# Run
while horizon <= budget: 
    print('Planning')
    kwargsIPPBnB = {'budget': budget, 'path': moving_horizon_path, 'horizon': horizon}
    optimal_path, optimal_cost = mplanning.run(start, goal, **kwargsIPPBnB)
    
    # Print
    if len(optimal_path) > len(moving_horizon_path): 
        next_node_id = mworld.graph.edges[optimal_path[i]].end_node_id
        moving_horizon_path.append(optimal_path[i])
    
    # Plot
    mplot.update(optimal_path, moving_horizon_path)
    time.sleep(1)
    # Update path and budget
    start = mworld.graph.nodes[next_node_id].state.reshape(2,1)
    budget -= 1
    i+=1

    print('Next Waypoint:', start.T)
    print('Remaing budget', budget)
    print('--------------------')

mplot.update(optimal_path)
wait = input('Press a key to finish')




import matplotlib.pyplot as plt
import agentpy as ap
# Custom made classes and functions
from TrafficModeling.multiAgentTraffic import MultiAgentTraffic
from TrafficModeling.roundabout import Roundabout
from TrafficModeling.road import Road

# Road agent positions
ratio = 3
x_center = 13
y_center = 13

cars_amount = 3
begin_points = [(26,13), (13,26), (13,0)]
end_points = [(0,13), (26,13), (13,26)]

roads_positions = []

# Generate road coordinates for each car and background road coordinates
for i in range(cars_amount):
    road = Road(ratio, x_center, y_center, begin_points[i], end_points[i])
    roads_positions.append(road.drawRoad())
road_background = road.drawBG()

# Define parameters
parameters = { 
    'size':27, 
    'steps':50,
    'roads_positions':roads_positions,
    'road_background':road_background,
    'cars_amount':cars_amount,
    'begin_points':begin_points
    
}

# Create single-run animation with custom colors
def animation_plot(model, ax):
    attr_grid=model.city.attr_grid('type_agent')
    color_dict = {0:'#808080', 1:'#ADFFBF', 2: '#FF00FF',3:'#0000FF', 4:'00FF00', None: '#497a41'}
    ap.gridplot (attr_grid, ax=ax, color_dict=color_dict, convert=True)
    ax.set_title(f"Traffic simulation\n"
    f"Time-step: {model.t}")

fig, ax = plt. subplots()

model = MultiAgentTraffic(parameters)

animation = ap.animate(model, fig, ax, animation_plot)
animation.save("./output/modelanimation.gif")
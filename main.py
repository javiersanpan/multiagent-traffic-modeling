import matplotlib.pyplot as plt
import agentpy as ap
# Custom made classes and functions
from TrafficModeling.multiAgentTraffic import MultiAgentTraffic
from TrafficModeling.road import Road

# Canvas size
size = 27

# Road agent positions
ratio = 5
vertical_center = 13
horizontal_center = 13

begin_points = [(26,13), (13,26), (13,1)]
end_points = [(0,13), (26,13), (13,26)]
cars_amount = len(begin_points)

# Should background road be drawn
draw_background = False

# Generate road coordinates for each car and background road coordinates
roads_positions = []
for i in range(cars_amount):
    road = Road(ratio, vertical_center, horizontal_center, begin_points[i], end_points[i], size)
    roads_positions.append(road.drawRoad())

if draw_background:
    road_background = road.draw_background()
else:
    road_background = []

# Define parameters
parameters = { 
    'size':size, 
    'steps':50,

    'roads_positions':roads_positions,
    'road_background':road_background,
    'cars_amount':cars_amount,
    'begin_points':begin_points
}
# Create single-run animation with custom colors
def animation_plot(model, ax):
    attr_grid = model.city.attr_grid('type_agent')
    color_dict = {0:'#808080', 1:'#ADFFBF', 2: '#FF00FF',3:'#0000FF', 4:'#00FF00', None: '#497a41'}
    ap.gridplot(attr_grid, ax=ax, color_dict=color_dict, convert=True)
    ax.set_title(f"Traffic simulation\n"f"Time-step: {model.t}")

fig, ax = plt.subplots()

model = MultiAgentTraffic(parameters)

animation = ap.animate(model, fig, ax, animation_plot)
animation.save("./output/modelanimation.gif")

print("Model and animation generated successfully")
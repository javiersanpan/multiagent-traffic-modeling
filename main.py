import matplotlib.pyplot as plt
import agentpy as ap
# Custom made classes and functions
from TrafficModeling.multiAgentTraffic import MultiAgentTraffic
from TrafficModeling.roundabout import Roundabout
from TrafficModeling.road import Road

# Road agent positions
roadObj = Road(3, 13, 13, [26,13], [13,26])
POS = roadObj.drawRoad()
print(POS)
print("AAAAAAAAAAA")

POSITIONS_X = []
POSITIONS_Y = []
POSITIONS_BG = []

rab = Roundabout(3, 13, 13)

#POSITIONS_X = roadObj.drawRoad()

#for i in range(0, 11):
#    POSITIONS_X.append((13,i))
#    POSITIONS_Y.append((i,13))
    
#for i in range(16, 27):
#    POSITIONS_X.append((13,i))
#    POSITIONS_Y.append((i,13))

#POSITIONS_X = POSITIONS_X + rab.drawTL() + rab.drawTR()
#POSITIONS_X.append((10,13))

#POSITIONS_Y = POSITIONS_Y + rab.drawBR() + rab.drawTR()
#POSITIONS_Y.append((13,16))

#POSITIONS_BG = rab.drawBL() + rab.drawBR()

print(POSITIONS_X)
print(type(POSITIONS_X))
print(type(POS))
print("BBBBBBB")

POSITIONS_X = POS

#print(POSITIONS_X)

# Define parameters
parameters = { 
    'size':27, 
    'steps':50,
    'POSITIONS_X':POSITIONS_X,
    'POSITIONS_Y':POSITIONS_Y,
    'POSITIONS_BG':POSITIONS_BG
}
# Create single-run animation with custom colors
def animation_plot(model, ax):
    attr_grid=model.city.attr_grid('type_agent')
    color_dict = {0:'#808080', 1:'#ADFFBF', 2: '#FF00FF',3:'#0000FF', None: '#497a41'}
    ap.gridplot (attr_grid, ax=ax, color_dict=color_dict, convert=True)
    ax.set_title(f"Traffic simulation\n"
    f"Time-step: {model.t}")

fig, ax = plt. subplots()

model = MultiAgentTraffic(parameters)

animation = ap.animate(model, fig, ax, animation_plot)
animation.save("./output/classesanimation.gif")
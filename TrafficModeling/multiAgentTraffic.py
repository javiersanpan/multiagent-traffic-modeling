import agentpy as ap

#LO QUE NECESITAMOS ES PONERLE OTRO ATRIBUTO A LOS CARROS PORQUE SÓLO ESTÁ IDENTIFICANDO QUE HAY ROAD

class MultiAgentTraffic(ap.Model):
    def setup(self):
        # Read custom parameters
        self.roads_positions = self.p.roads_positions
        #####self.road_background = self.p.road_background
        self.cars_amount = self.p.cars_amount
        self.begin_points = self.p.begin_points

        # Create grid
        self.city = ap.Grid(self, [self.p.size] * 2, track_empty=True)

        # Create car agents
        self.cars=ap.AgentList(self,self.cars_amount)
        # Add car agents
        ####self.city.add_agents(self.cars, [self.begin_points[0], self.begin_points[1], self.begin_points[2]])
        self.city.add_agents(self.cars, [self.begin_points[0], self.begin_points[1]])


        # Create and add road agents
        road_agents = []
        for i in range(self.cars_amount):
            road_agents.append(ap.AgentList(self, len(self.roads_positions[i])))
            self.city.add_agents(road_agents[i], positions=self.roads_positions[i] ,empty=False)

        ####background_road_agent = ap.AgentList(self,len(self.road_background))
        ####self.city.add_agents(background_road_agent, positions=self.road_background, empty=False)

        # Agent type attribute
        
        #0: untravelled road
        #1: travelled road
        #2: car 0
        #3: car 1
        #4: car 2

        #identificar si es carro o road!!
        
        road_agents.travel = 0

        road_agents[0].type_agent = 0
        road_agents[1].type_agent = 0
        ####road_agents[2].type_agent = 0
        ###background_road_agent.type_agent = 0
        

        self.cars[0].type_agent = 2
        self.cars[1].type_agent = 3
        #####self.cars[2].type_agent = 4

        # Road direction attribute
        # Each element is a road for a different car agent
        road_agents[0].road_direction = 0
        road_agents[1].road_direction = 1
        ####road_agents[2].road_direction = 2
        ####background_road_agent.road_direction = 3

    def step(self):
        cars = self.cars
        
        for car in cars:
            print("----------------")
            print("car position: ")
            print(self.city.positions[car])
            print("neighbors positions: ")
            for neighbor in self.city.neighbors(car):
                new_position = self.city.positions[neighbor]
                print(new_position)
                print("type agent")
                print(neighbor.identify)

                if neighbor.travel == 0 and neighbor.road_direction == 0 and car.type_agent == 2:
                    self.city.move_to(car, new_position)
                    neighbor.travel = 1
                    break
                '''
                elif 2 <= neighbor.type_agent and neighbor.type_agent<=3 and car.type_agent == 2:
                    print("uno")

                    print("neighbor type agent")
                    print(neighbor.type_agent)

                    print("car type agent")
                    print(car.type_agent)

                    print("car position")
                    print(self.city.positions[car])

                    print("neighbor position")
                    print(self.city.positions[neighbor])
                ####elif 2 <= neighbor.type_agent and neighbor.type_agent<=4:
                    if neighbor.type_agent < car.type_agent:
                        print("AAAAAAAAAA")
                        continue 
                ''' 
                if car.type_agent == 3 and neighbor.identify == 1:
                    print("YES!!!!!")
                    break
                if neighbor.travel == 0 and neighbor.road_direction == 1 and car.type_agent == 3:
                    self.city.move_to(car, new_position)
                    neighbor.travel = 1
                    break
                '''
                elif 2 <= neighbor.type_agent and neighbor.type_agent<=3 and car.type_agent == 3:
                    print("dos")

                    print("neighbor type agent")
                    print(neighbor.type_agent)

                    print("car type agent")
                    print(car.type_agent)

                    print("car position")
                    print(self.city.positions[car])

                    print("neighbor position")
                    print(self.city.positions[neighbor])
                #####elif 2 <= neighbor.type_agent and neighbor.type_agent<=4:
                    if neighbor.type_agent < car.type_agent:
                        print("BBBBBBBB")
                        break
                '''
#####DESCOMENTAR
'''
                if neighbor.type_agent == 0 and neighbor.road_direction == 2 and car.type_agent == 4:
                    self.city.move_to(car, new_position)
                    neighbor.type_agent = 1
                    break
                elif 2 <= neighbor.type_agent and neighbor.type_agent<=4:
                    if neighbor.type_agent < car.type_agent:
                        continue
'''
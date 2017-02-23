import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random

class traffic(object):

    def __init__(self, cars,length,steps):
        self.speeds = []
        self.cars = cars
        self.length = length
        self.steps = steps
        self.road = np.zeros((steps,self.length))
        i=0
        while self.cars-cars!=self.cars:
            if random.random()<=(float(self.cars)/float(self.length)):
                self.road[0,i%self.length]=1
                cars = cars-1
            i = i+1

    def drive(self,step):
        drive = 0
        still = 0
        for i in range(0,self.length):
            if self.road[step-1,i]==1:
                if self.road[step-1,(i+1)%(self.length)]==1 :
                    self.road[step,i]=1
                    still +=1
                else:
                    self.road[step,i]=0
                    drive +=1
            elif self.road[step-1,i]==0:
                if self.road[step-1,(i-1)%self.length]==1:
                    self.road[step,i]=1
                else:
                    self.road[step,i]=0
        self.speeds.append((drive*80)/(drive+still))

    def evolve(self):
        for i in range(1,self.steps):
            self.drive(i)

    def avgspeed(self):
        totspeed=0
        for i in self.speeds:
            totspeed+=i
        avspeed = float(totspeed)/len(self.speeds)
        return avspeed

    def tPrint(self):
        ax = plt.axes()
        for j in range(len(self.road[0])):
            for i in range(len(self.road)):
                if self.road[i,j] == 1:
                    ax.add_patch(patches.Circle((j,i),0.5, color='b'))
        plt.axis('scaled')
        plt.title("evolution of the road")
        plt.xlabel("car position")
        plt.ylabel("iteration")
        plt.show()

class Stats(object):

    def __init__(self, roadsize, steps):
        self.roads = [traffic(i,roadsize,steps) for i in range(1,roadsize)]
        self.avspeeds = []
        self.densities = []

    def evolveStat(self):
        for i in self.roads:
            i.evolve()
            
    def plot(self):
        for i in self.roads:
            self.avspeeds.append(i.avgspeed())
            self.densities.append(float(i.cars)/100)
        plt.plot(self.densities, self.avspeeds, 'ro')
        plt.axis([0,1,0,90])
        plt.title("avg speed vs car density")
        plt.xlabel("Car density")
        plt.ylabel("avg. speed")
        plt.show()
        

        
def main():
    task = None
    while task != 'exit':
        task = (raw_input("plot car density against avg.speed(plot) \ngraphically represent the road(road) \nexit the program (exit) ?\n "))


        if task == 'road':
            
            a = 0
            while a<1:
                try:
                    a = float(raw_input("Car density? "))
                    break
                except ValueError:
                    print("use a number smaller than 1")

            while True:
                try:
                    steps = int(raw_input("number of iterations? "))
                    break
                except ValueError:
                    print("use a number")
    
            c=traffic(a*100,100,steps)
            c.evolve()
            c.tPrint()
            #print(c.speeds)
        elif task == 'plot':
            while True:
                try:
                    steps = int(raw_input("number of iterations? "))
                    break
                except ValueError:
                    print("use a number")
                    
            b = Stats(100,steps)
            b.evolveStat()
            b.plot()
        else:
            print("Use one of the given commands!")

main()

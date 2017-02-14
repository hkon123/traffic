import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random

class traffic(object):

    def __init__(self, cars,length,steps):
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
        for i in range(0,self.length):
            if self.road[step-1,i]==1:
                if self.road[step-1,(i+1)%(self.length)]==1 :
                    self.road[step,i]=1
                else:
                    self.road[step,i]=0
            elif self.road[step-1,i]==0:
                if self.road[step-1,(i-1)%self.length]==1:
                    self.road[step,i]=1
                else:
                    self.road[step,i]=0

    def evolve(self):
        for i in range(1,self.steps):
            self.drive(i)

    def tPrint(self):
        ax = plt.axes()
        for j in range(len(self.road[0])):
            for i in range(len(self.road)):
                if self.road[i,j] == 1:
                    ax.add_patch(patches.Circle((j,i),0.5, color='b'))
        plt.axis('scaled')
        plt.show()

    def speed(self):
        

def main():
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
    
    a=traffic(a*100,100,steps)
    a.evolve()
    a.tPrint()
    
main()

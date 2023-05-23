from Roads import road1

leftLane1 = road1.freeSpace
leftLane2 =  road1.laneWidth +  road1.freeSpace + 4
rightLane1 =  road1.laneWidth*2 + 23 + road1.freeSpace
rightLane2 = road1.laneWidth*3 + 23 + road1.freeSpace

print(leftLane1)#6
print(leftLane2)#52
print(rightLane1)#113
print(rightLane2)#155

def blitCoordinate(self,spawnLocation, carPath):
        # if carPath[0] == 1:
        #     x = self.blitCoordinate(spawnLocation, [random.choice([0,2])])
        if spawnLocation == 1 or spawnLocation == 2 or spawnLocation == 3:
            if self.boundaries[2] < self.boundaries[3] : 
                if carPath[0] == 0:
                    x = int(self.boundaries[0] + self.laneWidth + 4 + self.freeSpace)
                elif carPath[0] == 1:
                    if carPath[1] == 0:
                        x = int(self.boundaries[0] + self.laneWidth + 4 + self.freeSpace)
                    else:
                        x = int(self.boundaries[0] + self.freeSpace)
                else:
                    x = int(self.boundaries[0] + self.freeSpace)
                        
            elif self.boundaries[2] >= self.boundaries[3]: 
                if carPath[0] == 0:
                    x = int(self.boundaries[1] + self.freeSpace)
                elif carPath[0] == 1:
                    if carPath[1] == 0:
                        x = int(self.boundaries[1] + self.freeSpace)    
                    else:
                        x = int(self.boundaries[1] + self.laneWidth + 4 + self.freeSpace)
                else:
                    x = int(self.boundaries[1] +self.laneWidth + 4 + self.freeSpace)
        else:
            if self.boundaries[2] < self.boundaries[3] :
                if carPath[0] == 0:
                    x = int(self.boundaries[0] + self.freeSpace)
                elif carPath[0] == 1:
                    if carPath[1] == 0:
                        x = int(self.boundaries[0] + self.freeSpace)
                    else:
                        x = int(self.boundaries[0] + self.laneWidth + 4 + self.freeSpace)
                else:
                    x = int(self.boundaries[0] + self.laneWidth + 4 + self.freeSpace)
                        
            elif self.boundaries[2] >= self.boundaries[3]: 
                if carPath[0] == 0:
                    x = int(self.boundaries[1] +self.laneWidth + 4 + self.freeSpace)
                elif carPath[0] == 1:
                    if carPath[1] == 0:
                        x = int(self.boundaries[1] + self.laneWidth + 4 + self.freeSpace)
                    else:
                        x = int(self.boundaries[1] + self.freeSpace)    
                else:
                    x = int(self.boundaries[1] + self.freeSpace)
        return x
    
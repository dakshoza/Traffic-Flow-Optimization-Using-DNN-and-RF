from Roads import road1

leftLane1 = road1.freeSpace + 36
leftLane2 =  road1.laneWidth +  road1.freeSpace + 4 +35
rightLane1 =  road1.laneWidth*2 + 23 + road1.freeSpace +34
rightLane2 = road1.laneWidth*3 + 23 + road1.freeSpace +34

print(leftLane1)#46
print(leftLane2)#92
print(rightLane1)#153
print(rightLane2)#195


import math
pos=[0,0]
while True:
    s=input()
    if not s:
        break
    movement=s.split('')
    direction=movement[0]
    steps=int(movement[1])
    if direction =='UP':
        pos[0]+=steps
    elif direction =='DOWN':
        pos[0]-=steps
    elif direction =='LEFT':
        pos[0]-=steps
    elif direction =='RIGHT':
        pos[0]+=steps
    else:
        pass

print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
    
        
        
        

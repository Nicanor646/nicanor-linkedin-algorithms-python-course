import os

DOORS=int(os.environ.get("DOORS",100))

door_status = [False]*DOORS

print(door_status)
for idx in range(0,DOORS):
    print(f"idx: {idx} -------------")
    for jdx in range(idx+1,DOORS+1,idx+1):
        door_status[jdx-1] = not door_status[jdx-1] 


for idx in range(0,DOORS):
    print(f"Door {idx+1} is: {'Open' if door_status[idx] else 'Closed'}")


import time
import os

lion_frames = [
r"""
 /\_/\ 
( o o ) 
 > ^ <
""",
r"""
 /\_/\ 
( o o ) 
 < ^ >
"""
]

width = 50
pos = 0
frame = 0

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(" " * pos + lion_frames[frame])
    
    pos += 1
    frame = (frame + 1) % len(lion_frames)
    
    if pos > width:
        pos = 0

    time.sleep(0.2)
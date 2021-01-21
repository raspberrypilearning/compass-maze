#!/bin/python3

from sense_hat import *
import maze

maze.start()

sense = SenseHat()
sense.clear()

sense.set_rotation(90)

            
while True:
    
  rumbo = sense.get_compass()

  if rumbo < 45 or rumbo > 315:
    dir = 'norte'
  elif rumbo < 135:
    dir = 'este'
  elif rumbo < 225:
    dir = 'sur'
  else:
    dir = 'oeste'
    
  sense.show_letter(dir[0].upper(), text_colour=maze.getColour())
  
  for e in sense.stick.get_events():
    if e.action == ACTION_PRESSED and e.direction == DIRECTION_MIDDLE:
      maze.walk(dir)
      
  if maze.escaped():
    sense.clear(0, 255, 0)
    break;
        

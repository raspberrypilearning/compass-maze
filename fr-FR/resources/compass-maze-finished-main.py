#!/bin/python3

from sense_hat import *
import maze

maze.start()

sense = SenseHat()
sense.clear()

sense.set_rotation(90)

            
while True:
    
  cap = sense.get_compass()

  if cap < 45 or cap > 315:
    dir = 'nord'
  elif cap < 135:
    dir = 'est'
  elif cap < 225:
    dir = 'sud'
  else:
    dir = 'ouest'
    
  sense.show_letter(dir[0].upper(), text_colour=maze.getColour())
  
  for e in sense.stick.get_events():
    if e.action == ACTION_PRESSED and e.direction == DIRECTION_MIDDLE:
      maze.marche(dir)
      
  if maze.sorti():
    sense.clear(0, 255, 0)
    break;
        

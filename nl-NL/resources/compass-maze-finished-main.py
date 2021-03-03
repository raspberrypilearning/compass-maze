#!/bin/python3

from sense_hat import *
import maze

maze.start()

sense = SenseHat()
sense.clear()

sense.set_rotation(90)

            
while True:
    
  koers = sense.get_compass()

  if koers < 45 or koers > 315:
    richting = 'noord'
  elif koers < 135:
    richting = 'oost'
  elif koers < 225:
    richting = 'zuid'
  else:
    richting = 'west'
    
  sense.show_letter(richting[0].upper(), text_colour=maze.geefKleur())
  
  for e in sense.stick.get_events():
    if e.action == ACTION_PRESSED and e.direction == DIRECTION_MIDDLE:
      maze.loop(richting)
      
  if maze.ontsnapt():
    sense.clear(0, 255, 0)
    break
        

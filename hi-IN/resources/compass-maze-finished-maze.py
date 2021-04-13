#a dictionary linking a room to other room positions
rooms = {
            'Blue' : { 
                  'south' : 'Red',
                  'west'  : 'Yellow',
                },        

            'Red' : { 
                  'north' : 'Blue',
                },
                
            'Yellow' : { 
                  'east'  : 'Blue',
                  'south' : 'Green',
                },
                
            'Green' : {    
                }

         }
         
colours = { 'Blue' : [0, 0, 255], 
            'Red' : [255, 0, 0],
            'Yellow' : [255, 255, 0],
            'Green' : [0, 255, 0] 
          }

def start():
  #print a main menu and the commands
  print('बचने के लिए हरे कमरे का पता लगाएं।')
  showStatus()

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom + ' room')
  print("---------------------------")
  
  if(currentRoom != 'Green'):
    print("बाहर निकलें:")
    print(*rooms[currentRoom].keys(), sep=', ')
  
def getColour():
  return colours[currentRoom]

# बीच में खिलाड़ी को स्टार्ट करें
currentRoom = 'Blue'

def walk(dir):
  global currentRoom
  if dir in rooms[currentRoom]:
  #set the current room to the new room
    currentRoom = rooms[currentRoom][dir]
    print("आप चलते हो", dir)
  # नए कमरे में कोई दरवाजा (link) नहीं है
  else:
    print('आप उस रास्ते पर नहीं जा सकते!')
    
  showStatus()
    
  return currentRoom
  
def escaped():
  return currentRoom == 'Green'

# खोलीतील इतर खोल्यांच्या स्थानाशी जोडणारा एक शब्दकोश
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
  # मुख्य मेनू आणि कमांड प्रिंट करा
  print('Find the green room to escape.')
  showStatus()

def showStatus():
  # खेळाडूची सद्य स्थिती प्रिंट करा
  print('---------------------------')
  print('You are in the ' + currentRoom + ' room')
  print("---------------------------")
  
  if(currentRoom != 'Green'):
    print("Exits: ")
    print(*rooms[currentRoom].keys(), sep=', ')
  
def getColour():
  return colours[currentRoom]

# मध्यभागी प्लेअरला प्रारंभ करा
currentRoom = 'Blue'

def walk(dir):
  global currentRoom
  if dir in rooms[currentRoom]:
  # नवीन खोलीत सध्याची खोली सेट करा
    currentRoom = rooms[currentRoom][dir]
    print("You walk", dir)
  # नवीन खोलीत दरवाजा (दुवा) नाही
  else:
    print('You can\'t go that way!')
    
  showStatus()
    
  return currentRoom
  
def escaped():
  return currentRoom == 'Green'

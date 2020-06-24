# قاموس يربط بين غرفة وأماكن الغرف الأخرى
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
  # اطبع القائمة الرئيسية والأوامر
  print('Find the green room to escape.')
  showStatus()

def showStatus():
  # اطبع حالة اللاعب الحالية
  print('---------------------------')
  print('You are in the ' + currentRoom + ' room')
  print("---------------------------")
  
  if(currentRoom != 'Green'):
    print("Exits: ")
    print(*rooms[currentRoom].keys(), sep=', ')
  
def getColour():
  return colours[currentRoom]

#start the player in the middle
currentRoom = 'Blue'

def walk(dir):
  global currentRoom
  if dir in rooms[currentRoom]:
  # تعيين الغرفة الحالية للغرفة الجديدة
    currentRoom = rooms[currentRoom][dir]
    print("You walk", dir)
  # لا يوجد باب (رابط) للغرفة الجديدة
  else:
    print('لا يمكنك الذهاب من هذا الطريق!')
    
  showStatus()
    
  return currentRoom
  
def escaped():
  return currentRoom == 'Green'

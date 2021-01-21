#un diccionario que enlaza una habitación a las posiciones de las otras habitaciones
habitaciones = {
            'Azul' : { 
                  'sur' : 'Rojo',
                  'oeste' : 'Amarillo',
                },        

            'Rojo' : { 
                  'norte' : 'Azul',
                },
                
            'Amarillo' : { 
                  'este' : 'Azul',
                  'sur' : 'Verde',
                },
                
            'Verde' : {    
                }

         }
         
colores = { 'Azul' : [0, 0, 255], 
            'Rojo' : [255, 0, 0],
            'Amarillo' : [255, 255, 0],
            'Verde' : [0, 255, 0] 
          }

def start():
  #imprime un menú principal y los comandos
  print ('Encuentra la habitación verde para escapar.')
  showStatus()

def showStatus():
  #imprimir el estado actual del jugador
  print('---------------------------')
  print('Estás en la habitación ' + currentRoom)
  print("---------------------------")
  
  if(currentRoom != 'Verde'):
    print("Salidas: ")
    print(*habitaciones[currentRoom].keys(), sep=', ')
  
def getColour():
  return colores[currentRoom]

#comienza el jugador en el medio
currentRoom = 'Azul'

def walk(dir):
  global currentRoom
  if dir in habitaciones[currentRoom]:
  #establecer la habitación actual a la nueva habitación
    currentRoom = habitaciones[currentRoom][dir]
    print("Caminas hacia el", dir)
  #no hay puerta (enlace) a la nueva habitación
  else:
    print('¡No puedes ir en esa dirección!')
    
  showStatus()
    
  return currentRoom
  
def escaped():
  return currentRoom == 'Verde'

#een woordenboek dat een kamer koppelt aan andere kamerposities
kamers = {
            'Blauwe' : { 
                  'zuid' : 'Rode',
                  'west' : 'Gele',
                },        

            'Rode' : { 
                  'noord' : 'Blauwe',
                },
                
            'Gele' : { 
                  'oost' : 'Blauwe',
                  'zuid' : 'Groene',
                },
                
            'Groene' : {    
                }

         }
         
kleuren = { 'Blauwe' : [0, 0, 255], 
            'Rode' : [255, 0, 0],
            'Gele' : [255, 255, 0],
            'Groene' : [0, 255, 0] 
          }

def start():
  #laat een hoofdmenu en de commando's zien
  print('Vind de groene kamer om te ontsnappen.')
  toonStatus()

def toonStatus():
  #laat de huidige status van de speler zien
  print('---------------------------')
  print('Je bent in de ' + huidigeKamer + ' kamer')
  print("---------------------------")
  
  if(huidigeKamer != 'Groen'):
    print("Uitgangen: ")
    print(*kamers[huidigeKamer].keys(), sep=', ')
  
def geefKleur():
  return kleuren[huidigeKamer]

#laat de speler in het midden beginnen
huidigeKamer = 'Blauwe'

def loop(richting):
  global huidigeKamer
  if richting in kamers[huidigeKamer]:
  #de huidige kamer wordt de nieuwe kamer
    huidigeKamer = kamers[huidigeKamer][richting]
    print("Je loopt ", richting)
  #er is geen deur (verbinding) naar de nieuwe kamer
  else:
    print('Je kunt zo niet gaan!')
    
  toonStatus()
    
  return huidigeKamer
  
def ontsnapt():
  return huidigeKamer == 'Groene'

#un dictionnaire liant une salle aux autres positions de salles
salles = {
            'Bleu' : { 
                  'sud' : 'Rouge',
                  'ouest' : 'Jaune',
                },        

            'Rouge' : { 
                  'nord' : 'Bleu',
                },
                
            'Jaune' : { 
                  'est' : 'Bleu',
                  'sud' : 'Vert',
                },
                
            'Vert' : {    
                }

         }
         
couleurs = { 'Bleu' : [0, 0, 255], 
            'Rouge' : [255, 0, 0],
            'Jaune' : [255, 255, 0],
            'Vert' : [0, 255, 0] 
          }

def start():
  #affiche un menu principal et les commandes
  print('Trouve la salle verte pour sortir.')
  showStatus()

def showStatus():
  #affiche le statut actuel du joueur
  print('---------------------------')
  print('Tu es dans la salle' + salleCourante)
  print("---------------------------")
  
  if(salleCourante != 'Vert'):
    print("Sorties : ")
    print(*salles[salleCourante].keys(), sep=', ')
  
def getColour():
  return couleurs[salleCourante]

# démarre le joueur au milieu
salleCourante = 'Bleu'

def marche(dir):
  global salleCourante
  if dir in salles[salleCourante]:
  # définit la pièce courante dans la nouvelle pièce
    salleCourante = salles[salleCourante][dir]
    print ("Tu marches vers ", dir)
  #il n'y a pas de porte (lien) vers la nouvelle salle
  else:
    print('Tu ne peux pas aller par là!')
    
  showStatus()
    
  return salleCourante
  
def sorti():
  return salleCourante == 'Vert'

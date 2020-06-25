# قاموس يربط بين غرفة وأماكن الغرف الأخرى
rooms = {
            'أزرق' : { 
                  'الجنوب': 'احمر',
                  'غرب' : 'أصفر',
                } ،        

            'أحمر': { 
                  'شمال' : 'أزرق',
                } ،
                
            'أصفر' : { 
                  'الشرق' : 'أزرق',
                  'جنوب' : 'أخضر',
                } ،
                
            'أخضر' : {    
                }}

         }
         
colours= { 'أزرق' : [0, 0, 255], 
            'أحمر': [255, 0, 0],
            'أصفر' : [255, 255, 0],
            'أخضر' : [0, 255, 0] 
          }

def start():
  # اطبع القائمة الرئيسية والأوامر
  print('ابحث عن الغرفة الخضراء للخروج.')
  showStatus()

showStatus():
  # اطبع حالة اللاعب الحالية
  print('---------------------------')
  print('أنت في الغرفة ' + currentRoom)
  print("---------------------------")
  
  if(currentRoom != 'اخضر'):
    print("الخروج")
    print(*rooms[currentRoom].keys(), sep=', ')
  
def getColour ():
  return colours[currentRoom]

#ابدأ اللاعب في الوسط
currentRoom = "أزرق"

def walk(dir):
  global currentRoom
  if dir in rooms[currentRoom]:
  # تعيين الغرفة الحالية للغرفة الجديدة
    currentRoom = rooms[currentRoom][dir]
    print("أنت تمشي", dir)
  # لا يوجد باب (رابط) للغرفة الجديدة
  else:
    print('لا يمكنك الذهاب من هذا الطريق!')
    
  showStatus()
    
  return currentRoom
  
def escaped():
  return currentRoom == 'اخضر'

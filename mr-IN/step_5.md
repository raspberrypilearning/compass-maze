## रंग जोडा

Sense HAT पाहून तुम्ही कोणत्या खोलीत होता हे जर सांगू शकाल तर चांगले होईल.

चला सद्य खोलीच्या रंगात होकायंत्र अक्षर प्रदर्शित करूया.

उदाहरणार्थ, जर तुम्ही ब्लू खोलीमध्ये असाल आणि दक्षिणेकडे तोंड असल्यास तुम्हाला अक्षर S ब्लू दिसला पाहिजे.

+ तुम्हाला `text-colour` `sense.show_letter` ला देण्याची गरज असेल. ते चार वेळा करण्याऐवजी, Sense HAT वर अक्षर दर्शविण्यासाठी कोड बदलून dir व्हेरिएबल वापरा.
    
    `dir[0].upper()` स्ट्रिंगचे पहिले अक्षर घेते आणि त्याचे मोठ्या अक्षरात रूपांतर करते म्हणून "north" तुम्हाला 'N' देते.
    
    `show_letter` एकदा वापरण्यासाठी तुमचा होकायंत्र कोड बदला:
    
    ![screenshot](images/compass-upper.png)

+ तुमचा होकायंत्र कोड असा दिसला पाहिजे:
    
    ![screenshot](images/compass-upper-done.png)

+ आता जेव्हा तुम्ही होकायंत्र अक्षर प्रदर्शित करता तेव्हा सद्य खोलीचा रंग वापरा:
    
    ![screenshot](images/compass-colour.png)

+ तुमच्या कोडची चाचणी घ्या आणि तुम्हाला आढळले पाहिजे की अक्षराच्या रंगाने तुम्ही कोणत्या खोलीत आहात हे तुम्ही सांगू शकता.
    
    ![screenshot](images/compass-colour-east.png)
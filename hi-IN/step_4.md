## Navigating the maze

आइए अब किसी भूलभुलैया के इर्द-गिर्द नेविगेट करने के लिए कंपास का उपयोग करें।

भूलभुलैया में कमरे और दरवाजे इस नक्शे में दिखाए गए अनुसार हैं:

![screenshot](images/compass-maze-map.png)

आप नीले कमरे में शुरू करते हैं और वहाँ से निकलने के लिए आपको हरा कमरा ढूँढना होता है।

+ एक साधारण साहसिक गेम (जैसी RPG प्रोजेक्ट में होती है) बनाने के लिए कोड आपकी प्रोजेक्ट में maze.py में है।
    
    `maze.py` में कुछ फंक्शन होते हैं जो आपको भूलभुलैया गेम लिखने में मदद करते हैं:
    
    + `maze.start()` - गेम को शुरू करता है
    + `maze.escaped()` - आपको बताता है कि खिलाड़ी भूलभुलैया से निकल पाया है या नहीं
    + `maze.walk(dir)` - खिलाड़ी को दी गई दिशा में ले जाता है
    + `maze.getColour()` - आपको वर्तमान कमरे का रंग देता है
    
    आपको `maze.py` आयात करने की आवश्यकता होगी:
    
    ![screenshot](images/compass-import.png)

+ गेम `maze.start()` से शुरू करें:
    
    ![screenshot](images/compass-start.png)

+ गेम के निर्देश आपको Sense HAT के नीचे दिखाई देंगे।
    
    ![screenshot](images/compass-start-test.png)

+ भूलभुलैया के इर्द-गिर्द जाने के लिए आप जिस दिशा में जाना चाहते हैं उसके साथ आपको `maze.walk(dir)` का उपयोग करना होगा।
    
    वर्तमान कंपास दिशा को `dir` वेरिएबल में रखें, आपको इसे प्रत्येक कंपास दिशा के लिए सेट करना होगा:
    
    ![screenshot](images/compass-dir.png)

+ आइए अब हम खिलाड़ी को उस दिशा में चलने दें, हैं जिस दिशा में Sense HAT कंपास तब इंगित करता है जब वे जॉयस्टिक पर बीच का बटन दबाते हैं।
    
    ![screenshot](images/compass-joystick.png)

+ कंपास का उपयोग करके भूलभुलैया के इर्द-गिर्द घूमने का प्रयास करें।
    
    जॉयस्टिक को दबाने के लिए आपको Sense HAT विंडो में क्लिक करना होगा और फिर कीबोर्ड पर एंटर (रिटर्न) को दबाना होगा।

+ Test your project by moving the Sense HAT to the direction you want to move in and then tapping Enter on the keyboard.
    
    Look at the map if you need help to find the Green room.

+ When the player reaches the Green room they have managed to escape the maze. Let's turn the screen green when they win and end the game:
    
    ![स्क्रीनशॉट](images/compass-end.png)
    
    The `break` finished the loop to end the game.
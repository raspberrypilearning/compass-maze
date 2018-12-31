## कंपास की दिशा दिखाना

इसके बाद आइए हम आपको Sense HAT स्क्रीन पर, कंपास की N, E, S या W दिशा दिखाएँ।

यदि कंपास की हैडिंग डिग्री में 315 और 45 के बीच है तो Sense HAT उत्तर की ओर इंगित कर रहा है और आप 'N' प्रदर्शित करना चाहते हैं। यदि हैडिंग 45 और 315 के बीच है तो आप 'E' आदि प्रदर्शित करना चाहते हैं।

![screenshot](images/compass-quadrants.png)

+ First let's show an N on the screen when the Sense HAT is facing north.
    
    Remember that when the Sense HAT is facing North the USB ports are at the top:
    
    ![screenshot](images/compass-north.png)

+ Change your code to display an 'N' when the compass heading is between 45 and 135:
    
    ![screenshot](images/compass-north-code.png)

+ Drag the Sense HAT to North (USB ports at the top of the screen) to test your compass.
    
    ![screenshot](images/compass-north-test.png)

The 'N' won't disappear, you need to add code for the other directions.

+ Hmm, the 'N' is sideways. It would make more sense to have the letter facing in the same direction as the USB ports.
    
    Add the following code to rotate the Sense HAT display.
    
    ![screenshot](images/compass-rotate.png)
    
    Now the compass letter will be lined up with the USB ports which makes more sense when using the Sense HAT as a compass.

+ Now let's show an E on the screen when the Sense HAT is facing east. If you're not facing north then the heading must be more than 45 degrees so you can just check that it's less than 315:
    
    ![screenshot](images/compass-east-code.png)

+ Add the code for south. Look at the compass to work out what the condition needs to be.

+ Your code should look like this:
    
    ![screenshot](images/compass-south-code.png)

+ Now add the code for west. If it's not north, east or south then it must be west! You can just use an 'else'.
    
    ![स्क्रीनशॉट](images/compass-west-code.png)

+ Test your code by dragging the Sense HAT around.
    
    You've made a Sense HAT compass!
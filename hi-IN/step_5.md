## रंग जोड़ें

बेहतर होगा कि यदि आप केवल Sense HAT को देखकर यह बता सकें कि आप किस कमरे में थे।

आइए हम वर्तमान कमरे के रंग में कंपास अक्षर को प्रदर्शित करें।

उदाहरण के लिए, यदि आप नीले कमरे में हैं और आपका मुँह दक्षिण की ओर है तो आपको नीला अक्षर S दिखाई देना चाहिए।

+ आपको `sense.show_letter` को कोई `text-colour` (पाठ-रंग) प्रदान करना होगा। इसे चार बार करने के बजाय, Sense HAT पर दिखाने के लिए अक्षर का पता लगाने के लिए यह पता लगाने के लिए dir variable (निर्देशिका वेरिएबल) का उपयोग करने के लिए कोड को बदलें।
    
    `dir[0].upper()` किसी स्ट्रिंग के पहले अक्षर को लेता है और उसे एक बड़े अक्षर में बदल देता है जिससे "उत्तर" के लिए आपको 'N' मिलता है।
    
    Change your compass code to use `show_letter` once:
    
    ![screenshot](images/compass-upper.png)

+ आपका कंपास कोड अब इस प्रकार दिखना चाहिए:
    
    ![screenshot](images/compass-upper-done.png)

+ Now use the colour of the current room when you display the compass letter:
    
    ![screenshot](images/compass-colour.png)

+ Test your code and you should find that you can tell which room you're in from the colour of the letter.
    
    ![स्क्रीनशॉट](images/compass-colour-east.png)
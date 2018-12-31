## परिचय:

इस प्रोजेक्ट में आप रंगीन कमरों की भूलभुलैया से बाहर निकलने के लिए Sense HAT का उपयोग एक कंपास के रूप में करेंगे। आपको Sense HAT को उस दिशा में दिखाने की आवश्यकता होगी, जिस दिशा में आप जाना चाहते हैं और फिर आगे जाने के लिए जॉयस्टिक के बीच का बटन दबाएँ।

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/0c8cdacd70?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark">
</iframe> <img src="images/compass-final.png" />
</div>

गेम को चलाने के लिए Run (चलाएँ) को दबाएँ और trinket आउटपुट विंडो में दिखाई देने वाले पाठ को पढ़ें।

आपकी वर्तमान कंपास दिशा Sense HAT के डिस्प्ले पर प्रदर्शित होगी (N (उत्तर के लिए), S (दक्षिण के लिए), E (पूर्व के लिए) या W (पश्चिम के लिए)। आप एमुलेटर में Sense HAT को चला कर दिशा बदल सकते हैं।

जब आपका मुँह उस दिशा में होता है जिसमें आप जाना चाहते हैं, तो कुंजीपटल पर एंटर दबाकर जॉयस्टिक पर बीच का बटन दबाएँ।

### क्लब लीडरों के लिए अतिरिक्त जानकारी

यदि आप इस प्रोजेक्ट को प्रिंट करना चाहते हैं, तो कृपया [प्रिंटर अनुकूल संस्करण](https://projects.raspberrypi.org/en/projects/compass-maze/print) का उपयोग करें।

## \--- collapse \---

## title: क्लब लीडर की टिप्पणियाँ

## परिचय:

इस परियोजना में, बच्चे यह सीखेंगे कि Sense HAT मैग्नेटोमीटर (कंपास) का उपयोग कैसे करें, और किसी भूलभुलैया में से नेविगेट करने के लिए कंपास की दिशा का उपयोग कैसे करें।

## ऑनलाइन संसाधन

**इस प्रोजेक्ट में Python 3 का उपयोग किया जाता है।** Python को ऑनलाइन लिखने के लिए हम [Trinket](https://trinket.io/) का उपयोग करने की सलाह देते हैं। इस परियोजना में निम्नलिखित Trinket हैं:

* ['Compass Maze' (कंपास भूलभुलैया) Starter Trinket (स्टार्टर ट्रिंकेट) -- jumpto.cc/compass-go](http://jumpto.cc/compass-go)

एक ऐसा trinket भी है जिसमें पूर्ण किया गया प्रोजेक्ट है:

* [‘Compass Maze’ पूर्ण -- trinket.io/python/d11bf21615](https://trinket.io/python/d11bf21615)

## ऑफ़लाइन संसाधन

इस प्रोजेक्ट को Sense HAT से किसी Raspberry Pi कंप्यूटर पर [ऑफ़लाइन भी पूरा किया जा सकता है](https://www.codeclubprojects.org/en-GB/resources/physical-sense-hat/)। आप इस प्रोजेक्ट के लिए 'प्रोजेक्ट सामग्री' लिंक पर क्लिक करके प्रोजेक्ट के संसाधनों पर पहुँच प्राप्त कर सकते हैं। इस लिंक में 'प्रोजेक्ट संसाधन' खंड है, जिसमें ऐसे संसाधन सम्मिलित हैं जिसकी बच्चों को इस प्रोजेक्ट को ऑफ़लाइन पूरा करने के लिए ज़रूरत होगी। सुनिश्चित करें कि प्रत्येक बच्चे को इन संसाधनों की प्रतिलिपि तक पहुँच प्राप्त होती है। इस खंड में निम्नलिखित फाइलें शामिल हैं:

* compass-maze/main.py
* compass-maze/maze.py

आपको 'स्वयंसेवक संसाधन' खंड में इस प्रोजेक्ट का पूर्ण किया गया संस्करण भी मिल सकता है, जिसमें निम्न शामिल हैं:

* compass-maze-finished/main.py
* compass-maze-finished/maze.py

(उपर्युक्त सभी संसाधन प्रोजेक्ट और स्वयंसेवक `.zip` फ़ाइलों के रूप में भी डाउनलोड किए जा सकते हैं।)

## सीखने के उद्देश्य

* Sense HAT मैग्नेटोमीटर (`get_compass()`) का उपयोग कैसे करें

इस प्रोजेक्ट में [Raspberry Pi Digital Making Curriculum](http://rpf.io/curriculum) के निम्नलिखित पहलुओं के तत्वों को शामिल किया गया है:

* [किसी समस्या को हल करने के लिए प्रोग्रामिंग संरचनाओं को जोड़े।](https://www.raspberrypi.org/curriculum/programming/builder)

## चुनौतियाँ

* "खिलाड़ी को पुरस्कृत करें" - गेम के अंत में LED पर n छवि प्रदर्शित करना;
* "अपनी खुद की भूलभुलैया बनाएँ" - अपनी खुद की भूलभुलैया बनाने के लिए भूलभुलैया शब्दकोश को संपादित करें।

\--- /collapse \---

## \--- collapse \---

## title: प्रोजेक्ट सामग्री

## प्रोजेक्ट संसाधन

* [सभी प्रोजेक्ट संसाधनों वाली .zip फ़ाइल](resources/compass-maze-project-resources.zip)
* [Compass Maze स्टार्टर प्रोजेक्ट](http://jumpto.cc/compass-go)
* [ऑफ़लाइन स्टार्टर Python फ़ाइल](resources/compass-maze-main.py)
* [ऑफ़लाइन स्टार्टर Python फ़ाइल जिसमें भूलभुलैया कोड होते हैं](resources/compass-maze-maze.py)

## क्लब लीडर संसाधन

* [सभी प्रोजेक्ट संसाधनों वाली .zip फ़ाइल](resources/compass-maze-volunteer-resources.zip)
* [ऑनलाइन पूर्ण की गई Trinket Compass Maze प्रोजेक्ट](https://trinket.io/python/0c8cdacd70)
* [compass-maze-finished/main.py](resources/compass-maze-finished-main.py)
* [compass-maze-finished/maze.py](resources/compass-maze-finished-maze.py)

\--- /collapse \---
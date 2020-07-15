# Table of Contents
### Table of Contents
### Influences
### Personal Declaration
### Acknowledgement
%# Preface
### Problem statement
### Motivation
### Methodology
#### Initial Plan
#### Tools and Technologies Used
#### Deliverables



#Influences
### Influences
+ ``_I am deliberate and afraid of nothing._"
** Audre Lorde **
+ ``_Never memorize something that you can look up._"
** Albert Einstein **
+ ``_Cogito, ergo sum_"
** René Descartes **
+ ``_That which can be asserted without evidence, can be dismissed without evidence._"
** Christopher Hitchens **
+ ``_Shut up and Calculate_ (his summary of Copenhagen's interpretation)"
** David Mermin **
# Personal Declaration
### Personal Declaration
_I attest to the fact that anything I have written in these slides is correct to the best of my memory, knowledge and understanding of mathematical time. I have tried to double check everything; reverse-engineering becasue of my lack of digital note taking habit, along the way. I hope I have not missed anything out, but if I have, I apologize for that in advance. These mistakes have arisen out of naivety and not malice. Keeping in line with the maxims of scientific method: If these mistakes are pointed out to  me, I'll take that as positive criticism and be happy to re-evaluate and work on those issues. My hope is that I am as lucid as I can be without boring anyone with this report, as I was at no point during my time at IIT Ropar, ever bored. If anything, it was not being there for the remiander of my internship after the lockdown had been reinforced that troubled me._
**Arihant Chawla**

### Acknowledgement

One must wear their influences on their shoulders; Those are for all to see and question, as much as for themselves to: See and Question. One has to go to great lengths, questioning their belief system to even go ahead and say that. It has been a long self-imposed exile, away from _Punjab Engineering College_, and it seems now to be out of my hands as to when I'll actually be physically be back in college again. When I had planned my future, as one often mawkishly does, I had not factored in a global pandemic. It was, to put it mildly, a roller coaster ride but since this presentation is only about my project undertaken from _Jan 8, 2020_ to _June 30, 2020_ at _Indian Institute of Technology, Ropar_ under the guidance of _Dr. Balwinder Sodhi_ at _Applied and and Contemporary Software Engineering (ACSE) Labs_, I would like to restrict myself to talk about only that time frame
### Acknowledgement 
During this six month period in which I had to come to terms with my own mortality vicariously, I have realized a lot of things, but chiefly this: I need to ask more questions, because it's better to ask than to assume. I would have earlier argued that it's more fun to figure out than to ask, but even figuring out needs more information, lest it runs a risk of overfitting. I am immensly thankful to Dr. Sodhi and IIT Ropar to have given me the opportunity to come back for a second round of internship, to accomodate me as per my needs, and to bear with all of my ideosyncracies. I have a curious mind, and I often let it run away far ahead, but Dr Sodhi has been an anchor, more a _buddy_ of mine than a mentor, both of which he excells at. And for that, I can not thank him enough. I would also like to thank the whole team of Applied and Contemporary Software Engineering (ACSE) Lab, IIT Ropar for hosting me not once but twice, with special thanks to Ritu Kapur, from who I learnt being more meticulous. I hope I have the good fortune of collaborating with IIT Ropar in the future.
### Acknowledgement 
I would also like to thank Agrim Dewan, my friend, batchmate and fellow intern at ACSE Lab for letting me bounce absurd ideas off of him. I would also like to do the same (in no particular order) for Vaibhav Mudgal, Kashish Mittal, Rajat Munjal, Md. Junaid Usmani, Luvkesh and Prateek for bearing with my antics outside of lab.

It is with immense pleasure that I depart from this internship and end my sabbatical away from PEC. I would like to take this glorious time as an opportunity to now devote what time I have remaining in my undergraduate degree to give back to PEC in whatever capacity I can. I hope my new found insight can be of use to the college. In line with that, I need to express my gratitude to Dr Dheeraj Sanghi: Director, PEC for his tutelage from afar. Propotionate thanks is also due to the whole of CSE Department but chiefly Dr Poonam Saini whose guidance in this was valuable to me. 

Lastly, but perhaps most importantly, I would like to thank my family: my mom and dad for always supporting me and letting me make my decisions independently even when they are glaringly bad, and my sister, Ashna for being such a halo of inspiration in my life.
# Problem statement
### Problem Statement

On my arrival at IIT Ropar on _8th January, 2020_, Dr Sodhi discussed working on **Automatic recognition of Indian License Plates**. This was keeping in line with ACSE Lab's ideology of creating contemporary software. In his office at around  12:30pm, we had discussed about the intricacies of it, it's use cases and expected timeline. Ironically, it was supposed to be completed in around two months. We could not have forseen me getting fixated on the real world application of the project and playing around with it for the entire duration of my intern. All excuses aside, it was a steep learning cruve for me as I'm genreally not a get your hands dirty with code person. I had to read up, as I was expected to about the intricacies of Optical Character Recognition. Among other things I did on 8th January, I remember looking at OCR based solutions in Tesseract, YOLOv2, and other applications of OCR, primarily in the study of Archaic languages like Roman, Greek, etc.
# Motivation
### Motivation

The motivation to do this project was pretty simple: Build an open source solution specifically trained for Indian License Plates, to make such a solution more accessible and comparable to existing market solutions. To be used in real world applications, with all the corner cases to be targeted (Different colored license plates, License Plate number extending on two line, et cetera.)
#Methodology
### Methodology
## Initial Plan
#### Initial Plan

The idea was to build upon the existing open source tools to train a layer over it to make it more specific to Indian License plates. For this we surveyed a variety of open source libraries, conducting preliminary investigation based on 
1. Reusability of code,
2. Accuracy of prediction,
3. Heuristics like no. of forks, stars, et cetera.

After this preliminary investigation (Understand-ai repository)[https://github.com/understand-ai/anonymizer] was selected, because of high detection accuracy. The original repository was basically for automatic obfuscation of faces and license plates. 

Fortunately, it had a modular structure, so we used the box detector module and built a tesseract layer over it to then conduct OCR.

Initially, the tesseract layer did not give very accurate results, especially when faced with corner cases like low resolution of plates, multi-line license plates, and colored plates. This was resolved to some degree using preprocessing tools in libraries like OpenCV, Pillow et cetera.

After resolving this, the idea was to make it compatible with the docker image of the _video to frame by frame image capture module_ Agrim was making for his project and the modular nature of my project and the fact that we were both primarily working on python, would help make it compatible.

Achieving this, we would have moved on to the webapp for the same. I had originally planned it to be in Django, PostgreSQL based system. Dr. Sodhi wanted a Java based webapp for the same as it would have better offline availability (on old subsystems than newer python based modules)

Originally, we had planned that this project would be over in a the  duration of 8-12 weeks (as per the original conversation on 8th January, 2020). Again the pandemic and the lack of productivity at home (atleast for me) was a hinderance to our plans. 

After this I had planned on completing the project I had previously worked on with Dr Sodhi, during May-July of 2019 as part of my summer intern at ACSE Lab on Bugzilla Bug reports based predictions using analysis of bugs metadata and sentiment analysis of comments of bug reports.

---

## Tools and Technologies Used
#### Tools and Technologies Used

- Python3.7
	* pytest==3.9.1
	* flake8==3.5.0
	* numpy==1.15.2
	* tensorflow-gpu==1.11.0
	* scipy==1.1.0
	* Pillow==5.3.0
	* requests==2.20.0
	* googledrivedownloader==0.3
	* tqdm==4.28.0
	* pytesseract

---

## Deliverables
#### Deliverables
I have successfully completed (or plan to for final submission of project report to IIT Ropar and PEC till, 24th July 2020) the following tasks: 

1. Written Literature Reviews of YOLOv2, Tesseract4, PILLOW based image pre processing and it's comparison with OpenCV (will be submitted in the final report, still have to type them out from handwritten notes)
2. Analyzed Multiple existing libraries and open-source tools to select one (Anonymizer-AI)[github.com/anonymizer-ai]
3. Extracted detection module from the aforementioned open source tool.
4. Created modules for preprocessing, license plate recognition using Tesseract
5. Created a scipt that returns the detedcted license plate number as a string 
6. Complete the documentation (along with illulstrations) of the repository and make a project report and presentation out of it (currently as the documentation is in markdown it won't take much effort to transpose into latex code)

Dr Sodhi was already working on the offline application for the same. He has since hosted it on (Gtungi)[https://app.gtungi.in/pahchan/]. 

---

# Future Work
### Future Work
--- 
1. I was playing around with some of the OCR features in tesseract when I realized that the number plates that are being installed in all newer cars will be of a high security registration plate (HSRP)[https://parivahan.gov.in/parivahan/en/content/high-security-registration-plates-hsrp-new-vehicle] type. And as such all non high security license plates will be obsolete in the next 10-15 years. (RC expires in 15 years).
2. Create modules for the detection of the third license plate as per the specifications in the link provided above.
 


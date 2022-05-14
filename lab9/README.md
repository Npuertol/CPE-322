# Lesson 9: YANG

**cat intrustiondetection.yang**
![catyang](/screenshots/lab9_A1_catyang.png)

**pyang -f yin -o intrusiondetection.yin intrusiondetection.yang, cat intrusiondetection.yin**
![convertthencatyin](/screenshots/lab9_A2_catyin.png)

**pyang -f uml -o intrusiondetection.uml intrusiondetection.yang --uml-no=stereotypes,annotation,typedef, cat intrusiondetection.yin**
![convertthencatuml](/screenshots/lab9_A3_catuml.png)

**sudo pip3 install -U plantuml, python3 -m plantuml intrusiondetection.uml**
![installplantuml](/screenshots/lab9_A4_plantumlinstall.png)

**View .png file using Pinta (pinta instrusiondetection.png)**
![pintapng](/screenshots/lab9_A5_pintapng.png)

**View .png using Gimp (gimp -a intrusiondetection.png)**
![gimppng](/screenshots/lab9_A6_gimppng.png)

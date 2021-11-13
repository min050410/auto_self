> ### Self Mecro
`python selenium`을 이용한 `자가진단`을 버튼 하나만 누르면 자동으로 완료가 되는 프로그램입니다.  
`pyautogui`를 이용해 비밀번호 찾기 함수를 만들었고,  
사용자 입력을 받아 `list`형식으로 `index`를 참조해 `selenium`에 적용시켰습니다.  
```python
# 비밀번호 입력 예시
list_password = list(password)
imgprefix = 'password\password_' 
imgsuffix = '.PNG'
for i in list_password:
    if(i != '\0'):
        text = pyautogui.locateOnScreen(imgprefix+i+imgsuffix, confidence=0.9)
    center = pyautogui.center(text)
    pyautogui.click(center)
    # t.sleep(1)
```
- 비밀번호 사진 예시
<div>
<img src="https://github.com/min050410/auto_self/blob/master/password/password_0.PNG?raw=true"/>
<img src="https://github.com/min050410/auto_self/blob/master/password/password_1.PNG?raw=true"/>
<img src="https://github.com/min050410/auto_self/blob/master/password/password_2.PNG?raw=true"/>
<!--<img src="https://github.com/min050410/auto_self/blob/master/password/password_3.PNG?raw=true"/>
<img src="https://github.com/min050410/auto_self/blob/master/password/password_4.PNG?raw=true"/>
<img src="https://github.com/min050410/auto_self/blob/master/password/password_5.PNG?raw=true"/>
<img src="https://github.com/min050410/auto_self/blob/master/password/password_6.PNG?raw=true"/>
<img src="https://github.com/min050410/auto_self/blob/master/password/password_7.PNG?raw=true"/>
<img src="https://github.com/min050410/auto_self/blob/master/password/password_8.PNG?raw=true"/>
<img src="https://github.com/min050410/auto_self/blob/master/password/pasword_9.PNG?raw=true"/>-->
<img src="https://github.com/min050410/auto_self/blob/master/password/enter.PNG?raw=true"/>

</div>

- 앞으로 추가할 일들
  - `tinker`를 이용해 `Desktop App` 만들기
  - 파일 모듈화 진행
  
- 구현 영상
  - <a href="https://www.youtube.com/watch?v=8awEKKuVUVw"> `v 1.0.0` </a>
  - <a href="https://www.youtube.com/watch?v=mQfeCTXfh-s"> `v 1.0.1` </a>

- Window Destop App 진행사항 보기
  - <a href="https://github.com/min050410/Tkinter_GUI/blob/master/auto_macro.py">`진행사항`</a>
  
현재 버전 `v 1.0.1`  
제작자 : <a href="https://github.com/min050410">`min050410`</a>  
감사합니다


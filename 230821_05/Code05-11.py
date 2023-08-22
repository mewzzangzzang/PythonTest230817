from tkinter import *

window = Tk()

# 메뉴 부분 구성. mainMenu : 상위 메뉴 하나만 존재하면 됩니다
mainMenu = Menu(window)

# 틀린부분 메인메뉴는 하나만 있으면 됩니다
# mainMenu2 = Menu(window)
window.config(menu = mainMenu)

# 메인메뉴의 부모 창
# window.config(menu = mainMenu2)

# 파일메뉴의 부모 창 -> 메인 메뉴
fileMenu = Menu(mainMenu)
fileMenu2 = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
# mainMenu2 ->mainMenu

fileMenu.add_command(label = "열기")
fileMenu.add_separator()
fileMenu.add_command(label = "종료")

mainMenu.add_cascade(label = "파일2", menu = fileMenu2)
fileMenu2.add_command(label = "종료2")
fileMenu2.add_command(label = "열기2")
fileMenu2.add_separator()
window.mainloop()

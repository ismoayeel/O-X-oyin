from PyQt5.QtWidgets import *


class myclass(QWidget):
    def __init__(self):
        super().__init__()

        
        self.grid_lay=QGridLayout()
        self.v_main_lay = QVBoxLayout()
        self.h_btn_lay = QHBoxLayout()

        self.btn1=QPushButton("", clicked=lambda: self.push(self.btn1))
        self.btn2=QPushButton("", clicked=lambda: self.push(self.btn2))
        self.btn3=QPushButton("", clicked=lambda: self.push(self.btn3))
        self.btn4=QPushButton("", clicked=lambda: self.push(self.btn4))
        self.btn5=QPushButton("", clicked=lambda: self.push(self.btn5))
        self.btn6=QPushButton("", clicked=lambda: self.push(self.btn6))
        self.btn7=QPushButton("", clicked=lambda: self.push(self.btn7))
        self.btn8=QPushButton("", clicked=lambda: self.push(self.btn8))
        self.btn9=QPushButton("", clicked=lambda: self.push(self.btn9))

        self.start_btn=QPushButton("Start")
        self.start_btn.clicked.connect(self.Start)

        self.finish_btn=QPushButton("Finish")
        self.finish_btn.hide()
        self.finish_btn.clicked.connect(self.Finish)

        self.exit_btn=QPushButton("Exit", clicked=lambda: exit())

        self.h_btn_lay.addWidget(self.start_btn)
        self.h_btn_lay.addWidget(self.finish_btn)
        self.h_btn_lay.addWidget(self.exit_btn)

        self.lst=[self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]

        index = 0

        for i in range(3):
            for j in range(3):
                self.lst[index].setFixedSize(50,50)
                self.lst[index].setStyleSheet("font-size:20px;background:grey")
                self.lst[index].setEnabled(False)
                self.grid_lay.addWidget(self.lst[index],i,j)
                index+=1

        self.v_main_lay.addLayout(self.grid_lay)
        self.v_main_lay.addLayout(self.h_btn_lay)

        self.setLayout(self.v_main_lay)

        self.counter=1

    def push(self, btn):

        if self.counter%2==1:
            if btn.text() == "":
                btn.setText("X")
                self.counter+=1
        else:
            if btn.text() == "":
                btn.setText("O")
                self.counter+=1


        if (self.btn1.text() == "X" and self.btn2.text() == "X" and self.btn3.text() == "X") or (self.btn1.text() == "O" and self.btn2.text() == "O" and self.btn3.text() == "O"):
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText(f"{self.btn1.text()} yutdi")
            self.msg.exec_()

            self.counter=1

            self.btn1.setText("")
            self.btn2.setText("")
            self.btn3.setText("")
            self.btn4.setText("")
            self.btn5.setText("")
            self.btn6.setText("")
            self.btn7.setText("")
            self.btn8.setText("")
            self.btn9.setText("")

        elif (self.btn4.text() == "X" and self.btn5.text() == "X" and self.btn6.text() == "X") or (self.btn4.text() == "O" and self.btn5.text() == "O" and self.btn6.text() == "O"):
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText(f"{self.btn4.text()} yutdi")
            self.msg.exec_()

            self.counter=1

            self.btn1.setText("")
            self.btn2.setText("")
            self.btn3.setText("")
            self.btn4.setText("")
            self.btn5.setText("")
            self.btn6.setText("")
            self.btn7.setText("")
            self.btn8.setText("")
            self.btn9.setText("")

        elif (self.btn7.text() == "X" and self.btn8.text() == "X" and self.btn9.text() == "X") or (self.btn7.text() == "O" and self.btn8.text() == "O" and self.btn9.text() == "O"):
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText(f"{self.btn7.text()} yutdi")
            self.msg.exec_()

            self.counter=1

            self.btn1.setText("")
            self.btn2.setText("")
            self.btn3.setText("")
            self.btn4.setText("")
            self.btn5.setText("")
            self.btn6.setText("")
            self.btn7.setText("")
            self.btn8.setText("")
            self.btn9.setText("")
            
        elif (self.btn1.text() == "X" and self.btn4.text() == "X" and self.btn7.text() == "X") or (self.btn1.text() == "O" and self.btn4.text() == "O" and self.btn7.text() == "O"):
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText(f"{self.btn1.text()} yutdi")
            self.msg.exec_()

            self.counter=1

            self.btn1.setText("")
            self.btn2.setText("")
            self.btn3.setText("")
            self.btn4.setText("")
            self.btn5.setText("")
            self.btn6.setText("")
            self.btn7.setText("")
            self.btn8.setText("")
            self.btn9.setText("")
            
        elif (self.btn2.text() == "X" and self.btn5.text() == "X" and self.btn8.text() == "X") or (self.btn2.text() == "O" and self.btn5.text() == "O" and self.btn8.text() == "O"):
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText(f"{self.btn2.text()} yutdi")
            self.msg.exec_()

            self.counter=1

            self.btn1.setText("")
            self.btn2.setText("")
            self.btn3.setText("")
            self.btn4.setText("")
            self.btn5.setText("")
            self.btn6.setText("")
            self.btn7.setText("")
            self.btn8.setText("")
            self.btn9.setText("")
            
        elif (self.btn3.text() == "X" and self.btn6.text() == "X" and self.btn9.text() == "X") or (self.btn3.text() == "O" and self.btn6.text() == "O" and self.btn9.text() == "O"):
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText(f"{self.btn3.text()} yutdi")
            self.msg.exec_()

            self.counter=1

            self.btn1.setText("")
            self.btn2.setText("")
            self.btn3.setText("")
            self.btn4.setText("")
            self.btn5.setText("")
            self.btn6.setText("")
            self.btn7.setText("")
            self.btn8.setText("")
            self.btn9.setText("")
            
        elif (self.btn1.text() == "X" and self.btn5.text() == "X" and self.btn9.text() == "X") or (self.btn1.text() == "O" and self.btn5.text() == "O" and self.btn9.text() == "O"):
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText(f"{self.btn1.text()} yutdi")
            self.msg.exec_()

            self.counter=1

            self.btn1.setText("")
            self.btn2.setText("")
            self.btn3.setText("")
            self.btn4.setText("")
            self.btn5.setText("")
            self.btn6.setText("")
            self.btn7.setText("")
            self.btn8.setText("")
            self.btn9.setText("")
            
        elif (self.btn3.text() == "X" and self.btn5.text() == "X" and self.btn7.text() == "X") or (self.btn3.text() == "O" and self.btn5.text() == "O" and self.btn7.text() == "O"):
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText(f"{self.btn3.text()} yutdi")
            self.msg.exec_()

            self.counter=1

            self.btn1.setText("")
            self.btn2.setText("")
            self.btn3.setText("")
            self.btn4.setText("")
            self.btn5.setText("")
            self.btn6.setText("")
            self.btn7.setText("")
            self.btn8.setText("")
            self.btn9.setText("")
            

    def Start(self):
        self.btn1.setText("")
        self.btn2.setText("")
        self.btn3.setText("")
        self.btn4.setText("")
        self.btn5.setText("")
        self.btn6.setText("")
        self.btn7.setText("")
        self.btn8.setText("")
        self.btn9.setText("")

        self.finish_btn.show()
        self.start_btn.hide()
        for index, btn in enumerate(self.lst):
            btn.setEnabled(True)

    def Finish(self):
        self.finish_btn.hide()
        self.start_btn.show()
        
        self.btn1.setText("")
        self.btn2.setText("")
        self.btn3.setText("")
        self.btn4.setText("")
        self.btn5.setText("")
        self.btn6.setText("")
        self.btn7.setText("")
        self.btn8.setText("")
        self.btn9.setText("")

        for index, btn in enumerate(self.lst):
            btn.setEnabled(False)

app=QApplication([])
win=myclass()
win.show()
app.exec_()

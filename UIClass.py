

import speech
import speechFunctions

from time import strftime

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTime


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1002, 495)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_btn = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_btn.setGeometry(QtCore.QRect(410, 160, 171, 70))
        self.pushButton_btn.setObjectName("pushButton_btn")
        self.pushButton_btn.clicked.connect(self.inputSpeech)# When user pushes the talk button
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(660, 60, 331, 201))
        self.groupBox.setObjectName("groupBox")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 20, 312, 173))
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setObjectName("calendarWidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(660, 270, 331, 191))
        self.groupBox_2.setObjectName("groupBox_2")
        self.todaysEvents_text = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.todaysEvents_text.setGeometry(QtCore.QRect(10, 28, 311, 151))
        self.todaysEvents_text.setObjectName("todaysEvents_text")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 160, 321, 191))
        self.groupBox_3.setObjectName("groupBox_3")
        self.news_txt = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.news_txt.setGeometry(QtCore.QRect(10, 30, 301, 151))
        self.news_txt.setObjectName("news_txt")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 360, 321, 101))
        self.groupBox_4.setObjectName("groupBox_4")
        self.jokes_text = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.jokes_text.setGeometry(QtCore.QRect(10, 28, 301, 61))
        self.jokes_text.setObjectName("jokes_text")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 70, 321, 80))
        self.groupBox_5.setObjectName("groupBox_5")
        self.weather_text = QtWidgets.QPlainTextEdit(self.groupBox_5)
        self.weather_text.setGeometry(QtCore.QRect(10, 30, 301, 41))
        self.weather_text.setObjectName("weather_text")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 20, 331, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(780, 30, 91, 16))
        self.time.setObjectName("time")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(350, 270, 291, 191))
        self.groupBox_6.setObjectName("groupBox_6")
        self.help_text = QtWidgets.QPlainTextEdit(self.groupBox_6)
        self.help_text.setGeometry(QtCore.QRect(10, 30, 271, 151))
        self.help_text.setObjectName("help_text")
        self.wallpaper = QtWidgets.QLabel(self.centralwidget)
        self.wallpaper.setGeometry(QtCore.QRect(0, 0, 1000, 470))
        self.wallpaper.setText("")
        self.wallpaper.setObjectName("wallpaper")
        self.wallpaper.raise_()
        self.pushButton_btn.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.groupBox_4.raise_()
        self.groupBox_5.raise_()
        self.label.raise_()
        self.time.raise_()
        self.groupBox_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        #UI Function calls
        speechFunctions.speechFunctions.jokes(self,False)
        speechFunctions.speechFunctions.googleNews(self, False)
        speechFunctions.speechFunctions.weather(self, False)
        speechFunctions.speechFunctions.help(self, False)
        speechFunctions.speechFunctions.agenda(self,False)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_btn.setText(_translate("MainWindow", "Push to talk"))
        self.groupBox.setTitle(_translate("MainWindow", "Calendar"))
        self.groupBox_2.setTitle(_translate("MainWindow", "List of Events today"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Google News"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Jokes"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Weather"))
        self.label.setText(_translate("MainWindow", "Welcome to the personal assistant program, please use the push to talk button to get started."))
        self.time.setText(_translate("MainWindow", "12:00:00"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Help"))

    def inputSpeech(self): # The function that is called when the button is pushed
        s = speech.speech
        execute = speechFunctions.speechFunctions

        s.AIResponse("What can I do for you today?")
        command = speech.speech.myCommand(self)
        if 'hello' in command:
            day_time = int(strftime('%H'))
            if day_time < 12:
                s.AIResponse('Hello Sir. Good morning')
            elif 12 <= day_time < 18:
                s.AIResponse('Hello Sir. Good afternoon')
            else:
               s.AIResponse('Hello Sir. Good evening')
        # Checking for keywords in the command function
        elif 'open' in command:
            execute.openWebpage(self, command)
        elif 'joke' in command:
            execute.jokes(self, True)
        elif 'news' in command:
            execute.googleNews(self, True)
        elif 'weather' in command:
            execute.weather(self, True)
        elif 'time' in command:
            execute.time(self)
        elif 'launch' in command:
            execute.launch(self, command)
        elif 'play a song' in command:
            execute.playSong(self)
        elif 'change wallpaper' in command:
            execute.changeWallpaper(self)
        elif 'tell me about' in command:
            execute.wikiSearch(self, command)
        elif 'agenda' in command:
            execute.agenda(self, True)
        elif 'help me' in command:
            execute.help(self, True)
        else:
            s.AIResponse("I did not catch that.") # If the keyword was not said or not understood

    # Clock function that gets called every second
    def clock(self):
        currentTime = QTime.currentTime()
        text = currentTime.toString('hh:mm:ss')
        self.time.setText(text)



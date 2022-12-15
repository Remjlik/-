from neoBase import obj_lst, like_object, unlike_object, clean_likes
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3 as sq
from collections import Counter
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

selected_sights_list = []
selected_category_list = []


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 800)
        self.setWindowTitle("Гид по городу Минск")
        self.setMaximumSize(600, 800)
        self.setStyleSheet("background-color: #22222e; color: wight")
        self.central_widget = QStackedWidget(self)
        login_widget = Page1()
        self.central_widget.addWidget(login_widget)
        self.setCentralWidget(self.central_widget)
        login_widget.pushButton.clicked.connect(self.check)
        clean_likes()

    def page_1(self):    
        login_widget = Page1()
        self.central_widget.addWidget(login_widget)
        self.central_widget.setCurrentWidget(login_widget)
        btn = login_widget.pushButton.clicked.connect(self.check)
        if bool(btn) == True:
            selected_category_list.clear()

    def page_2(self):
        logged_in_widget = Page2()
        self.central_widget.addWidget(logged_in_widget)
        self.central_widget.setCurrentWidget(logged_in_widget)
        logged_in_widget.button_2b.clicked.connect(self.page_1)
        btn = logged_in_widget.button_2n.clicked.connect(self.page_4)
        if bool(btn) == True:
            selected_sights_list.clear()

    def page_3(self):
        try:
            login_widget = Page3(text1)
            self.central_widget.addWidget(login_widget)
            self.central_widget.setCurrentWidget(login_widget)
            login_widget.button_3b.clicked.connect(self.page_1)
        except:
            pass

    def page_4(self):
        login_widget = Page4()
        self.central_widget.addWidget(login_widget)
        self.central_widget.setCurrentWidget(login_widget)
        login_widget.button_3b.clicked.connect(self.page_2)

    def check(self):
        if selected_category_list:
            self.page_2()
        else:
            self.page_3()
     



class Page1(QWidget):
    def change(self):
        get_database_name(self.comboBox.currentText())
    
    def __init__(self):
        super().__init__()
        self.resize(600, 800)
        self.setStyleSheet("background-color: #22222e;")

        self.name = QLabel(self)
        self.name.setText("Поиск достопримечательностей")
        self.name.setGeometry(QtCore.QRect(0, 0, 600, 80))
        self.name.setStyleSheet("color: rgb(181, 181, 181);\n""font-size: 40px;\n""padding-left: 0px;")

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(0, 100, 600, 70))
        self.comboBox.setStyleSheet(
            "background-color: rgb(0,0,0);\n""color: rgb(181, 181, 181);\n""padding: 4px;\n""font-size: 30px;\n")
        self.comboBox.setEditable(True)
        self.comboBox.activated.connect(self.change)

        self.comboBox.addItem("")
        for i in obj_lst:
            self.comboBox.addItem(i)

        self.genre = QLabel(self)
        self.genre.setText("Категории:")
        self.genre.setGeometry(QtCore.QRect(0, 200, 500, 80))
        self.genre.setStyleSheet("color: rgb(181, 181, 181);\n""font-size: 40px;\n""padding-left: 200px;")

        self.pushButton = QtWidgets.QPushButton("Далее", self)
        self.pushButton.setGeometry(QtCore.QRect(270, 700, 320, 80))

        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
            "background-color: #808080;\n""border: 2px solid #f66867;\n""border-radius: 40px;\n""color: white")

        self.checkBox_9 = QtWidgets.QCheckBox(" Для Детей", self)
        self.checkBox_9.setGeometry(QtCore.QRect(10, 700, 250, 80))
        font.setPointSize(23)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setStyleSheet(
            "background-color: #9ACD32; border: 2px solid #f66867; border-radius: 40px; color: white")

        self.checkBox_8 = QtWidgets.QCheckBox(" Общепит", self)
        self.checkBox_8.setGeometry(QtCore.QRect(340, 600, 250, 80))
        font.setPointSize(26)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setStyleSheet(
            "background-color: #DC143C;\n""border: 2px solid #f66867;\n""border-radius: 40px;\n""color: white")

        self.checkBox_7 = QtWidgets.QCheckBox(" Природные", self)
        self.checkBox_7.setGeometry(QtCore.QRect(10, 600, 320, 80))
        font.setPointSize(27)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setStyleSheet(
            "background-color: #5F9EA0;\n""border: 2px solid #f66867;\n""border-radius: 40px;\n""color: white")

        self.checkBox_6 = QtWidgets.QCheckBox(" Архитектурные", self)
        self.checkBox_6.setGeometry(QtCore.QRect(259, 500, 330, 80))
        font.setPointSize(21)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setStyleSheet(
            "background-color:#808000;\n""border: 2px solid #f66867;\n""border-radius: 40px;\n""color: white")

        self.checkBox_5 = QtWidgets.QCheckBox(" Исторические", self)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 500, 240, 80))
        font.setPointSize(17)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setStyleSheet(
            "background-color: #191970;\n""border: 2px solid #f66867;\n""border-radius: 40px;\n""color: white")

        self.checkBox_4 = QtWidgets.QCheckBox(" Религиозные", self)
        self.checkBox_4.setGeometry(QtCore.QRect(420, 400, 170, 80))
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setStyleSheet(
            "background-color: #8B008B;\n""border: 2px solid #f66867;\n""border-radius: 40px;\n""color: white")

        self.checkBox_3 = QtWidgets.QCheckBox(" Развлекательные", self)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 400, 400, 80))
        font.setPointSize(23)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setStyleSheet(
            "background-color: #FFA500;\n""border: 2px solid #f66867;\n""border-radius: 40px;\n""color: white")

        self.checkBox_2 = QtWidgets.QCheckBox(" Культурные", self)
        self.checkBox_2.setGeometry(QtCore.QRect(360, 300, 230, 80))
        font.setPointSize(18)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet(
            "background-color: #008B8B;\n""border: 2px solid #f66867;\n""border-radius: 40px;\n""color: white")

        self.checkBox_1 = QtWidgets.QCheckBox(" Военно Патриотические", self)
        self.checkBox_1.setGeometry(QtCore.QRect(10, 300, 340, 80))
        font.setPointSize(15)
        self.checkBox_1.setFont(font)
        self.checkBox_1.setStyleSheet(
            "background-color: #B22222; border: 2px solid #f66867; border-radius: 40px; color: white; ")
        self.checkBox_1.stateChanged.connect(
            lambda state=self.checkBox_1.isChecked(), style=self.checkBox_1.styleSheet(),
                   text=self.checkBox_1.text().replace(" ", ""): self.selected(state, style, self.checkBox_1, text))
        self.checkBox_2.stateChanged.connect(
            lambda state=self.checkBox_2.isChecked(), style=self.checkBox_2.styleSheet(),
                   text=self.checkBox_2.text().replace(" ", ""): self.selected(state, style, self.checkBox_2, text))
        self.checkBox_3.stateChanged.connect(
            lambda state=self.checkBox_3.isChecked(), style=self.checkBox_3.styleSheet(),
                   text=self.checkBox_3.text().replace(" ", ""): self.selected(state, style, self.checkBox_3, text))
        self.checkBox_4.stateChanged.connect(
            lambda state=self.checkBox_4.isChecked(), style=self.checkBox_4.styleSheet(),
                   text=self.checkBox_4.text().replace(" ", ""): self.selected(state, style, self.checkBox_4, text))
        self.checkBox_5.stateChanged.connect(
            lambda state=self.checkBox_5.isChecked(), style=self.checkBox_5.styleSheet(),
                   text=self.checkBox_5.text().replace(" ", ""): self.selected(state, style, self.checkBox_5, text))
        self.checkBox_6.stateChanged.connect(
            lambda state=self.checkBox_6.isChecked(), style=self.checkBox_6.styleSheet(),
                   text=self.checkBox_6.text().replace(" ", ""): self.selected(state, style, self.checkBox_6, text))
        self.checkBox_7.stateChanged.connect(
            lambda state=self.checkBox_7.isChecked(), style=self.checkBox_7.styleSheet(),
                   text=self.checkBox_7.text().replace(" ", ""): self.selected(state, style, self.checkBox_7, text))
        self.checkBox_8.stateChanged.connect(
            lambda state=self.checkBox_8.isChecked(), style=self.checkBox_8.styleSheet(),
                   text=self.checkBox_8.text().replace(" ", ""): self.selected(state, style, self.checkBox_8, text))
        self.checkBox_9.stateChanged.connect(
            lambda state=self.checkBox_9.isChecked(), style=self.checkBox_9.styleSheet(),
                   text=self.checkBox_9.text().replace(" ", ""): self.selected(state, style, self.checkBox_9, text))

    def selected(self, state, style, name, text):
        if state == QtCore.Qt.Checked:
            name.setStyleSheet(
                "background-color: #808080; border: 2px solid #f66867; border-radius: 40px; color: black; ")
            if text not in selected_category_list: selected_category_list.append(text)
        else:
            name.setStyleSheet(style)
            selected_category_list.remove(text)
        global selected_category
        selected_category = str(selected_category_list).replace("[", "").replace("]", "")
        


class Page2(QWidget):
    def __init__(self):
        clean_likes()
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        super().__init__()
        self.scroll_ = QScrollArea()
        self.widget_layout = QVBoxLayout()
        chooseText = QLabel("Выберите интересующие вас места:")
        chooseText.setStyleSheet("color: #C0C0C0;")
        br = QLabel("<hr>")
        br.setOpenExternalLinks(True)
        chooseText.setFont(font)
        self.widget_layout.addWidget(chooseText)
        self.widget_layout.addWidget(br)
        font.setPointSize(12)
        x, y = get_database()
        for i, j in zip(x, y):
            self.objectIN = QtWidgets.QCheckBox(i)
            self.objectIN.setFont(font)
            self.objectIN.setStyleSheet("color: #C0C0C0;")
            self.widget_layout.addWidget(self.objectIN)
            self.pixmap = QPixmap()
            self.pixmap.loadFromData(QByteArray(j))
            lbl = QLabel(self)
            lbl.setMaximumSize(550, 400)
            lbl.setPixmap(self.pixmap)
            self.widget_layout.addWidget(lbl)
            self.objectIN.stateChanged.connect(
                lambda state=self.objectIN.isChecked(), name=self.objectIN.text(), colorC = self.objectIN: self.selectBooks(state, name, colorC))
        self.just_widget = QWidget()
        self.just_widget.setLayout(self.widget_layout)
        self.scroll_.setWidget(self.just_widget)
        self.scroll_.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setMinimumSize(600, 800)
        self.setMaximumSize(600, 800)
        self.blayout = QVBoxLayout()
        self.button_2b = QPushButton("Назад")
        self.button_2b.setStyleSheet(
            "background-color: #808080;\n""border: 2px solid #f66867;\n""border-radius: 40px;\n""color: white")
        self.button_2b.setFont(font)
        self.button_2n = QPushButton("Далее")
        self.button_2n.setFont(font)
        self.button_2n.setStyleSheet(
            "background-color: #808080;\n""border: 2px solid #f66867;\n""border-radius: 40px;\n""color: white")
        self.blayout.addWidget(self.scroll_)
        self.blayout.addWidget(self.button_2n)
        self.blayout.addWidget(self.button_2b)
        self.setLayout(self.blayout)

    def selectBooks(self, state, name, color):
        if state == QtCore.Qt.Checked:
            color.setStyleSheet("color: #F5DEB5")
            if name not in selected_sights_list:
                selected_sights_list.append(name)
                like_object(name)
        else:
            color.setStyleSheet("color: #C0C0C0;")
            selected_sights_list.remove(name)
            unlike_object(name)
        print(selected_sights_list)
        # for i in selected_sights_list:
        #     print(i)
        #     like_object(i)




class Page3(QWidget):
    def __init__(self, info):
        super().__init__()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.setMinimumSize(600, 800)
        self.setMaximumSize(600, 800)
        self.widget_layout = QVBoxLayout()
        for i in info:
            objectIN = QLabel(i)
            objectIN.setFont(font)
            objectIN.setStyleSheet("color: #C0C0C0;")
            self.widget_layout.addWidget(objectIN)
            self.pixmap = QPixmap()
            self.pixmap.loadFromData(QByteArray(png))
            lbl = QLabel()
            lbl.setMaximumSize(550, 400)
            lbl.setPixmap(self.pixmap)
            self.widget_layout.addWidget(lbl)
            description = QLabel()
            description.setMaximumWidth(550)
            description.setText(text2)
            description.setStyleSheet("color: #C0C0C0; font-size: 20px")
            description.setWordWrap(True)
            link = QLabel()
            link.setOpenExternalLinks(True)
            link.setStyleSheet("color: #C0C0C0; font-size: 20px")
            link.setText(f"<a href= '{maps}'>Смотреть на карте</a>")
            self.widget_layout.addWidget(description)
            self.widget_layout.addWidget(link) 

        self.just_widget = QWidget()
        self.just_widget.setLayout(self.widget_layout)
        self.scroll_ = QScrollArea()
        self.scroll_.setMaximumSize(600, 800)
        self.scroll_.setWidget(self.just_widget)
        self.scroll_.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.blayout = QVBoxLayout()
        self.button_3b = QPushButton("Назад")
        self.button_3b.setStyleSheet(
            "background-color: #808080;\n""border: 2px solid #f66867;\n""border-radius: 40px;\n""color: white")
        self.button_3b.setFont(font)
        self.blayout.addWidget(self.scroll_)
        self.blayout.addWidget(self.button_3b)
        self.setLayout(self.blayout)

class Page4(QWidget):
    def __init__(self):
        super().__init__()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.setMinimumSize(600, 800)
        self.setMaximumSize(600, 800)
        self.widget_layout = QVBoxLayout()
        for i in selected_sights_list:
            a = get_database_name(i)
            objectIN = QLabel(i)
            objectIN.setFont(font)
            objectIN.setStyleSheet("color: #C0C0C0;")
            self.widget_layout.addWidget(objectIN)
            self.pixmap = QPixmap()
            self.pixmap.loadFromData(QByteArray(a))
            lbl = QLabel()
            lbl.setMaximumSize(550, 400)
            lbl.setPixmap(self.pixmap)
            self.widget_layout.addWidget(lbl)
            description = QLabel()
            description.setMaximumWidth(550)
            description.setText(text2)
            description.setStyleSheet("color: #C0C0C0; font-size: 20px")
            description.setWordWrap(True)
            link = QLabel()
            link.setOpenExternalLinks(True)
            link.setStyleSheet("color: #C0C0C0; font-size: 20px")
            link.setText(f"<a href= '{maps}'>Смотреть на карте</a>")
            self.widget_layout.addWidget(description) 
            self.widget_layout.addWidget(link) 
        self.just_widget = QWidget()
        self.just_widget.setLayout(self.widget_layout)
        self.scroll_ = QScrollArea()
        self.scroll_.setMaximumSize(600, 800)
        self.scroll_.setWidget(self.just_widget)
        self.scroll_.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.blayout = QVBoxLayout()
        self.button_3b = QPushButton("Назад")
        self.button_3b.setStyleSheet(
            "background-color: #808080;\n""border: 2px solid #f66867;\n""border-radius: 40px;\n""color: white")
        self.button_3b.setFont(font)
        self.blayout.addWidget(self.scroll_)
        self.blayout.addWidget(self.button_3b)
        self.setLayout(self.blayout)




def get_database():
    with sq.connect("Data.db") as db:
        cur = db.cursor()
        cur.execute(f'SELECT name, png FROM Data WHERE genre in ({selected_category})')
        result = cur.fetchall()
        recommendation = []
        png = []
        recText = []
        for i in result:
            for j in i:
                if j != None:
                    recommendation.append(j)
        seriated_recommendation = [k for k, v in Counter(recommendation).items() if v > 1]
        recommendation = list(set(recommendation))
        for i in seriated_recommendation: recommendation.remove(i)
        recommendation = seriated_recommendation + recommendation
        for i in recommendation:
            if isinstance(i, str):
                recText.append(i)
        for i in recText:
            cur.execute(f'SELECT png FROM Data WHERE name like "{i}"')
            result = cur.fetchone()
            png.append(result[0])
        
        return recText, png 
        
def get_database_name(a):
    try:
        with sq.connect("Data.db") as db:
            cur = db.cursor()
            cur.execute(f'SELECT name, description, png, route, maps FROM Data WHERE name = "{a}"')
            result = cur.fetchall()
            result = list(result[0])
            global text1, text2, png, maps
            text1 = result[:1]; text2 = result[1]
            png, route, maps = result[2], result[3], result[4]
            text2 = text2 + "\n\nКак добраться:\n"  +  route
            return png
    except: pass
        

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("QCheckBox::indicator {width:  0px; height: 0px;}")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

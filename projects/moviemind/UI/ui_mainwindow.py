# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import QCursor, QFont
from PySide6.QtWidgets import (QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QMenuBar,
                               QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
                               QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, system):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 793)
        self.system = system
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(950, 741))
        self.centralwidget.setStyleSheet(u"background-color:rgb(255, 250, 232);\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.leftWidget = QWidget(self.centralwidget)
        self.leftWidget.setObjectName(u"leftWidget")
        self.leftWidget.setMaximumSize(QSize(179, 707))
        self.gridLayout = QGridLayout(self.leftWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(40, 0, 20, 0)
        self.label = QLabel(self.leftWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(120, 40))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(65, 168, 99);")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.gridLayout.setRowStretch(1, 1)


        self.horizontalLayout_3.addWidget(self.leftWidget)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.rightWidget = QWidget(self.centralwidget)
        self.rightWidget.setObjectName(u"rightWidget")
        self.rightWidget.setMaximumSize(QSize(11111, 11111))
        self.verticalLayout = QVBoxLayout(self.rightWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.verticalWidget_8 = QWidget(self.rightWidget)
        self.verticalWidget_8.setObjectName(u"verticalWidget_8")
        self.verticalLayout_8 = QVBoxLayout(self.verticalWidget_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.verticalWidget_8)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setStyleSheet(u"color: rgb(65, 168, 99);")

        self.verticalLayout_8.addWidget(self.label_8)

        self.gridWidget_2 = QWidget(self.verticalWidget_8)
        self.gridWidget_2.setObjectName(u"gridWidget_2")
        self.gridLayout_2 = QGridLayout(self.gridWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalWidget_2 = QWidget(self.gridWidget_2)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        self.verticalLayout_2 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.verticalWidget_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_9 = QVBoxLayout(self.widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pushButton_m1 = QFrame(self.widget)
        self.pushButton_m1.setObjectName(u"pushButton_m1")
        sizePolicy1.setHeightForWidth(self.pushButton_m1.sizePolicy().hasHeightForWidth())
        self.pushButton_m1.setSizePolicy(sizePolicy1)
        self.pushButton_m1.setMinimumSize(QSize(135, 200))
        self.pushButton_m1.setMaximumSize(QSize(135, 200))
        self.pushButton_m1.setStyleSheet(u"border:2px solid rgb(216, 202, 158);")

        self.verticalLayout_9.addWidget(self.pushButton_m1)

        self.label_m1 = QLabel(self.widget)
        self.label_m1.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_m1.sizePolicy().hasHeightForWidth())
        self.label_m1.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Microsoft Tai Le"])
        self.label_m1.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_m1)


        self.verticalLayout_2.addWidget(self.widget)

        self.verticalWidget_5 = QWidget(self.verticalWidget_2)
        self.verticalWidget_5.setObjectName(u"verticalWidget_5")
        self.verticalLayout_5 = QVBoxLayout(self.verticalWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_m5 = QFrame(self.verticalWidget_5)
        self.pushButton_m5.setObjectName(u"pushButton_m5")
        self.pushButton_m5.setMinimumSize(QSize(135, 200))
        self.pushButton_m5.setMaximumSize(QSize(135, 200))
        self.pushButton_m5.setStyleSheet(u"border:2px solid rgb(216, 202, 158);")

        self.verticalLayout_5.addWidget(self.pushButton_m5)

        self.label_m5 = QLabel(self.verticalWidget_5)
        self.label_m5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_m5.sizePolicy().hasHeightForWidth())
        self.label_m5.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.label_m5)


        self.verticalLayout_2.addWidget(self.verticalWidget_5)


        self.gridLayout_2.addWidget(self.verticalWidget_2, 0, 0, 1, 1)

        self.verticalWidget_3 = QWidget(self.gridWidget_2)
        self.verticalWidget_3.setObjectName(u"verticalWidget_3")
        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_2 = QWidget(self.verticalWidget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_10 = QVBoxLayout(self.widget_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pushButton_m2 = QFrame(self.widget_2)
        self.pushButton_m2.setObjectName(u"pushButton_m2")
        self.pushButton_m2.setMinimumSize(QSize(135, 200))
        self.pushButton_m2.setMaximumSize(QSize(135, 200))
        self.pushButton_m2.setStyleSheet(u"border:2px solid rgb(216, 202, 158);")

        self.verticalLayout_10.addWidget(self.pushButton_m2)

        self.label_m2 = QLabel(self.widget_2)
        self.label_m2.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_m2.sizePolicy().hasHeightForWidth())
        self.label_m2.setSizePolicy(sizePolicy)

        self.verticalLayout_10.addWidget(self.label_m2)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.verticalWidget_6 = QWidget(self.verticalWidget_3)
        self.verticalWidget_6.setObjectName(u"verticalWidget_6")
        self.verticalLayout_6 = QVBoxLayout(self.verticalWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_m6 = QFrame(self.verticalWidget_6)
        self.pushButton_m6.setObjectName(u"pushButton_m6")
        self.pushButton_m6.setMinimumSize(QSize(135, 200))
        self.pushButton_m6.setMaximumSize(QSize(135, 200))
        self.pushButton_m6.setStyleSheet(u"border:2px solid rgb(216, 202, 158);")

        self.verticalLayout_6.addWidget(self.pushButton_m6)

        self.label_m6 = QLabel(self.verticalWidget_6)
        self.label_m6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_m6.sizePolicy().hasHeightForWidth())
        self.label_m6.setSizePolicy(sizePolicy)

        self.verticalLayout_6.addWidget(self.label_m6)


        self.verticalLayout_3.addWidget(self.verticalWidget_6)


        self.gridLayout_2.addWidget(self.verticalWidget_3, 0, 1, 1, 1)

        self.verticalWidget_4 = QWidget(self.gridWidget_2)
        self.verticalWidget_4.setObjectName(u"verticalWidget_4")
        self.verticalLayout_4 = QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_3 = QWidget(self.verticalWidget_4)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.pushButton_m3 = QFrame(self.widget_3)
        self.pushButton_m3.setObjectName(u"pushButton_m3")
        self.pushButton_m3.setMinimumSize(QSize(135, 200))
        self.pushButton_m3.setMaximumSize(QSize(135, 200))
        self.pushButton_m3.setStyleSheet(u"border:2px solid rgb(216, 202, 158);")

        self.verticalLayout_11.addWidget(self.pushButton_m3)

        self.label_m3 = QLabel(self.widget_3)
        self.label_m3.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_m3.sizePolicy().hasHeightForWidth())
        self.label_m3.setSizePolicy(sizePolicy)

        self.verticalLayout_11.addWidget(self.label_m3)


        self.verticalLayout_4.addWidget(self.widget_3)

        self.verticalWidget_7 = QWidget(self.verticalWidget_4)
        self.verticalWidget_7.setObjectName(u"verticalWidget_7")
        self.verticalLayout_7 = QVBoxLayout(self.verticalWidget_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_m7 = QFrame(self.verticalWidget_7)
        self.pushButton_m7.setObjectName(u"pushButton_m7")
        self.pushButton_m7.setMinimumSize(QSize(135, 200))
        self.pushButton_m7.setMaximumSize(QSize(135, 200))
        self.pushButton_m7.setStyleSheet(u"border:2px solid rgb(216, 202, 158);")

        self.verticalLayout_7.addWidget(self.pushButton_m7)

        self.label_m7 = QLabel(self.verticalWidget_7)
        self.label_m7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_m7.sizePolicy().hasHeightForWidth())
        self.label_m7.setSizePolicy(sizePolicy)

        self.verticalLayout_7.addWidget(self.label_m7)


        self.verticalLayout_4.addWidget(self.verticalWidget_7)


        self.gridLayout_2.addWidget(self.verticalWidget_4, 0, 2, 1, 1)

        self.verticalWidget = QWidget(self.gridWidget_2)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalLayout_12 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(9, 9, 9, 9)
        self.verticalWidget_21 = QWidget(self.verticalWidget)
        self.verticalWidget_21.setObjectName(u"verticalWidget_21")
        self.verticalLayout_13 = QVBoxLayout(self.verticalWidget_21)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(9, 9, 9, 9)
        self.pushButton_m4 = QFrame(self.verticalWidget_21)
        self.pushButton_m4.setObjectName(u"pushButton_m4")
        self.pushButton_m4.setMinimumSize(QSize(135, 200))
        self.pushButton_m4.setMaximumSize(QSize(135, 200))
        self.pushButton_m4.setStyleSheet(u"border:2px solid rgb(216, 202, 158);")

        self.verticalLayout_13.addWidget(self.pushButton_m4)

        self.label_m4 = QLabel(self.verticalWidget_21)
        self.label_m4.setObjectName(u"label_m4")
        sizePolicy.setHeightForWidth(self.label_m4.sizePolicy().hasHeightForWidth())
        self.label_m4.setSizePolicy(sizePolicy)

        self.verticalLayout_13.addWidget(self.label_m4)


        self.verticalLayout_12.addWidget(self.verticalWidget_21)

        self.verticalWidget_31 = QWidget(self.verticalWidget)
        self.verticalWidget_31.setObjectName(u"verticalWidget_31")
        self.verticalLayout_14 = QVBoxLayout(self.verticalWidget_31)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(9, 9, 9, 9)
        self.pushButton_m8 = QFrame(self.verticalWidget_31)
        self.pushButton_m8.setObjectName(u"pushButton_m8")
        self.pushButton_m8.setMinimumSize(QSize(135, 200))
        self.pushButton_m8.setMaximumSize(QSize(135, 200))
        self.pushButton_m8.setStyleSheet(u"border:2px solid rgb(216, 202, 158);")

        self.verticalLayout_14.addWidget(self.pushButton_m8)

        self.label_m8 = QLabel(self.verticalWidget_31)
        self.label_m8.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_m8.sizePolicy().hasHeightForWidth())
        self.label_m8.setSizePolicy(sizePolicy)

        self.verticalLayout_14.addWidget(self.label_m8)


        self.verticalLayout_12.addWidget(self.verticalWidget_31)


        self.gridLayout_2.addWidget(self.verticalWidget, 0, 3, 1, 1)


        self.verticalLayout_8.addWidget(self.gridWidget_2)

        self.horizontalWidget_2 = QWidget(self.verticalWidget_8)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        sizePolicy.setHeightForWidth(self.horizontalWidget_2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_11 = QPushButton(self.horizontalWidget_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy1.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy1)
        self.pushButton_11.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_11.setStyleSheet(
            "background-color: rgb(65, 168, 99); color: white; border-radius: 6px; padding: 8px 16px;"
        )
        self.pushButton_11.clicked.connect(self.switchContent)

        self.horizontalLayout_2.addWidget(self.pushButton_11)


        self.verticalLayout_8.addWidget(self.horizontalWidget_2)


        self.verticalLayout.addWidget(self.verticalWidget_8)


        self.horizontalLayout_3.addWidget(self.rightWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 950, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.switchContent()

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def switchContent(self):
        movie_ids = self.system.recommend_for_user(1, 8)
        movie_cards = (
            (self.pushButton_m1, self.label_m1),
            (self.pushButton_m2, self.label_m2),
            (self.pushButton_m3, self.label_m3),
            (self.pushButton_m4, self.label_m4),
            (self.pushButton_m5, self.label_m5),
            (self.pushButton_m6, self.label_m6),
            (self.pushButton_m7, self.label_m7),
            (self.pushButton_m8, self.label_m8),
        )
        for position, (poster, label) in enumerate(movie_cards):
            has_movie = position < len(movie_ids)
            poster.setVisible(has_movie)
            label.setVisible(has_movie)
            label.setTextFormat(Qt.TextFormat.PlainText)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setWordWrap(True)
            label.setText(self.system.get_movie_name(int(movie_ids[position])) if has_movie else "")
        self.statusbar.showMessage("No recommendations available" if len(movie_ids) == 0 else "")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MovieMind", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "<h2>MovieMind</h2>", None))
        self.label_8.setText(
            QCoreApplication.translate("MainWindow", '<h1 align="center">Recommended films</h1>', None)
        )
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", "Refresh recommendations", None))

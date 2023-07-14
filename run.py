# -*-coding = utf-8 -*-
# @Time : 2023/7/14 13:56
# @Author : 万锦
# @File : run.py
# @Softwore : PyCharm

from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication
import sys

ui,_ = loadUiType("echarts交互.ui")

class MainWindow(QMainWindow,ui):
    def __init__(self, parent=None):
        """
        一些初始设置
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.init()
        self.button_connect()

    def init(self):
        self.pie_chart = QWebEngineView()
        self.line_chart = QWebEngineView()
        self.bar_chart = QWebEngineView()

    def button_connect(self):
        self.pushButton.clicked.connect(self.pie)
        self.pushButton_2.clicked.connect(self.line)
        self.pushButton_3.clicked.connect(self.bar)
        self.pushButton_4.clicked.connect(self.pie_change)
        self.pushButton_5.clicked.connect(self.line_change)
        self.pushButton_6.clicked.connect(self.bar_change)

    def bar(self):
        self.statusBar().showMessage("柱状图正在加载中...")
        if self.verticalLayout_3.count()>0:
            self.verticalLayout_3.removeItem(self.verticalLayout_3.itemAt(0))
        self.bar_chart.load(QUrl("file:///" + "./html/bar.html"))
        self.verticalLayout_3.addWidget(self.bar_chart)
        self.statusBar().showMessage("柱状图加载完毕")

    def bar_change(self):
        jscode = "bar_com(5, 20, 36, 10, 10, 20)"
        if self.bar_chart.page():
            self.bar_chart.page().runJavaScript(jscode)

    def pie(self):
        self.statusBar().showMessage("柱状图正在加载中...")
        if self.verticalLayout.count() > 0:
            self.verticalLayout.removeItem(self.verticalLayout.itemAt(0))
        self.pie_chart.load(QUrl("file:///" + "./html/pie.html"))
        self.verticalLayout.addWidget(self.pie_chart)
        self.statusBar().showMessage("柱状图加载完毕")
    def pie_change(self):
        jscode = "pie_com(120, 132, 101, 134, 90)"
        if self.pie_chart.page():
            self.pie_chart.page().runJavaScript(jscode)
    def line(self):
        self.statusBar().showMessage("线图正在加载中...")
        if self.verticalLayout_2.count() > 0:
            self.verticalLayout_2.removeItem(self.verticalLayout_2.itemAt(0))
        self.line_chart.load(QUrl("file:///" + "./html/line.html"))
        self.verticalLayout_2.addWidget(self.line_chart)
        self.statusBar().showMessage("线图加载完毕")

    def line_change(self):
        jscode = "line_com(120, 132, 101, 134, 90, 230, 210)"
        if self.line_chart.page():
            self.line_chart.page().runJavaScript(jscode)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainwindwow = MainWindow()
    mainwindwow.show()
    sys.exit(app.exec_())
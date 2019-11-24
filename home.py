from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *
from PySide2.QtGui import QPixmap

from main import MainWindow


class MainWidget (QWidget):

    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        f = QFile("home.ui")
        f.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.ui = loader.load(f,  self)

        f.close()
        logo = self.ui.findChild(QLabel, 'logoLabel')
        logo.setPixmap(QPixmap('ht.jpeg').scaled(300, 200))

        version = self.ui.findChild(QLabel, 'versionLabel')
        version.setText('Version 0.1.1')

        importButton = self.ui.findChild(QPushButton, 'createProjectButton')
        importButton.clicked.connect(self.openMainWindow)

        self.about = self.ui.findChild(QLabel, 'aboutLabel')
        self.about.setText('Hazutrend is a corrosion inspection software developed in October 2019. It is a multi-discipline engineering software that applies Machine Learning at the backend for inspection of Corrosion Rate, Erosion Trend Angle of pipelines and flowlines, Erosion Trend Factor and other tools for effective decision making. Hazutrend was developed by Amadi Hope Azubuike a Petroleum engineer from the Institute of Petroleum Studies (University of Port Harcourt)/ IFP School France, sponsored by Total E&P Nigeria. This software aims at solving decision making problems of onshore and offshore pipeline integrity in the petroleum industry.')

    def openMainWindow(self):
        self.mainUIWindow = MainWindow()
        self.hide()
        print('A new window is opened!')


if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication([])
    window = MainWidget()
    window.show()
    app.exec_()

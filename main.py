from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap
from PIL import Image, ImageDraw, ImageFont

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(800, 600)
                MainWindow.setStyleSheet("background-color: #30475e;")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.Title = QtWidgets.QLabel(self.centralwidget)
                self.Title.setGeometry(QtCore.QRect(240, 0, 341, 73))
                font = QtGui.QFont()
                font.setFamily("Fira Mono")
                font.setPointSize(45)
                font.setBold(True)
                font.setItalic(True)
                font.setWeight(75)
                self.Title.setFont(font)
                self.Title.setStyleSheet("color: #dddddd;")
                self.Title.setAlignment(Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
                self.Title.setObjectName("Title")
                self.ImageButton = QtWidgets.QPushButton(self.centralwidget)
                self.ImageButton.setGeometry(QtCore.QRect(10, 90, 221, 41))
                font = QtGui.QFont()
                font.setFamily("DejaVu Sans")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.ImageButton.setFont(font)
                self.ImageButton.setStyleSheet("background-color: #f05454;\n"
        "color: #FFFFFF;")
                self.ImageButton.setObjectName("ImageButton")
                self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEdit.setGeometry(QtCore.QRect(260, 90, 261, 41))
                self.lineEdit.setStyleSheet("background-color: #FFF;\n"
        "color: rgb(0, 0, 0);\n"
        "border-radius: 14px;\n"
        "padding: 7.5px 20px;")
                self.lineEdit.setObjectName("lineEdit")
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(540, 90, 241, 41))
                font = QtGui.QFont()
                font.setFamily("DejaVu Sans")
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.pushButton.setFont(font)
                self.pushButton.setStyleSheet("background-color: #f05454;\n"
        "color: #FFFFFF;")
                self.pushButton.setObjectName("pushButton")
                self.IMG = QtWidgets.QLabel(self.centralwidget)
                self.IMG.setGeometry(QtCore.QRect(200, 150, 391, 401))
                self.IMG.setText("")
                self.IMG.setPixmap(QtGui.QPixmap("ui/../images/placeholder.png"))
                self.IMG.setScaledContents(True)
                self.IMG.setObjectName("IMG")
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                self.image_path = ''
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

                self.ImageButton.clicked.connect(self.openImage)
                self.pushButton.clicked.connect(self.putWatermark)

        def openImage(self):
                imagePath, _ = QFileDialog.getOpenFileName()
                new_img = Image.open(imagePath)
                title_image = imagePath.split('/')[-1].split('.')[0] + '.png'
                new_img.save(f'./images/{title_image}')
                new_img.close()
                pixmap = QPixmap(f'./images/{title_image}')
                self.image_path = f'./images/{title_image}'
                self.IMG.setPixmap(pixmap)

        def putWatermark(self):
                text = self.lineEdit.text()
                img_select = Image.open(self.image_path).convert('RGBA')
                txt = Image.new('RGBA', img_select.size, (255,255,255,0))
                MAX_W, MAX_H = img_select.size
                draw = ImageDraw.Draw(txt)
                font = ImageFont.FreeTypeFont(r"./font/FreeMono.ttf",300)
                values = draw.textbbox((0, 0),text=text, font=font)
                draw.text(((MAX_W - values[2]) / 2, (MAX_H - values[3]) / 2), text, fill=(0,0,0, 100), font=font)
                combined = Image.alpha_composite(img_select, txt)
                combined.save(self.image_path)
                pixmap = QPixmap(self.image_path)
                self.IMG.setPixmap(pixmap)
                
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Watermark!"))
                self.Title.setText(_translate("MainWindow", "WATERMARK"))
                self.ImageButton.setText(_translate("MainWindow", "SELECT IMAGE"))
                self.lineEdit.setText(_translate("MainWindow", "Write here"))
                self.pushButton.setText(_translate("MainWindow", "PUT ON PHOTO"))


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec())

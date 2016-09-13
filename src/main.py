import argparse
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStyle
from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.QtCore import Qt

class myGLWidget(QOpenGLWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super(myGLWidget, self).__init__(parent, flags)
    
    def initializeGL(self):
        super(myGLWidget, self).initializeGL()
    
    def paintGL(self):
        super(myGLWidget, self).paintGL()
    
    def resizeGL(self, p_int, p_int_1):
        super(myGLWidget, self).resizeGL(p_int, p_int_1)

def main(args):
    app = QApplication(args)
    mainWindow = QMainWindow()
    mainWindow.setGeometry(
        QStyle.alignedRect(
            Qt.LeftToRight,
            Qt.AlignCenter,
            mainWindow.size(),
            app.desktop().availableGeometry()
        )
    )
    gl = myGLWidget()
    mainWindow.setCentralWidget(gl)
    mainWindow.show()
    app.exec_()

def cli():
    arg_parser = argparse.ArgumentParser()
    args = arg_parser.parse_args()
    if args == argparse.Namespace():
        args = []
    main(args)

if __name__ == '__main__':
    cli()
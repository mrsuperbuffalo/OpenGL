from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStyle
from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QOpenGLContext
from PyQt5.QtGui import QOpenGLVersionProfile
from PyQt5.QtGui import QSurfaceFormat
from PyQt5.QtGui import QOpenGLBuffer
from PyQt5.QtGui import QOpenGLShader
from PyQt5.QtGui import QOpenGLShaderProgram
from PyQt5.QtGui import QOpenGLVertexArrayObject
from PyQt5.QtCore import Qt

class MyGLWidget(QOpenGLWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super(MyGLWidget, self).__init__(parent, flags)

    def initializeGL(self):
        con = QOpenGLContext().currentContext()
        fun = con.versionFunctions()
        fun.glClearColor(0.0, 1.0, 0.0, 1.0)
        self.glFun = fun

def main():
    app = QApplication([])

    # for all surface formats
    fmt = QSurfaceFormat()
    fmt.setDepthBufferSize(24)
    fmt.setStencilBufferSize(8)
    fmt.setVersion(4, 1)
    fmt.setProfile(QSurfaceFormat.CoreProfile)
    QSurfaceFormat.setDefaultFormat(fmt)

    mWin = QMainWindow()
    mWin.setGeometry(
        QStyle.alignedRect(
            Qt.LeftToRight,
            Qt.AlignCenter,
            mWin.size(),
            app.desktop().availableGeometry()
        )
    )
    glWIn = MyGLWidget()

    # for a single window
    # fmt = QSurfaceFormat()
    # fmt.setDepthBufferSize(24)
    # fmt.setStencilBufferSize(8)
    # fmt.setVersion(4, 1)
    # fmt.setProfile(QSurfaceFormat.CoreProfile)
    # glWIn.setFormat(fmt)

    mWin.setCentralWidget(glWIn)
    try:
        mWin.show()
    except Exception as e:
        print(e)
    app.exec_()

if __name__ == '__main__':
    main()


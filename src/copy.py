from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QOpenGLContext
from PyQt5.QtGui import QOpenGLVersionProfile
from PyQt5.QtGui import QSurfaceFormat
from PyQt5.QtGui import QOpenGLShader
from PyQt5.QtGui import QOpenGLShaderProgram
from PyQt5.QtGui import QVector3D
from PyQt5.QtGui import QMatrix4x4
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
import sys
import numpy
# import pandas

class DrawingWidget(QOpenGLWidget):
    def __init__(self, *args, data, **kwargs):
        super(DrawingWidget, self).__init__(*args, **kwargs)
        self.vp = QOpenGLVersionProfile()

    def initializeGL(self):
        self.vp.setVersion(4, 1)

        vert_shader = """
        #version 330 core
        layout (location = 0) in vec3 position;

        void main(){
            gl_Position = vec4(position.x, position.y, position.z, 1.0)
        }
        """

        frag_shader = """
        #version 330 core
        out vec4 color;

        void main(){
            color = vec4(1.0f, 0.5f, 0.2f, 1.0f);
        }
        """


        self.shader = QOpenGLShaderProgram(self)
        self.shader.addShaderFromSourceCode(
            QOpenGLShader.Vertex,
            vert_shader
        )
        self.shader.addShaderFromSourceCode(
            QOpenGLShader.Fragment,
            frag_shader
        )
        self.shader.link()
        # self.fun = QOpenGLContext.currentContext().versionFunctions(self.vp)
        # print(self.fun)

    def resizeGL(self, width, height):
        fun = QOpenGLContext.currentContext().versionFunctions(self.vp)
        print(fun)


def main():
    """Entry for the application."""

    # data = numpy.random.rand(3, 3)
    data = numpy.array(
        [
            [-0.5, -0.5, 0.0],
            [ 0.5, -0.5, 0.0],
            [ 0.0,  0.5, 0.0]
        ]
    )

    app = QApplication([])
    mWin = QMainWindow()
    dWidget = DrawingWidget(data=data)
    mWin.setCentralWidget(dWidget)
    mWin.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
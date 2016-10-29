import argparse
import sys
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


class myGLWidget(QOpenGLWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags(), versionprofile=None):
        super(myGLWidget, self).__init__(parent, flags)
        self.versionprofile = versionprofile

    def initializeGL(self):
        self.gl = self.context().versionFunctions(self.versionprofile)
        if not self.gl:
            raise RuntimeError("unable to apply OpenGL version profile")
        self.gl.initializeOpenGLFunctions()

        self.createShaders()
        self.createVBO()
        self.gl.glClearColor(0.0, 0.0, 0.0, 0.0)

    def paintGL(self):
        """Painting callback that uses the initialized OpenGL functions."""
        if not self.gl:
            return

        self.gl.glClear(self.gl.GL_COLOR_BUFFER_BIT | self.gl.GL_DEPTH_BUFFER_BIT)
        self.gl.glDrawArrays(self.gl.GL_TRIANGLES, 0, 3)

    def resizeGL(self, w, h):
        """Resize viewport to match widget dimensions."""
        self.gl.glViewport(0, 0, w, h)


    def createShaders(self):
        """Create shaders."""

    def createVBO(self):
        """Create vertex buffer object."""

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

    fmt = QSurfaceFormat()
    fmt.setVersion(4, 1)
    fmt.setProfile(QSurfaceFormat.CoreProfile)
    fmt.setSamples(4)
    QSurfaceFormat.setDefaultFormat(fmt)

    vp = QOpenGLVersionProfile()
    vp.setVersion(4, 1)
    vp.setProfile(QSurfaceFormat.CoreProfile)

    gl = myGLWidget(mainWindow, versionprofile=vp)
    mainWindow.setCentralWidget(gl)
    mainWindow.show()
    sys.exit(app.exec_())


def cli():
    arg_parser = argparse.ArgumentParser()
    args = arg_parser.parse_args()
    if args == argparse.Namespace():
        args = []
    main(args)


if __name__ == '__main__':
    cli()
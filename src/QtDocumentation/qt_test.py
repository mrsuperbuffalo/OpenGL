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
import numpy as np

class MyGLWidget(QOpenGLWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags(), **kwargs):
        super(MyGLWidget, self).__init__(parent, flags)
        self.data = kwargs.get('data')

    def initializeGL(self):
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

        con = QOpenGLContext().currentContext()
        fun = con.versionFunctions()
        fun.glClearColor(0.0, 1.0, 0.0, 1.0)
        self.glFun = fun

        posAttr = self.shader.attributeLocation('position')


    def resizeGL(self, width, height):
        self.glFun.glViewport(0, 0, width, height)
        self.glFun.glClearColor(1.0, 1.0, 1.0, 1.0)
        self.glFun.glClear(self.glFun.GL_COLOR_BUFFER_BIT)

    def paintGL(self):
        self.glFun.glClearColor(1.0, 1.0, 1.0, 1.0)
        self.glFun.glClear(self.glFun.GL_COLOR_BUFFER_BIT)

        self.glFun.glEnable(self.glFun.GL_BLEND)
        self.glFun.glBlendFunc(self.glFun.GL_SRC_COLOR,
                               self.glFun.GL_ONE_MINUS_SRC_COLOR)

        # self.shader_program.setUniformValue('minx', self.minx)
        # self.shader_program.setUniformValue('maxx', self.maxx)
        # self.shader_program.setUniformValue('miny', self.miny)
        # self.shader_program.setUniformValue('maxy', self.maxy)
        #
        # self.shader_program.setUniformValue("degs", self.degs)
        # self.shader_program.enableAttributeArray('xx')
        # self.shader_program.enableAttributeArray('ox')
        # self.shader_program.enableAttributeArray('yy')
        # self.shader_program.enableAttributeArray('oy')
        # fun.glDrawArrays(fun.GL_TRIANGLES, 0, self.number_of_points)
        # self.shader_program.disableAttributeArray('xx')
        # self.shader_program.disableAttributeArray('ox')
        # self.shader_program.disableAttributeArray('yy')
        # self.shader_program.disableAttributeArray('oy')
        # fun.glDisable(fun.GL_BLEND)


def main():
    data = np.array(
        [
            [-0.5, -0.5, 0.0],
            [ 0.5, -0.5, 0.0],
            [ 0.0,  0.5, 0.0]
        ]
    )


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
    glWIn = MyGLWidget(data=data)

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

#http://stackoverflow.com/questions/25703307/pyqt4-opengl-gl-core-profile-error
# might be useful
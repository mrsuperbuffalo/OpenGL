from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QSurfaceFormat
from PyQt5.QtGui import QOpenGLShaderProgram
from PyQt5.QtGui import QOpenGLVersionProfile
from PyQt5.QtGui import QOpenGLShader
from PyQt5.QtGui import QMatrix4x4
from PyQt5.QtGui import QScreen
from numpy import array

class TriangleWindow(QOpenGLWidget):
    def __init__(self, *args, **kwargs):
        super(TriangleWindow, self).__init__(*args, **kwargs)
        vp = QOpenGLVersionProfile()
        vp.setVersion(4, 1)
        vp.setProfile(QSurfaceFormat.CoreProfile)
        self.versionprofile = vp
        self.m_frame = 0

    def initializeGL(self):
        self.gl = self.context().versionFunctions(self.versionprofile)
        if not self.gl:
            raise RuntimeError("unable to apply OpenGL version profile")
        self.gl.initializeOpenGLFunctions()

        self.m_program = QOpenGLShaderProgram()
        self.m_program.addShaderFromSourceCode(QOpenGLShader.Vertex, vertex_shader)
        self.m_program.addShaderFromSourceCode(QOpenGLShader.Fragment, fragment_shader)
        self.m_program.link()
        self.pos_attr = self.m_program.attributeLocation('posAttr')
        self.col_attr = self.m_program.attributeLocation('colAttr')
        self.matrix_uniform = self.m_program.uniformLocation('matrix')

    def render(self, *__args):
        retinaScale = QApplication.instance().devicePixelRatio()
        self.glViewport(0, 0,
            retinaScale * self.width(),
            retinaScale * self.height()
        )
        self.gl.glClear(self.gl.GL_COLOR_BUFFER_BIT)
        self.m_program.bind()

        matrix = QMatrix4x4()
        matrix.perspective(60.0, 4.0/3.0, 0.1, 100.0)
        matrix.translate(0, 0, -2)
        matrix.rotate(100 * self.m_frame / refresh_rate, 0, 1, 0)
        self.m_program.setUniformValue(self.matrix_uniform, matrix)

        vertices = array([
            0.0, 0.707,
            -0.5, -0.5,
            0.5, 0.5
        ])

        colors = array([
            1.0, 0.0, 0.0,
            0.0, 1.0, 0.0,
            0.0, 0.0, 1.0
        ])

        self.gl.glVertexAttribPointer(
            self.posAttr, 2, self.gl.GL_FLOAT, self.gl.GL_FALSE, 0, vertices)
        self.gl.glVertexAttribPointer(
            self.colAttr, 3, self.gl.GL_FLOAT, self.gl.GL_FALSE, 0, colors)

        self.gl.glEnableVertexAttribArray(0)
        self.gl.glEnableVertexAttribArray(1)

        self.gl.glDrawArrays(self.gl.GL_TRIANGLES, 0, 3)

        self.gl.self.gl.glDisableVertexAttribArray(0)

        self.m_program.release()

        self.m_frame += 1



if __name__ == '__main__':
    app = QApplication([])


    vertex_shader = """
    attribute highp vec4 posAttr;
    attribute lowp vec4 colAttr;
    varying lowp vec4 col;
    uniform highp mat4 matrix;

    void main() {
        col = colAttr;
        gl_Position = matrix * posAttr;
    }
    """

    fragment_shader = """
    varying lowp vec4 col;
    void main(){
        gl_FragColor = col;
    }
    """

    # screen = QScreen()
    # refresh_rate = screen.refreshRate()
    refresh_rate = 60


    qs_format = QSurfaceFormat()
    qs_format.setSamples(16)
    window = TriangleWindow()

    window.setFormat(qs_format)
    window.resize(640, 480)
    window.show()
    # window.setAnimating(True)

    app.exec_()
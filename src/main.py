import argparse
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStyle
from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QAbstractOpenGLFunctions
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QMatrix4x4
from PyQt5.QtGui import QOpenGLContext
from PyQt5.QtGui import QOpenGLVersionProfile
from PyQt5.QtGui import QSurfaceFormat
from PyQt5.QtGui import QOpenGLBuffer
from PyQt5.QtGui import QOpenGLShader
from PyQt5.QtGui import QOpenGLShaderProgram
from PyQt5.QtGui import QOpenGLVertexArrayObject
from PyQt5.QtCore import Qt

class myGLWidget(QOpenGLWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super(myGLWidget, self).__init__(parent, flags)
    
    def initializeGL(self):
        con = QOpenGLContext().currentContext()
        self.vp = QOpenGLVersionProfile()
        lastok = (None, None)
        for major in (1,2,3,4):
            for minor in range(40):
                try:
                    self.vp.setVersion(major, minor)
                    self.vp.setProfile(QSurfaceFormat.CoreProfile)
                    fun = con.versionFunctions(self.vp)
                    fun.glClearColor(0.0, 0.0, 0.0, 1.0)
                    print("{}.{} ok".format(major, minor))
                    lastok = (major, minor)
                except:
                    pass
        self.vp.setVersion(*lastok)

        self.shader_program = QOpenGLShaderProgram(self)
        self.shader_program.create()
        self.shader_program.bind()
        self.shader_program.addShaderFromSourceCode(
            QOpenGLShader.Vertex,
            """
            # version 330 core
            attribute highp vec4 vertex;
            uniform highp mat4 matrix;
            void main(void)
            {
                gl_Position = matrix * vertex;
            }
            """)
        self.shader_program.addShaderFromSourceCode(
            QOpenGLShader.Geometry,
            """
            # version 330 core
            layout(points) in;
            layout(triangle_strip, max_vertices = 3) out;

            void main()
            {
                gl_Position = gl_in[0].gl_Position + vec4(-0.1, 0.0, 0.0, 0.0);
                EmitVertex();

                gl_Position = gl_in[0].gl_Position + vec4(0.1, 0.0, 0.0, 0.0);
                EmitVertex();

                gl_Position = gl_in[0].gl_Position + vec4(0.0, 0.1, 0.0, 0.0);
                EmitVertex();

                EndPrimitive();
            }
            """)

        self.shader_program.addShaderFromSourceCode(
            QOpenGLShader.Fragment,
            """
            # version 330 core
            uniform mediump vec4 color;
            void main(void)
            {
                gl_FragColor = color;
            }
            """)
        self.shader_program.link()
        self.shader_program.bind()

    
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
    # con = QOpenGLContext(app)
    gl = myGLWidget(mainWindow)
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
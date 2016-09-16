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

con = QOpenGLContext()
# con = QOpenGLContext().currentContext()
print(con)
vp = QOpenGLVersionProfile()
lastok = (None, None)
for major in (1,2,3,4):
    for minor in range(40):
        try:
            # vp.setVersion(major, minor)
            # vp.setProfile(QSurfaceFormat.CoreProfile)
            # fun = con.versionFunctions(vp)
            # fun.glClearColor(1.0, 0.5, 1.0, 1.0)
            # print(major, minor)
            print("{}.{} ok".format(major, minor))
            lastok = (major, minor)
        except Exception as e:
            print(e)
            pass
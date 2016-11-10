# Knowledge

This will hopefully document my understanding of how the each component works
and how they interact with each other.


## OpenGL



## QOpenGL

This will probably just be just a discussion of the QOpenGLWidget which should
be used for all the Qt integrations.

As of this writing I have done some research on this topic. I want to write
about what I know now so I can see where I get. I believe InitializeGL this is
the location to set up all the shader's for the image to be drawn. There are
several shader's that come together to draw what you want depending on how you
put it together. If this is the case you would need to have a set of shader's
dedicated to, in my case, a cube(wireframe), a cube(solid), a cone, a cylinder,
"dots", and sphere. So when we know what to draw we create shader's for them. I
also believe we can have shader's for all the components. Once Qt/OpenGL knows
what we want to draw it is painted during another step. I believe this step in
paintGL method.


### InitializeGL

    This virtual function is called once before the first call to paintGL() or
    resizeGL(). Reimplement it in a subclass.

    This function should set up any required OpenGL resources and state.

    There is no need to call makeCurrent() because this has already been done
    when this function is called. Note however that the framebuffer is not yet
    available at this stage, so avoid issuing draw calls from here. Defer such
    calls to paintGL() instead.

The makeCurrent method is something I wasn't familiar with so I followed the
link provided in the quoted text.

    void QOpenGLWidget::makeCurrent()

        Prepares for rendering OpenGL content for this widget by making the
        corresponding context current and binding the framebuffer object in that
        context.

        It is not necessary to call this function in most cases, because it is
        called automatically before invoking paintGL().

        See also context(), paintGL(), and doneCurrent().

Hmm, it looks like this is also the location where a context is created for the
widget. A context for the widget looks to be created in the initializeGL method.
We do not need to create a context before that in order to get access to the gl
functions.


### PaintGL


    void QOpenGLWidget::paintGL()

        This virtual function is called whenever the widget needs to be painted.
        Reimplement it in a subclass.

        There is no need to call makeCurrent() because this has already been
        done when this function is called.

        Before invoking this function, the context and the framebuffer are
        bound, and the viewport is set up by a call to glViewport(). No other
        state is set and no clearing or drawing is performed by the framework.


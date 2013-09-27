import matplotlib_qt
from PyQt4.QtGui import QMainWindow
from qt_window_manager import WindowManager
import state_action_browser_ui
import basewindow
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT
import pylab as mpl
from esdcs.gui.drawUtils import drawObject
from esdcs.gui import context3d

from diapers.diaper_state import DiaperState

class MainWindow(QMainWindow, state_action_browser_ui.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.figure = mpl.figure()
        self.axes = self.figure.gca()
        self.axes.set_aspect("equal")
        self.oldParent = self.figure.canvas.parent()
        self.figure.canvas.setParent(self)
        self.matplotlibFrame.layout().addWidget(self.figure.canvas)
        self.toolbar = NavigationToolbar2QT(self.figure.canvas, self)
        self.addToolBar(self.toolbar)
        self.windowManager = WindowManager(self.windowsMenu)

        self.limits = [-2, 8, -2, 8]

        self.contextWindow = context3d.MainWindow()
        self.contextWindow.setWindowTitle(self.contextWindow.windowTitle() + 
                                          " - State Action Browser")
        self.contextWindow.setVisible(True)
        self.windowManager.addWindow(self.contextWindow)


        self.state = DiaperState.example_state()
        self.contextWindow.setContext(self.state.to_context())
        self.draw()

    def draw(self):
        self.axes.clear()
        self.artists = []

        for g in self.state.to_context().objects:
                drawObject(self.axes, g)

        self.restoreLimits()
        self.figure.canvas.draw()

                
    def updateLimits(self, mplEvent):
        self.saveLimits()
    def saveLimits(self):
        self.limits = self.axes.axis()
    def restoreLimits(self):
        if self.limits != None:
            self.axes.axis(self.limits)


def main(argv):
    app = basewindow.makeApp()
    wnd= MainWindow()
    wnd.show()
    app.exec_()

if __name__=="__main__":
    import sys
    main(sys.argv)



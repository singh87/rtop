import psutil
import datetime
import socket
import os
import npyscreen
from drawille import Canvas

hostname = socket.gethostname()

class GraphWidget(npyscreen.MultiLineEdit):
    pass

class TitledGraphWidget(npyscreen.BoxTitle):
    _contained_widget = GraphWidget

class FormObject(npyscreen.Form):
    def create(self):
        self.add(TitledGraphWidget, name='CPU Usage',max_height=10,max_width=50)
        self.add(TitledGraphWidget, name='Memory Usage',max_height=10,max_width=50)


class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', FormObject, name='rtop-%s' % hostname)

    def onInMainLoop(self):
        pass

 
time = str(datetime.datetime.now().time())


if (__name__=="__main__"):
    app = App().run()








    
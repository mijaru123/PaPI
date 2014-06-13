from PySide import QtCore, QtGui, QtWebKit
import os, sys
from categories import Formatter
from yapsy.PluginManager import PluginManager

class Main(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.layout = QtGui.QVBoxLayout()
        self.formattersCombo = QtGui.QComboBox()
        self.editor = QtGui.QPlainTextEdit()
        self.preview = QtWebKit.QWebView()

        self.layout.addWidget(self.formattersCombo)
        self.layout.addWidget(self.editor)
        self.layout.addWidget(self.preview)

        self.editor.textChanged.connect(self.updatePreview)
        self.setLayout(self.layout)

        # Create plugin manager
        self.manager = PluginManager(categories_filter={ "Formatters": Formatter})
        self.manager.setPluginPlaces(["plugins"])

        # Load plugins
        self.manager.locatePlugins()
        self.manager.loadPlugins()

        # A do-nothing formatter by default
        self.formattersCombo.addItem("None")
        self.formatters = {}
        print(self.manager.getPluginsOfCategory("Formatters"))
        for plugin in self.manager.getPluginsOfCategory("Formatters"):
            print("XXX")
            # plugin.plugin_object is an instance of the plugin
            self.formattersCombo.addItem(plugin.plugin_object.name)
            self.formatters[plugin.plugin_object.name] = plugin.plugin_object

    def updatePreview(self):
        # Check what the current formatter is
        name =  str(self.formattersCombo.currentText())
        text = str(self.editor.toPlainText())
        if name in self.formatters:
            text = self.formatters[name].formatText(text)
        self.preview.setHtml(text)

def main():
    # Again, this is boilerplate, it's going to be the same on
    # almost every app you write
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

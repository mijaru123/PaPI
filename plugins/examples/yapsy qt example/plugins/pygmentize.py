from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

from categories import Formatter

class Pygmentizer(Formatter):
    name = "Python Code"

    def formatText(self, text):
        return highlight(text, PythonLexer(), HtmlFormatter(full=True))
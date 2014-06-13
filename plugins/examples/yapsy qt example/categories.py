class Formatter(object):
    """Plugins of this class convert plain text to HTML"""

    name = "No Format"

    def formatText(self, text):
        """Takes plain text, returns HTML"""
        return text
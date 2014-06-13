from categories import Formatter
import docutils.core
import docutils.io


class Rest(Formatter):
    name = "Restructured Text"

    def formatText(self, text):
        output = docutils.core.publish_string(
            text, writer_name = 'html'
        )
        return output
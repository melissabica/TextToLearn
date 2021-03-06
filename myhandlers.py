# myhandlers.py

from rapidsms.contrib.handlers import KeywordHandler
from rapidsms.contrib.handlers import PatternHandler
from training_materials.models import TrainingMaterial

help_text = {
    'training': 'To start, reply START TAG. Example, START INTRO. To continue, reply NEXT TAG.',
    'quiz': 'To start, reply QUIZ TAG. Example, QUIZ INTRO. To continue, reply ANS youranswer.',
}
"""
class TMHandler(KeywordHandler):
    heyword = "start"
    
    if(tag == Training
    self.respond("TrainingMaterial.me")
"""
class HelpHandler(KeywordHandler):
    keyword = "help"

    def help(self):
        """Invoked if someone just sends `HELP`.  We also call this
        from `handle` if we don't recognize the arguments to HELP.
        """
        self.respond("Reply HELP TRAINING or HELP QUIZ for instructions.")

    def handle(self, text):
        """Invoked if someone sends `HELP <any text>`"""
        text = text.strip().lower()
        if text == 'training':
            self.respond(help_text['training'])
        elif text == 'quiz':
            self.respond(help_text['quiz'])
        else:
            self.help()
            

class SumHandler(PatternHandler):
    pattern = r'^(\d+) plus (\d+)$'

    def handle(self, a, b):
        a, b = int(a), int(b)
        total = a + b

        self.respond(
            "%d+%d = %d" %
            (a, b, total))

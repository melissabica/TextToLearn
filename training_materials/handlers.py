# voting/handlers.py

from rapidsms.contrib.handlers import KeywordHandler

from .models import TrainingMaterial, MessageTracker
from django.db.models import F

"""class StartHandler(KeywordHandler):
    keyword = "start"

    def help(self):
        help() gets invoked when we get the ``results`` message
        with no arguments
        # Build the response message, one part per choice
        
        parts = []
        for choice in Choice.objects.all():
            part = "%s: %d" % (choice.name, choice.votes)
            parts.append(part)
        # Combine the parts into the response, with a semicolon after each
        msg = "; ".join(parts)
        # Respond
        self.respond(msg)
    def handle(self, text):
       """ """This gets called if any arguments are given along with
        ``RESULTS``, but we don't care; just call help() as if they
        passed no arguments""""""
        self.help()
"""
class StartHandler(KeywordHandler):
    keyword = "start"

    def help(self):
        """Respond with the valid commands.  Example response:
        ``Valid commands: VOTE <Moe|Larry|Curly>``
        """
        self.respond("Invalid training material tag")

    def handle(self, text):
        text = text.strip()
        # look for a choice that matches the attempted vote
        try:
            tm = TrainingMaterial.objects.get(tag__iexact=tag)
        except TrainingMaterial.DoesNotExist:
            # Send help
            self.help()
        else:
            try:
                contact = MessageTracker.objects.get(self.msg.contact)
            except:
                MessageTracker.objects.create(contact=contact, tmorquiz = "tm", msgnum = 1)
            if tm.messagenum == 1:
                self.respond("%s" % tm.messages)
            else:
                self.respond("%s" % tm.messages[:160])
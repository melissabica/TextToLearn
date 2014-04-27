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
        self.respond("Invalid training material tag")

    def handle(self, text):
        text = text.strip()
        
        try: #valid tag?
            tm = TrainingMaterial.objects.get(tag__iexact=text)
        except TrainingMaterial.DoesNotExist:
            # Send help
            self.help()
        else:
            try: #is this user assigned to this training material?
                tm.assigned_users.objects.get(contact = self.msg.contact.id)
            except:
                self.respond("You have not been assigned this training")
            else: 
                try: #has this user done training before?
                    msgt = MessageTracker.objects.get(contact =self.msg.contact.id)
                except: #if not create an instance of messagetracker for them
                    msgt = MessageTracker.objects.create(contact=self.msg.contact, tmorquiz = "tm", msgnum = 1)            
                msgt.tmorquiz = "tm"
                msgt.msgnum = 1
                msgt.save()
                if tm.messagenum == 1:
                    self.respond("%s" % tm.messages)
                else:
                    self.respond("%s" % tm.messages[:160])

class NextHandler(KeywordHandler):
    keyword = "next"
    
    def help(self):
        self.respond("You have not started this training material")
    
    def handle(self, text):
        text = text.strip()
        try:
            tm = TrainingMaterial.objects.get(tag__iexact=text)
        except TrainingMaterial.DoesNotExist:
            # Send help
            self.help()
        else:
            try:
                msgt = MessageTracker.objects.get(contact = self.msg.contact.id)
            except:
                self.respond("You are not a registered user")
            else:
                if(msgt.tmorquiz == "tm"):
                    msgt.msgnum = msgt.msgnum + 1
                    msgt.save()
                    if tm.messagenum == msgt.msgnum:
                        self.respond("%s" % tm.messages[160*(msgt.msgnum-1):])
                        msgt.tmorquiz = ""
                        msgt.msgnum = 0
                        msgt.save()
                    else:
                        self.respond("%s" % tm.messages[160*(msgt.msgnum-1):160*msgt.msgnum])
                else:
                    self.help()

class QuizHandler(KeywordHandler):
    keyword = "quiz"
    
    def help(self):
        self.respond("Quiz is not available");
    
    def handle(self, text):
        try:
            tm = TrainingMaterial.objects.get(tag__iexact=text)
        except:
            self.help()
        else:
            try:
                msgt = MessageTracker.objects.get(contact = self.msg.contact.id)
            except:
                self.respond("You are not a registered user")
            else:
                if tm.question_1 is None:
                    self.help()
                else:
                    msgt.tmorquiz = "quiz"
                    msgt.msgnum = 1
                    msgt.save()
                    self.respond("%s" % tm.question_1)

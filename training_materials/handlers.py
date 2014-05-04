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
        try: #Registered User?
            self.msg.contact.id
        except: #Not a contact in our system reject
            self.respond("You have not been registered in our system")
        else:
            try: #valid tag?
                tm = TrainingMaterial.objects.get(tag__iexact=text)
            except TrainingMaterial.DoesNotExist:
                # Send help
                self.help()
            else:
                 #is this user assigned to this training material?
                if not tm.assigned_users.filter(id = self.msg.contact.id).exists():
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
        text = text.strip()
        try:
            tm = TrainingMaterial.objects.get(tag__iexact=text)
        except:
            if text == '':
                self.respond("You must enter QUIZ <TAG>")
            else:
                self.help()
        else:
            try:
                msgt = MessageTracker.objects.get(contact = self.msg.contact.id)
            except:
                self.respond("You are not a registered user")
            else:
                if tm.question_1 == '':
                    self.help()
                else:
                    msgt.tmorquiz = "quiz"
                    msgt.msgnum = 1
                    msgt.tag = text
                    msgt.save()
                    self.respond("%s -Reply ANS youranswer" % tm.question_1)

class AnsHandler(KeywordHandler):
    keyword = "ans"
    
    def help(self):
        self.respond("Quiz is not available")
    
    def handle(self, text):
        text = text.strip()
        try: #Have they started a training material?
            msgt = MessageTracker.objects.get(contact = self.msg.contact.id)
        except: #No, forward to next handler
            self.respond("you are not taking a quiz")
        else: #have started a training
            if msgt.tmorquiz != "quiz": #started quiz?
                self.respond("you are not taking a quiz") #No pass to next handler
            else: #started quiz
                try: #did the training material vanish?
                    tm = TrainingMaterial.objects.get(tag__iexact=msgt.tag)
                except TrainingMaterial.DoesNotExist:
                    self.respond("This shouldn't happen, but TM mysteriously vanished")
                else:
                    #Handle Quiz Answers
                    if msgt.msgnum == 1:
                        text = text.lower().strip()
                        tof = ""
                        if text == tm.answer_1:
                            tof = "Correct.\n"
                        else:
                            tof = ""
                            self.respond("Incorrect.\n Correct answer: %s" % tm.answer_1)
                        if tm.question_2 == "":
                            msgt.msgnum = 0
                            msgt.tmorquiz = ""
                            msgt.tag = ""
                            msgt.save()
                            self.respond("%s(quiz complete)" % tof) 
                        else:
                            msgt.msgnum += 1
                            msgt.save()
                            self.respond("%s%s-Reply ANS youranswer" % (tof, tm.question_2))
                    
                    elif msgt.msgnum == 2:
                        text = text.lower().strip()
                        tof = ""
                        if text == tm.answer_2:
                            tof = "Correct.\n"
                        else:
                            tof = "Incorrect.\n"
                        if tm.question_3 is "":
                            msgt.msgnum = 0
                            msgt.tmorquiz = ""
                            msgt.tag = ""
                            msgt.save()
                            self.respond(tof)
                        else:
                            msgt.msgnum += 1
                            msgt.save()
                            self.respond("%s%s-Reply ANS youranswer" % (tof, tm.question_3))
                            
                    elif msgt.msgnum == 3:
                        text = text.lower().strip()
                        tof = ""
                        if text == tm.answer_3:
                            tof = "Correct.\n"
                        else:
                            tof = "Incorrect.\n"
                        if tm.question_4 is "":
                            msgt.msgnum = 0
                            msgt.tmorquiz = ""
                            msgt.tag = ""
                            msgt.save()
                            self.respond(tof)
                        else:
                            msgt.msgnum += 1
                            msgt.save()
                            self.respond("%s%s-Reply ANS youranswer" % (tof, tm.question_4))                            
                            
                    elif msgt.msgnum == 4:
                        text = text.lower().strip()
                        tof = ""
                        if text == tm.answer_4:
                            tof = "Correct.\n"
                        else:
                            tof = "Incorrect.\n"
                        if tm.question_5 is "":
                            msgt.msgnum = 0
                            msgt.tmorquiz = ""
                            msgt.tag = ""
                            msgt.save()
                            self.respond(tof)
                        else:
                            msgt.msgnum += 1
                            msgt.save()
                            self.respond("%s%s-Reply ANS youranswer" % (tof, tm.question_5))
                    
                    elif msgt.msgnum == 5:
                        text = text.lower().strip()
                        tof = ""
                        if text == tm.answer_4:
                            tof = "Correct.\n"
                        else:
                            tof = "Incorrect.\n"
                        msgt.msgnum = 0
                        msgt.tmorquiz = ""
                        msgt.tag = ""
                        msgt.save()
                        self.respond("%s(complete)" % tof)               

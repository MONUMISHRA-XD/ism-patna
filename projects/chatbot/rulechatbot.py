import random
import re

class RuleBot:
    negative_responces = ("sorry","no","never","so sorry","nope","no at chance")
    exit_commands = ("exit","quiet","pause","good bye","bye")
    random_questions = (
         "hii there how are you",
         "hii sir how are you doing",
         "why are you here?",
         "does earth have a leader?",
         "whats planet have you visited",
         "what technology do you have on your planet"               
         )  

def __init__(self):
    self.ismbabble = {
        'describe_planets_intent' : r'.*\s*your planet.*',
        'answer_why_intent' : r'why/sare.*',
        'about_ismers' : r'.*\s ismers'
                      }

def greet(self):
    self.name = input("whats your name?\n")
    will_help = input(
        f"hii {self.name},i am ismers bot.will you help me to learn about your college?\n")
    if will_help in self.negative_responces:
        print("ok, have a nice day!")
        return 
    self.chat()

def make_exit(self,reply):
    for command in self.exit_commands:
        if reply == command:
            print("okay,have a nice day")
            return True

def chat(self):
    reply = input(random.choice(self.random_questions)).lower()
    while not self.make_exit(reply):
        reply = input(self.match_reply(reply))

def match_reply(self,reply):
    for key, value in self.ismbabble.items():
        intent = key
        regex_patterns = value
        found_match = re.match(regex_patterns, reply)
        if found_match and intent == 'describe_planets_intent':
            return self.describe_planets_intent()
        elif found_match and intent == 'answer_why_intent':
            return self.answer_why_intent()
        elif found_match and intent ==  'about_ismers':
            return self.about_ismers()
        if not found_match:
           return self.no_match_intent()

def describe_planets_intent(self):
    responses = ("my planet is no more\n","my planet has lost\n")
    return random.choice(responses)

def answer_why_intent(self):
    responses  = ("i am in  peace\n,i","i here to collect data on your college\n ","i heard the teachers is good\n")
    return random.choice(responses)

def about_ismers(self):
    responses = ("International School of Management Patna or popularly known as ISM Patna was established in the year 2011 and is approved by the All India Council of Technical Education (AICTE). The institute offers a Post Graduate Diploma in Management (PGDM) course to the students. The admission process is merit-based and the institute accepts scores of the exams like CAT/ XAT/ MAT/ CMAT. ISM Patna has signed an MoU with the SolBridge University, South Korea. It will provide the students with an opportunity to spend one trimester in South Korea without any extra tuition fee.\n",
                 "International School of Management, Patna or also known as ISM Patna is a private university which was established in the year 2011. The institute has been approved by the All India Council Of Technical Education (AICTE). ISM Patna is quite popular for offering PGDM, BBA, BCA, B.Com and BMS courses to the students. International School of Management Patna Admission are done through an entrance based process wherein the candidates are selected on the basis of their performance in exams such as CAT/ MAT/ CMAT/ XAT.\n")
    return random.choice(responses)

def no_match_intent(self):
    responses = ("please tell me more about this!!!\n","please tell more!!\n","why do you that.\n","i see can you elaborate?\n",
                 "why\n","can you tell me more?\n", "i see . How do you think?\n")
    return random.choice(responses)

ismbot = RuleBot()
ismbot.greet()


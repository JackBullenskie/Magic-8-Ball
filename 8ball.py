#!/usr/bin/env python

from random import randint
import time
import sys

responses = ["Absolutley not, you idiot",  "Sure! Dumbass.", \
"I don't know what you just said, you idiot",  \
"There is a strong chance of success",  "Maybe", \
"Keep trying, and don't give up", "Yes",  "No",  \
"I think it's possible",  "Your hopes are too high",  \
"Most likely, yes",  "I honestly don't know",  "Not today",  \
"Try, try again",  "Confucius say,no",  "Buddha say, yes",  \
"Thats a weird question, but yes",  "Ask your mom",  \
"Today's your lucky day",  "Sorry, but no"]

def respond():
    r = randint(0,  20)
    raw_input("Ask me a question: ")
    print responses[r]
    time.sleep(2)
    again()
    
def again():
    x = raw_input("Ask another question? ")
    while x.lower() == 'yes':
        respond()
    else:
        print "Have a good day!"
        sys.exit()
        
respond()

# 8-15 Printing Models

import printing_models as pm

unprinted_designs = ['robotic arm', 'head', 'screw']
completed_models = []

pm.print_models(unprinted_designs, completed_models)


# 8-16 Imports

import printing_models
from printing_models import print_models
from printing_models import print_models as pm
from printing_models import *



# 8-17 Styling Functions

short_messages = ['message_0', 'message_1', 'message_2', 'message_3']
sent_messages = []

def send_messages(short_messages):
    """
    This functions receives a list of short messages, and then copies 
    that list to a new list and print each element being copied into console
    """
    while short_messages:
        printed_message = short_messages.pop()
        sent_messages.append(printed_message)
        print(printed_message)


print("Values in Lists after function execution:")
print("\n")
send_messages(short_messages=short_messages[:])
print(short_messages)
print("\n")
print(sent_messages)
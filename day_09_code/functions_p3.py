# 8-9 Messages

# short_messages = ['message_0', 'message_1', 'message_2', 'message_3']

# def show_messages(short_messages):
#     for message in short_messages:
#         print(message)

# show_messages(short_messages=short_messages)


# 8-10 Sending Messages

# short_messages = ['message_0', 'message_1', 'message_2', 'message_3']
# sent_messages = []

# def send_messages(short_messages):
#     while short_messages:
#         printed_message = short_messages.pop()
#         sent_messages.append(printed_message)
#         print(printed_message)


# print("New Values in Lists after function execution:")
# print("\n")

# print(short_messages)
# print("\n")
# print(sent_messages)


# 8-11 Archived Messages

short_messages = ['message_0', 'message_1', 'message_2', 'message_3']
sent_messages = []

def send_messages(short_messages):
    while short_messages:
        printed_message = short_messages.pop()
        sent_messages.append(printed_message)
        print(printed_message)


print("Values in Lists before function execution:")
print("\n")

print(short_messages)
print("\n")
print(sent_messages)

print("Values in Lists after function execution:")
print("\n")
send_messages(short_messages=short_messages[:])
print(short_messages)
print("\n")
print(sent_messages)
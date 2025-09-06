# 8-10: Sending Messages
def send_messages(messages, sent_messages):
    while messages:
        msg = messages.pop(0)
        print(f"Sending message: {msg}")
        sent_messages.append(msg)

texts = ["Hello!", "How are you?", "Python is fun."]
sent = []

send_messages(texts, sent)

print("\nSent messages:", sent)
print("Remaining messages:", texts)

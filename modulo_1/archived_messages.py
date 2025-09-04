# 8-11: Archived Messages
def send_messages(messages, sent_messages):
    while messages:
        msg = messages.pop(0)
        print(f"Sending message: {msg}")
        sent_messages.append(msg)

texts = ["Hello!", "How are you?", "Python is fun."]
archived = []

send_messages(texts[:], archived)  # Use a copy

print("\nOriginal messages:", texts)
print("Archived messages:", archived)

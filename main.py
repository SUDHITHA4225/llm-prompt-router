from router import classify_intent, route_and_respond

print("LLM Prompt Router Started")
print("Type 'exit' to quit\n")

while True:

    message = input("User: ")

    if message.lower() == "exit":
        break

    intent_data = classify_intent(message)

    print("\nDetected Intent:", intent_data)

    response = route_and_respond(message, intent_data)

    print("\nAI:", response)

    print("\n----------------------\n")
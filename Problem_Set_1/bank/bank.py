msg = input("Greeting: ")
msg = msg.lower()
msg = msg.strip()

if msg.startswith("hello"):
    print("$0")
elif msg.startswith("h"):
    print("$20")
else:
    print("$100")

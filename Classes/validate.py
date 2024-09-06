import re

email = input("What's your email? ").strip()

# username, domain = email.split("@")

# if (username) and ("." in domain):
# if (username) and (domain.endswith(".com")):
#     print("Valid")
# else:
#     print("Invalid")

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email):
if re.search(r"^\w+@(\w+\.)?\w+\.(com|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
import secrets
import string

chars = string.digits + string.ascii_letters + string.punctuation
print("Dieser Generator ist von Zachi!")
print(''.join(secrets.choice(chars) for _ in range(40)))
input("Press Enter to continue...")
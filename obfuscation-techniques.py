import base64
import hashlib

def rot13(s):
  result = ''
  for char in s:
    if char.isalpha():
      shift = 13 if char.lower() < 'n' else 13
      result += chr(ord(char) + shift)
    
    else:
      result += char
  
  return result

# Encoding strings with base64
def encode_base64(self):
  return base64.b64encode(self.encode()).decode()

# Decoding string with base64
def decode_base64(self):
  return base64.b64decode(self.encode()).decode()

# Hasting strings with SHA-256 for one way obfuscation
def hash_sha256(self):
  return hashlib.sha256(self.encode()).hexdigest()

# String to obfuscate
original_string = "This is a secret message!"

# Using the obfuscation techniques
obfuscation_rot13 = rot13(original_string)
obfuscation_base64 = encode_base64(obfuscation_rot13)
obfuscation_sha256 = hash_sha256(obfuscation_base64)

# Obfuscation outputs
print(f"ROT13: {obfuscation_rot13}")
print(f"Base 64 Encoded: {obfuscation_base64}")
print(f"SHA-256 Hash: {obfuscation_sha256}")
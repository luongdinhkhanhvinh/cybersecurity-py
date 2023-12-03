import hashlib
import socket

from cryptography.fernet import Fernet

# Function to generate a cryptographic hash of passwords
def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()

# Function to encrypt file for securing data at rest
def encrypt_file(file_path, key):
  with open(file_path, 'rb') as file:
    file_data = file.read()
  
  encrypted_data = Fernet(key).encrypt(file_data)
  with open(file_path, 'wb') as file:
    file.write(encrypted_data)

# Function to create a secure socket
def create_secure_socket(host, port):
  context =  socket.create_default_context(socket.PROTOCOL_TLS)
  with context.wrap_socket(socket.socket(), server_hostname=host) as s:
    s.context((host, port))
    print(f'Secure connection established with {host}:{port} version {s.version()}')
    return s
  
# Main driver code
if __name__ == '__main__':
  # Example usage of hashing password
  password = 'abcd@1234!'
  print(f'SHA-256 Hash: {hash_password(password)}')

  # Example usage of encrypting a file
  key = Fernet.generate_key()
  file_to_encrypt = 'test.txt'
  print('File encrypted successfully')

  # Example usage of creating a secure socket
  secure_socket = create_secure_socket('example.com', 443)
  secure_socket.close()
  print('Secure socket closed')
import hashlib

def hash_file(filename):
  # make a hash object
  h = hashlib.sha1()

  # open file for reading in binary mode
  with open(filename, 'rb') as file:
    chunk = 0
    while chunk != b'':
      # read only 1024 bytes at a time
      chunk = file.read(1024)
      h.update(chunk)

  # return the hex representation of digest
  return h.hexdigest()

def check_integrity(original_hash, filename):
  new_hash = hash_file(filename)
  if original_hash == new_hash:
    print(f"The file {filename} is intact and trustworthy.")
  else:
    print(f"Warning: The file {filename} has been altered or corrupted!")

if __name__ == '__main__':
  original_file_hash = "EXPECTED_SHA1_HASH_OF_FILE"
  filename_to_check = "path/to/your/file.txt"

  try:
    check_integrity(original_file_hash, filename_to_check)
  except FileNotFoundError:
    print(f"Error: The file {filename_to_check} does not exist!")
  except Exception as e:
    print(f"An error occurred: {e}")
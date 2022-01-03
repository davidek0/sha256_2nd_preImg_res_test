import time
import random
import string
from hashlib import sha256


string_list = []
time_limit = 18000.0        # five hours time limit (18000 s).
list_size = 99
max_string_size = 10000     # No theoretical restriction except: x > 0. However very large strings will slow computation down significantly so restriction is practical.

# Generate some random string of random size in specified interval (param).
def GetRandomString(max_size):
    temp_str = ""
    for _ in range (random.randint(0, max_size)): temp_str += random.choice(string.ascii_letters)
    return temp_str

# Hash a string to its specific SHA-256 digest and return as hexadecimal.
def GenerateSHA256(inputstring: str): 
    digest = sha256(inputstring.encode())
    hxdigest = digest.hexdigest()
    return hxdigest

# Generate a list of randomly structured strings.
def RandomStringList(size: int) -> list: 
    for _ in range (size): string_list.append(GetRandomString(max_string_size))

def HashList(str_list: tuple) -> list:
    hash_list = [GenerateSHA256(j) for j in str_list]
    return hash_list



RandomStringList(list_size)
digest_list = HashList(tuple(string_list))
print(list(digest_list))


# We loop until we have found a perfect match:
time_start = time.time()
counter = 0.0
while 1:
    counter += 1
    
    temp_str = GetRandomString(max_string_size)
    temp_hash = GenerateSHA256(temp_str)
    print(temp_hash)

    # If a collision is found, then we have proven the SHA-256 hash function to be non-secure.
    if temp_hash in digest_list:
        print(f"Hash collision found, digest: {temp_hash} had initial input '{string_list[digest_list.index(temp_hash)]} ' which collides with '{temp_str}'.")
        
        end_time = time.time() - time_start
        print(f"Total time lapsed: {str(end_time // 3600)} hours, {str((end_time % 3600) // 60)} minutes, {str(end_time % 60)} seconds.")
        print(f"Total attempts: {str(counter)}")
        break
    
    else:
        if (time.time() - time_start) > time_limit:
            print(f"No collision found for set limit: {str(time_limit // 3600)} hours, {str((time_limit % 3600) // 60)} minutes, {str(time_limit % 60)} seconds.")
            print(f"Total attempts: {str(counter)}")
            break
        

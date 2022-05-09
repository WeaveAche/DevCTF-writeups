import hashlib

salt = "f789bbc328a3d1a3"

i = 0
while 1:
    password = f"{salt}{i}"
    
    result = hashlib.md5(password.encode())
    hash = result.hexdigest()

    if hash.startswith("0e"):
        if hash[2:].isdigit():
            print(i)
            break

    i+=1

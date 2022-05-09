# ScientificHashes
Everything about the challenge screams PHP type juggling. First hint says to get some salt. After carefully seeing the cookie in response, 
we find the salt to be `f789bbc328a3d1a3`. After that we can write a python script to get a valid password

```python
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
```

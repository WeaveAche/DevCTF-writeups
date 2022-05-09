**(Caution: very lazy writeup ahead)** 
Open the .dll file in IDA pro.

# Payload
![payload](payload.png)

# Mutex
![mutex](mutex.png)

# WhichAddress?
![wa](wa.png)

# Privileged
![priv](priv.png)

# LevelUp
![levelup](levelup.png)

The `WriteProcessMemory()` call writes the payload into memory. The application is given
by the `pszPath` in `CreateProcessA`. The path was obfuscated a bit, but was easy to reverse.

![pszPath](pszPath.png)

# DropThis
![hmm](hmm.png)

![sus](sus.png)

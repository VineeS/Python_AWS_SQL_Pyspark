## steps before running the fast API

1. make sure in requiements.txt you have fastapi and uvicorn
   ex: fastapi==0.75.1
   uvicorn==0.17.6

2. write the code in main.py
   from fastapi import FastAPI
   import uvicorn
   from myLib.logic import wiki
   from myLib.logic import search_wiki

app = FastAPI()

@app.get("/")
async def root():
return {"message": "Wiki API call. Call /search or /wiki"}

@app.get("/search/{value}")
async def add(num1: int, num2: int):
"""Page to search"""

    result = search_wiki(value)
    return {"result": result}

if **name** == '**main**':
uvicorn.run(app, port=8080, host='0.0.0.0')

### 1. error below can be resolved my checking what all services are running in your loccal machine

2. command 1 -> ps -ef |grep jenkins (I checked jenkins as jenkins was running on this port)
3. Vinees-MBP:~ vinee$ ps -ef |grep jenkins
   501 657 1 0 31May24 ?? 12:28.89 /usr/local/opt/openjdk/bin/java -Dmail.smtp.starttls.enable=true -jar /usr/local/opt/jenkins-lts/libexec/jenkins.war --httpListenAddress=127.0.0.1 --httpPort=8080
   501 10106 10072 0 12:26PM ttys004 0:00.01 grep jenkins
4. Vinees-MBP:~ vinee$ kill -9 657
5. Vinees-MBP:~ vinee$ ps -ef |grep jenkins
   501 10111 10072 0 12:26PM ttys004 0:00.00 grep jenkins
6. Vinees-MBP:~ vinee$ lsof -i :8080
   COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
   Python 9927 vinee 10u IPv4 0x7ea65c15093a49e5 0t0 TCP \*:http-alt (LISTEN)
   Python 9927 vinee 13u IPv4 0x7ea65c15093a7825 0t0 TCP localhost:http-alt->localhost:53996 (CLOSE_WAIT)
7. checking if other port is available :
   Vinees-MBP:~ vinee$ lsof -i :8081
   Vinees-MBP:~ vinee$ kill -9 9927
   Vinees-MBP:~ vinee$ kill -9 9927

#### 2. Now run the 'python main.py' command and the code run go to browser and check http://0.0.0.0:8080 as mentioned below

(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces % python main.py
INFO: Started server process [10175]
INFO: Waiting for application startup.
INFO: Application startup complete.
ERROR: [Errno 48] error while attempting to bind on address ('0.0.0.0', 8080): address already in use
INFO: Waiting for application shutdown.
INFO: Application shutdown complete.

(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces %
[6] + killed python main.py
(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces % python main.py
WARNING: You must pass the application as an import string to enable 'reload' or 'workers'.
(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces % python main.py
INFO: Started server process [10272]
INFO: Waiting for application startup.
INFO: Application startup complete.
INFO: Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO: 127.0.0.1:54245 - "GET / HTTP/1.1" 200 OK

## if you have any error need to kill and restart go to terminal -->

Vinees-MBP:~ vinee$ lsof -i :8080
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
Python 10272 vinee 10u IPv4 0x7ea65c15093a6c95 0t0 TCP _:http-alt (LISTEN)
Vinees-MBP:~ vinee$ kill -9 10272
Vinees-MBP:~ vinee$ lsof -i :8080
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
Python 10736 vinee 10u IPv4 0x7ea65c1506157ad5 0t0 TCP _:http-alt (LISTEN)
Vinees-MBP:~ vinee$ kill -9 10739
-bash: kill: (10739) - No such process
Vinees-MBP:~ vinee$ kill -9 10736
Vinees-MBP:~ vinee$

## now search for http://0.0.0.0:8080/wiki/Barack Obama in the browser you will get the output

## you can also go to browser and query http://0.0.0.0:8080/docs

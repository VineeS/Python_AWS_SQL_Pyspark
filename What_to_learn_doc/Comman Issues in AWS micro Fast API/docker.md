(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces % make build
docker build -t deploy-fastapi .
[+] Building 0.2s (2/2) FINISHED docker:desktop-linux
=> [internal] load build definition from Dockerfile 0.0s
=> => transferring dockerfile: 212B 0.0s
=> ERROR [internal] load metadata for docker.io/library/python:3.12-slim-bookworm 0.1s

---

> [internal] load metadata for docker.io/library/python:3.12-slim-bookworm:

---

## Dockerfile:1

1 | >>> FROM python:3.12-slim-bookworm
2 |  
 3 | RUN mkdir -p /app

---

ERROR: failed to solve: python:3.12-slim-bookworm: failed to resolve source metadata for docker.io/library/python:3.12-slim-bookworm: error getting credentials - err: exec: "docker-credential-desktop": executable file not found in $PATH, out: ``
make: \*\*\* [build] Error 1

### had an error while downloading the image hence did a manual pull

(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces % docker pull python:3.12-slim-bookworm

3.12-slim-bookworm: Pulling from library/python
2cc3ae149d28: Pull complete
87c0edd565e2: Pull complete
f0485792db2a: Pull complete
d50c9bebe690: Pull complete
eda5c9531256: Pull complete
Digest: sha256:2fba8e70a87bcc9f6edd20dda0a1d4adb32046d2acbca7361bc61da5a106a914
Status: Downloaded newer image for python:3.12-slim-bookworm
docker.io/library/python:3.12-slim-bookworm

What's next:
View a summary of image vulnerabilities and recommendations → docker scout quickview python:3.12-slim-bookworm
(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces % make build  
docker build -t deploy-fastapi .
[+] Building 20.0s (10/10) FINISHED docker:desktop-linux
=> [internal] load build definition from Dockerfile 0.0s
=> => transferring dockerfile: 212B 0.0s
=> [internal] load metadata for docker.io/library/python:3.12-slim-bookworm 0.0s
=> [internal] load .dockerignore 0.0s
=> => transferring context: 2B 0.0s
=> [1/5] FROM docker.io/library/python:3.12-slim-bookworm 0.1s
=> [internal] load build context 0.2s
=> => transferring context: 247.26kB 0.1s
=> [2/5] RUN mkdir -p /app 0.4s
=> [3/5] COPY . main.py /app/ 0.1s
=> [4/5] WORKDIR /app 0.0s
=> [5/5] RUN pip install -r requirements.txt 18.7s
=> exporting to image 0.7s
=> => exporting layers 0.7s
=> => writing image sha256:45122ae3946b37c90d4960a14ee95d96d502febed2f1a8782950a112ce3ce605 0.0s
=> => naming to docker.io/library/deploy-fastapi 0.0s

What's next:  
 View a summary of image vulnerabilities and recommendations → docker scout quickview

### take the image ID to put in makefile --> run docker command select deploy-fastapi

(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces % docker image ls
REPOSITORY TAG IMAGE ID CREATED SIZE
deploy-fastapi latest 45122ae3946b 2 minutes ago 207MB
python 3.12-slim-bookworm be56959c9ae6 2 weeks ago 130MB
hyperledger/fabric-ca 1.5 4ea287b75c63 2 years ago 69.8MB
hyperledger/fabric-ca 1.5.2 4ea287b75c63 2 years ago 69.8MB
hyperledger/fabric-ca latest 4ea287b75c63 2 years ago 69.8MB
hyperledger/fabric-tools 2.3 98fa0bfb0fd2 2 years ago 445MB
hyperledger/fabric-tools 2.3.3 98fa0bfb0fd2 2 years ago 445MB
hyperledger/fabric-tools latest 98fa0bfb0fd2 2 years ago 445MB
hyperledger/fabric-peer 2.3 a491b5ab42f6 2 years ago 53.3MB
hyperledger/fabric-peer 2.3.3 a491b5ab42f6 2 years ago 53.3MB
hyperledger/fabric-peer latest a491b5ab42f6 2 years ago 53.3MB
hyperledger/fabric-orderer 2.3 9e1952b8840d 2 years ago 35.4MB
hyperledger/fabric-orderer 2.3.3 9e1952b8840d 2 years ago 35.4MB
hyperledger/fabric-orderer latest 9e1952b8840d 2 years ago 35.4MB
hyperledger/fabric-ccenv 2.3 56fa403e02ee 2 years ago 502MB
hyperledger/fabric-ccenv 2.3.3 56fa403e02ee 2 years ago 502MB
hyperledger/fabric-ccenv latest 56fa403e02ee 2 years ago 502MB
hyperledger/fabric-baseos 2.3 b35a8ef578c0 2 years ago 6.87MB
hyperledger/fabric-baseos 2.3.3 b35a8ef578c0 2 years ago 6.87MB
hyperledger/fabric-baseos latest b35a8ef578c0 2 years ago 6.87MB
couchdb 3.1.1 90b214af2436 2 years ago 191MB
node-docker latest 395ec281dd8e 3 years ago 1.52GB
<none> <none> 49df1e5f467f 3 years ago 1.52GB
bitnami/postgresql 10-debian-10 9ae38fe470c2 3 years ago 257MB
bitnami/airflow-scheduler 2-debian-10 09236716079a 3 years ago 1.16GB
bitnami/redis 6.0-debian-10 b877fdea107e 3 years ago 103MB
bitnami/airflow 2-debian-10 1f711411de72 3 years ago 1.2GB
bitnami/airflow-worker 2-debian-10 3ed7768b3cdd 3 years ago 1.16GB
ethereum/solc 0.8.0-alpine 10133f38d330 3 years ago 15.6MB
ethereum/solc 0.8.0 681c2f666868 3 years ago 9.98MB
ethereum/solc 0.7.6 abd8e7884857 3 years ago 9.9MB
ubuntu bionic 2c047404e52d 3 years ago 63.3MB
docker101tutorial latest 6612e1ef4af9 3 years ago 26.8MB
<none> <none> aedd5e12d2d0 3 years ago 123MB
<none> <none> 13523ed435a5 3 years ago 224MB
<none> <none> 7019733573a7 3 years ago 110MB
mysql latest 5ac22cccc3ae 3 years ago 544MB
python alpine fbfb63e3c6bb 3 years ago 80.3MB
nginx alpine ecd67fe340f9 3 years ago 21.6MB
node 12-alpine 057fa4cc38c2 3 years ago 89.3MB
mcr.microsoft.com/mssql/server 2019-latest d2520a2df464 4 years ago 1.51GB
ethereum/solc 0.6.3 b22648333a2e 4 years ago 8.42MB
microsoft/mssql-server-linux latest 314918ddaedf 5 years ago 1.35GB
(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces %

## once everything is up and running

(.venv) vinee@Vinees-MBP Python-AWS-FastAPI-microservicces % make run
#run docker
docker run -p 127.0.0.1:8080:8080 45122ae3946b
INFO: Started server process [1]
INFO: Waiting for application startup.
INFO: Application startup complete.
INFO: Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)

### while running phrases I got an error hence added the below

RUN python -m textblob.download_corpora to requiement.txt

### also you can run into issues like

docker: Error response from daemon: driver failed programming external connectivity on endpoint hopeful_gagarin (d7b5ffb3da47df89f63de947480d66a54ba8fb18f6934ee0f7997542caf1dac9): Bind for 127.0.0.1:8080 failed: port is already allocated.

that time you need to kill the localhost

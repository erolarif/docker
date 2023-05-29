
# DOCKER
- Docker is a technology used to eliminate problems such as version incompatibilities and library issues that may occur when multiple people are working on software projects. It enables software projects to be developed, tested, and distributed quickly.

![Uygulama Ekran Görüntüsü](https://developers.redhat.com/sites/default/files/styles/article_feature/public/blog/2014/05/homepage-docker-logo.png?itok=zx0e-vcP)


# Run The Project On Your Own

## Installing Docker On Ubuntu
- You can follow the steps in the link below in order to set up Docker. You should follow the steps in Post-installation steps in the link.

Link : [LINK](https://docs.docker.com/engine/install/ubuntu/)

## Installıng Git on Ubuntu
- To install Git on your computer you can run the command below.

```bash
sudo apt-get install git-all
```


## Cloning To GitHub Repository
```bash
git clone ....
```
## Build 
- To build the Dockerfile you should run the command below in the file which is cloned from the repostory.
```bash 
docker build -t port_mapping_test . 
```
## Run
- To run the docker image run command can be used.
- -it (interactive terminal) allows you to interact with the container's shell or command prompt, similar to how you would interact with a terminal on a local machine. Without -it command it typically starts in the background, and you don't have direct access to the container's terminal.
- --rm (remove) 

```bash
docker run -it --rm port_mapping_test
```

# Dockerfile

```Dockerfile
FROM ubuntu:latest    #Main image folder is ubuntu image
RUN apt-get update
RUN apt install -y python3-pip
RUN mkdir /app.
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
````



# Examples Script Examples

- The Transmitter Code is given below. This code will be run in docker container. 

```python
# Transmitter Code
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({'message': 'Hello! I am coming from Docker container.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
```


- Receiver code is given below. This code will be run in your computer.

```python
# Receiver Code

import requests

response = requests.get('http://localhost:5000')
print(response.json())
```

- First run the Trasnmitter code in the docker container. After that when you run the receiver code there will be a communication between your docker container and computer.


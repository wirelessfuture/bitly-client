# bitly-client
A simple web app that allows the user to shorten and expand URL's. 

## GET requests
Users can send a GET request to 0.0.0.0:5000, sending a GET request with the
parameters: method, url will return an application/json response. Sending a GET
request without url parameters will render the user input form instead. 

## POST requests
When the user input form is submitted it uses a POST request with an internal Flask listener to process the request, and will return an application/json response.

## Installation

#### Manual Installation
1. Install latest version of Python > https://www.python.org/downloads/
2. Install the latest version of GIT > https://git-scm.com/downloads
3. CD into desired directory and then run `git clone https://github.com/wirelessfuture/bitly-client.git`
4. Install virtualenv - run `pip install virtualenv`
5. Create a virtualenv - `virtualenv venv`
6. Activate the virtualenv: On Linux run `source venv/bin/activate` On Windows run `venv\Scripts\activate`
7. Run `pip install -r requirements.txt` to install all required packages
8. Run `python main.py` to start the server

#### Docker Image
I have provided a dockerhub repo for ease of installation:
1) Simply install docker > https://docs.docker.com/get-docker/
2) run `docker pull dispatj/bitly-client && docker run -p 5000:5000 dispatj/bitly-client`

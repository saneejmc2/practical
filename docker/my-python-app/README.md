Build the docker image:



docker build -t my-python-app:1.0 .





Remove the old container in case:

docker rm my-python-app





Run the Docker image:



docker run -d --name my-python-app -p 5000:8080 my-python-app:1.0



check the docker:

docker ps





Open a web browser:

http://localhost:5000



or in command line: curl http://localhost:5000


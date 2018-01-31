# jr-sre-homework

While extensive experience with the following technologies is not a pre-requisite for this position, a basic understanding or the ability to come up to speed quickly is. We've designed this homework to demonstrate a minimal skill set that we believe is required to be successful in this position.  

We value your time and expect this this homework will take less than two hours to complete from start to finish. Please do not go beyond this time limit or submit work product outside the scope of the questions below. Bonus questions are not required. 

Please fork this repo to a private repo in your personal GitHub account. Answer each question inline or in appropriately named files added to the repo. Submit a pull request when completed. Be prepared to discuss your answers in detail during an on-site homework review. 

## Docker
### Setup 
You will require access to any machine running a current version of Docker and a connection to the internet for downloading a small hello-world image. 


$ docker pull hello-world 
### Question 1: 
When troubleshooting problematic docker containers, it's useful to know what command is executing when the container is started.  What command (CMD) is run when starting the hello-world container? 


$ docker run --rm hello-world 

### Question 2:
What are the contents of the /etc/resolv.conf file in the container? 

### Bonus 1 (not required):
Submit a program, written in the language of your choice, that takes the image name as input and outputs the answer to the previous questions. 

## AWS
### Setup 
You will require access to an AWS account and access to a machine with the AWS CLI installed. 

### Question 3: 
Submit an AWS CLI command to launch a new EC2 instance. 

### Question 4: 
Submit an AWS CLI command to describe the EC2 instance launched in Question 3.  Output should include only the LaunchTime, InstanceId, and State.Name and be presented in tabular format. 

### Bonus 2 (not required): 
Submit a program, written in the language of your choice, that uses an AWS SDK and performs the same work as Questions 3 and 4. 


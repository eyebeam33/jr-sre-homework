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

__A1:__	`CMD=/hello`

### Question 2:
What are the contents of the /etc/resolv.conf file in the container? 

__A2:__ The file is empty

### Bonus 1 (not required):
Submit a program, written in the language of your choice, that takes the image name as input and outputs the answer to the previous questions. 

_See_ `qash.sh`

## AWS
### Setup 
You will require access to an AWS account and access to a machine with the AWS CLI installed. 
```
$ aws ec2 create-vpc --cidr-block 10.0.0.0/16
VPC     10.0.0.0/16     dopt-d72133b3   default False   pending vpc-a579c4dc

$ aws ec2 create-subnet --vpc-id vpc-a579c4dc --cidr-block 10.0.0.0/24
SUBNET  us-west-2c      251     10.0.0.0/24     pending subnet-9123f9cb vpc-a579c4dc

$ aws ec2 create-key-pair --key-name xwood --query 'KeyMaterial' --output text > xwood.pem

$ chmod 400 xwood.pem 
```

### Question 3: 
Submit an AWS CLI command to launch a new EC2 instance. 

__A3:__
```
$ aws ec2 run-instances --image-id ami-7d3dc51d --count 1 --instance-type t2.micro --key-name xwood --subnet-id subnet-9123f9cb
899920520588    r-0adff61b9368f99d7
INSTANCES       0       x86_64          False   xen     ami-7d3dc51d    i-0c839c875d23e94e0     t2.micro        xwood      2018-02-04T21:38:52.000Z        ip-10-0-0-140.us-west-2.compute.internal        10.0.0.140              /dev/sda1  ebs     True            subnet-9123f9cb hvm     vpc-a579c4dc
MONITORING      disabled
NETWORKINTERFACES               0a:b9:47:c3:bb:ae       eni-635ce364    899920520588    10.0.0.140      True    in-use     subnet-9123f9cb vpc-a579c4dc
ATTACHMENT      2018-02-04T21:38:52.000Z        eni-attach-7ec13886     True    0       attaching
GROUPS  sg-17fa2668     default
PRIVATEIPADDRESSES      True    10.0.0.140
PLACEMENT       us-west-2c              default
SECURITYGROUPS  sg-17fa2668     default
STATE   0       pending
STATEREASON     pending pending
```

### Question 4: 
Submit an AWS CLI command to describe the EC2 instance launched in Question 3.  Output should include only the LaunchTime, InstanceId, and State.Name and be presented in tabular format. 

__A4:__
```
$ aws ec2 describe-instances --instance-id i-0c839c875d23e94e0 --query 'Reservations[*].Instances[*].[LaunchTime,InstanceId,State.Name]'
2018-02-04T21:38:52.000Z        i-0c839c875d23e94e0     running
```

### Bonus 2 (not required): 
Submit a program, written in the language of your choice, that uses an AWS SDK and performs the same work as Questions 3 and 4. 

_See_ `awscli.py`

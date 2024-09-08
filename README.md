# Devops Project 

>## Build a Python Flask App and Deploy Using AWS Elastic Beanstalk
>>### • Procedure:
>> 1. Develop a simple Python Flask application.
>> 2. Install the AWS Elastic Beanstalk CLI and initialize the environment.
>> 3. Deploy the Flask application using Elastic Beanstalk.
>> 4. Monitor and scale the application using the AWS Management Console.

> [!IMPORTANT]
> For best practice of python web app hosting on AWS , i followed some steps
> 1. Hosting through AWS ec2
> 2. Re-Hosing through AWS Elastic Beanstlak 

## Table of Contents

1. [Introduction](#introduction)
2. [Instance Lunching](#Instance-Lunching)
3. [Setup-virtual-enironment](setup-venv)
4. [Py app Setup](#app-setUp)



## Introduction

This guide will walk you  through the process of deploying a python Flask application on AWS ec2 and also AWS Elastic Beanstalk , a fully managed service that allows you to easily deploy and managed applications in the cloud.

## Instance-Lunching

> Before you begin , ensure you have AWS account if not then first create it.

- Goto Search bar and write `ec2` and Select the EC2 option 
    ![Search Bar Screenshots](/images/searchbar.webp)

- Click on `Launch instance` Button 
![lunch instance Screenshots](/images/lunch_instance.webp)


- Give name of the Instance
![Instance Name giving Screenshots](/images/instance-Name.webp)


- On Application and OS Images -> Select `Amazon Linux `

- On Instance type -> select t2.micro (free tier eligible (for practice purpose))

- Select `Key pair` for connecting through locally  and for security Purpose'
> [!NOTE]
> if you Don't have Key Pair then must create new [Key Pair](#key-pair)

- On Network setting, Check some Steps
1. Auto-assign public Ip --> Enable ? if not then click on `edit` of Network setting and Enabled it.
2. Allow SSH traffic from Anywhere 
3. Allow HTTP and HTTPS traffic from the internet

![Network Security Screenshots](/images/network_security.webp)


- Click on `Launch instance` -> Bottom Right  


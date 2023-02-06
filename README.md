# Airline Flight Fare Prediction
<img src = "https://github.com/atanu-1991/Data/blob/main/flight_fare_pred.jpg" alt="MLBC">

![Python 3.10](https://img.shields.io/badge/Python-3.10-brightgreen.svg) ![Scikit-Learn](https://img.shields.io/badge/Library-ScikitLearn-orange.svg)  
This repository consists of files required for end to end implementation and deployment of Machine Learning Flight Fare Prediction web application created with Flask and deployed on the AWS Platform.

## Table of Contents
  * [App Link](#app-link)
  * [About the App](#about-the-app)
  * [Deployement on AWS](#deployement-on-aws)
  * [Technologies Used](#technologies-used)


## App Link
If you want to view the deployed model, click on the following link:<br />
[URL](http://flightfare-env.eba-y2mpi355.ap-south-1.elasticbeanstalk.com/)

## About the App  
The Airline Flight Fare Prediction is a Flask web application to predict airline flight fares across the Indian cities. The dataset for the project is a time-stamped dataset so, while building the model, extensive pre-processing was done on the dataset especially on the date-time columns to finally come up with a ML model which could effectively predict airline fares across various Indian Cities. 
The dataset had many features which had to pre-processed and transformed into new parameters for a cleaner and simple web application layout to predict the fares. The various independent features in the dataset were: 

Airline: The name of the airline.

Date_of_Journey: The date of the journey

Source: The source from which the service begins.

Destination: The destination where the service ends.

Route: The route taken by the flight to reach the destination.

Dep_Time: The time when the journey starts from the source.

Arrival_Time: Time of arrival at the destination.

Duration: Total duration of the flight.

Total_Stops: Total stops between the source and destination.

Additional_Info: Additional information about the flight

Price: The price of the ticket

## Deployement on AWS

### The WebApp was deployed to AWS Elastic Beanstalk
* Create a new folder named ".ebextensions"
* In that folder create a file <any_name>.config (* Make sure the extension is .config)
* Above file should contain the following
```bash
 option_settings:
  "aws:elasticbeanstalk:container:python":
    WSGIPath: <main python file name>:<flask app name>
```
* Make a zip file with all necessary files and folder
* Login to AWS
* Search for `Elastic Beanstalk` and click `Create Application`
* Give any valid name, select platform and upload the zip file. Finally click on **Create Application** and you will find a url

### CI/CD Pipeline using GitHub actions for the application hosted via AWS Elastic BeanStalk

We have already deployed our Flask App and got the [url](http://flightfare-env.eba-y2mpi355.ap-south-1.elasticbeanstalk.com/)

Now, we need to develop a CI/CD Pipeline so that when ever we push a new update for our App, it will automatically get deployed and reflect those changes on the same url.

Below Steps Have Followed:
* Create <any_name>.yml file in the folder .github/workflows/.
* Mention all the actions to be executed with a particular trigger (say git push)
* Create AWS IAM User with any name and set necessary permissions
* After creating IAM User a csv file will be generated with AWS_ACCESS_KEY_ID and AWS_ACCESS_KEY_ID
* In git repo go to settings -> secrets -> actions -> New Repo Secrets
* Save secrets named AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY_ID and AWS_REGION with respective values from the downloaded csv file.
* Create a S3 Bucket with same AWS Region.
* Commit code in Github and it will automatically start deploy code in AWS

## Technologies Used
![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/)[<img target="_blank" src="https://github.com/get-icon/geticon/raw/master/icons/aws.svg" width=200 height=90>](https://aws.amazon.com/)[<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/)

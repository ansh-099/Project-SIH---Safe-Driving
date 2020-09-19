# Safe Driving
![Build Status](https://travis-ci.org/rob729/Minimal_ToDo.svg?branch=master)
![Codacy Badge](https://api.codacy.com/project/badge/Grade/346c2ba7d2d841a48fc83734e3d2d682)
![Maintainability](https://api.codeclimate.com/v1/badges/c462858751a234cdcd08/maintainability)
[![Platform](https://img.shields.io/badge/platform-android-blue.svg)](http://developer.android.com/index.html)
[![API](https://img.shields.io/badge/API-21%2B-blue.svg?style=flat)](https://android-arsenal.com/api?level=21)

## Team - Dream Slayers
Driving a car is a complex, multifaceted and potentially risky activity requiring full mobilization of physiological and cognitive resources to maintain performance over time. Any loss of these resources can have dramatic consequences, including accidents. Moreover, the promise of autonomous vehicles makes it even more important to determine the driver’s operational state. This has recently generated a large number of studies, both from the fundamental perspective and with a view to potential applications.

## Challenge
Not just detecting but also predicting impairment of a car driver’s operational state is a challenge. This study aims to determine whether the standard sources of information used to detect drowsiness can also be used to predict when a given drowsiness level will be reached. The challenge is ambitious: not only detecting, but also predicting, degradation in the driver’s operational state.
## Working

* Machine learning model for predicting optimal velocity to avoid collision.
* ML model deployed at server https://alertme123.herokuapp.com/api 
* Android App (AlertMe) providing functionality: notification when in high danger zone,demarcating areas on map accoring to accidents  data , performing a HTTP POST request to the server to make predictions.
* An alternative mathematical model for avoiding collisions by taking into consideration distance vectors , velocity vectors and their dot products . A GUI simulation was made for the same using using matplotlib. 
* You can check the pdfs included for complete details.

<table>
        <tr>
<td><img src = "https://user-images.githubusercontent.com/35291991/88955373-757b0280-d2b9-11ea-86a8-7bda034c4461.png" height = "460" width="240"></td>
<td><img src = "https://user-images.githubusercontent.com/35291991/93025610-cbfb9080-f61c-11ea-80ad-9760c3140535.png" height = "460" width="240"></td>
<td><img src = "https://user-images.githubusercontent.com/35291991/93025176-75d91e00-f619-11ea-9f5d-951b5bd51e95.png" height = "460" width="240"></td>
        </tr>
        <tr>
<td><img src = "https://user-images.githubusercontent.com/35291991/93025201-9d2feb00-f619-11ea-98c0-58a26ebbe116.png" height = "460" width="240"></td>
<td><img src = "https://user-images.githubusercontent.com/35291991/93025207-aa4cda00-f619-11ea-84b5-789439a3fcbe.png" height = "460" width="240"></td>
<td><img src = "https://user-images.githubusercontent.com/35291991/93025128-08c58880-f619-11ea-9b2b-9f41b8c149ad.png" height = "460" width="240"></td>
        </tr>
</table> 
</br>


### Get Directions 

* Get Disclaimer about your area .i.e. in a risky area or not. </br>
* Get to know What should be your best velocity. </br>

### Tech Stack Used
* [Keras](https://keras.io/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Heroku](https://www.heroku.com/)
* [Firebase](https://firebase.google.com/docs)
* [Google Maps API](https://developers.google.com/maps/documentation)


Cheers!

# BuildWeek-2

<!-- PROJECT LOGO -->
<p align="center">
<!--   <a href="https://github.com/othneildrew/Best-README-Template"> -->
    <img src="https://www.saggiamente.com/wp-content/uploads/2019/08/newlogoandroid.png" alt="Logo" width="120" height="80">
  </a>

  <h1 align="center">TRANSPORT TRACKER</h1>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#data-description">Data Description</a>
    </li>
    <li>
      <a href="#goal-of-this-project">Goal of this project</a>
    </li>
    <li>
      <a href="#project-plan">Project plan</a>
    </li>
      <li>
      <a href="#future-plans">Future Plans</a>
    </li>
    <li>
      <a href="#the-team">The Team</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
We are the **Huawei Watch Team** from [Strive School](https://strive.school/), and this is a project from our second build week (18-21/5/2021) out of many more to come in the course of our **AI Engineering specialization program**. For this project, we have been tasked to build a functioning machine learning model out of some fitness data that was collected from users on an andriod fitness app. You can find the original dataset [here](https://tempesta.cs.unibo.it/projects/us-tm2017/download.html)

<p align="center">
<img src="https://user-images.githubusercontent.com/27528504/119107723-cb26c400-ba1f-11eb-8bb6-77ba3ff42570.png" width="500" height="400">
</p>



<!-- GETTING STARTED -->

### Data Description

The dataset was developed by a [team of collaborators from the Univsersity of Bologna](https://tempesta.cs.unibo.it/projects/us-tm2017/tutorial.html#raw_data), and is based on 13 users who collected the data during their daily activities. The dataset includes all sensors available in phones such as accelerometer, gyrometer, etc., and distinguishes five transportation modes: 
/ being on a car
/ on a bus
/ on a train
/ standing still
/ walking.


### Goal of this project
* Our goal is to build a model with incredible accuracy in as many activity classes as possible.  


## Project plan

* Download and pre-process the data according to our needs
* Perform EDA(Exploratory Data Analysis) to find insights
* Perform Feature Engineering
* Create Machine Learning pipeline and run the data on multiple classifiers
* Choose the best classifier and find the accuracy on test_data
* Create a time series model which predicts the class for every 1 sec
* Calculate necessary parameters like speed, calorie count etc.

## Future plans
* As the model currently functions as a time series and continously predicts the type of transportation for a given time, we can extend it so that we can keep a track of the walking time of a person and possibly extend it as a fitness tracker.


<!-- CONTACT -->
## The Team:

| Contributors | Tasks | LINKEDIN|
| ------ | ------ | ------ |
| Nurlan_Sarkhanov | Mode development| [https://www.linkedin.com/in/nurlan-sarkhanov-8749a698/]|
| Lakshmipathi rao Devalla| Model development | [https://www.linkedin.com/in/devalla-lakshmipathirao/] |
| Olatunde Salami  | Feature Engineering | [https://www.linkedin.com/in/olatunde-salami/] |
| Agathiya Raja | Feature Engineering | [https://github.com/AgathiyaRaja]|
| Thanh Nguyen | Streamlit & Github | [https://www.linkedin.com/in/nguyenphuocxuanthanh/ |




# Software Engineering for Machine Learning Assignment

(a) Clear documentation for your API. (How it should be called, what data it expects, any pre-conditions for the service, and how to understand the output).

How it should be called:
<br></br>
To call the model, you will go to this link on a browser or curl on the terminal with the following syntax: 
"http://localhost:5000/predict?health={value}&absences={value}&studytime={value}&freetime={value}&famrel={value}&failures={value}"
where one replaces any "{value}" statements with the corresponding query value for the feature.

Expected Data:
<br></br>
It expects data based on the health of the student, the number of absences of the student, the study time of the student (on a scale of 1 to 5), the free time of the student (on a scale of 1 to 5), the quality of the family relationships of the student (on a scale of 1 to 5), and the number of failures of past classes of the student (0 to 3 if n <=3, 4 otherwise). 

Pre-conditions for Service:
<br></br>
No pre-conditions for calling this microservice except that the data is within the expected parameters.

Understanding the Output:
<br></br>
It should return a binary value where 1 means that the student is a quality student and 0 means that they are not a quality student

(b) A description of which features you used in training your model, and how your retrained the model performs better than the baseline model

For our model, we are utilizing the features of health, absences, failures, studytime, freetime, and family relations. 
<br></br>
Description of features:
<br></br>
Health - current health status (where 1 = very bad and 5 = very good)
<br></br>
Absences - number of school absences (0 to 93)
<br></br>
Failures - number of past class failures (0 to 3 if n <= 3, otherwise 4)
<br></br>
Studytime - weekly study time (1 = <2 hours, 2 = 2-5 hours, 3 = 5-10 hours, or 4 = >10 hours)
<br></br>
Freetime - free time after school (where 1 = very low and 5 = very high)
<br></br>
Family relations - quality of family relationships (where 1 = very bad and 5 = excellent)
<br></br>

How we retrained the model:
<br></br>
The baseline model utilized the features of health, age, and absences, which aren't necessarily the best indicators of performance success in graduate programs. Thus, we retrained our model utilizing what we thought might be better indicators such as their health (they could possibly not do as well if unhealthy), absences (if they miss class a lot, they are bound to do worse), failures (if they have failed in the past, they are more likely to fail), study time (if they study more, then they will tend to do better), free time (less free time is less time to focus on their studies), and family relationships (this might be a distractor if its bad). Our retrained model still uses the random forest classifier. However, we have much better performance in terms of prediction. Our model had the F1 Score of 0.9 (or 90%) and the baseline model had the F1 score of 0.5 (or 50%). To clarify, F1 Score is the weighted average of Precision and Recall. Therefore, this score takes both false positives and false negatives into account.

(c) deployment instructions

To deploy our retrained model, follow these steps:
<br></br>
1. Clone our repository by running "git clone https://github.com/CMU-313/fall-2021-hw4-sleepygit"
2. Change the directory into the git repository downloaded and subsequently into the dockerfile directory by running "cd fall-2021-hw4-sleepygit/dockerfile"
3. Build the docker container by running "docker build -t ml:latest ."
4. Run the docker container by running "docker run -d -p 5000:5000 ml"
5. Finally, You can see the result when querying the micro service by opening a web browser and going to http://localhost:5000/predict and inputting the query values after the predict in the URL or you can output the result by running "curl http://localhost:5000/predict" and putting query values after predict as described in part (a). 

(d) an explanation and justification of the testing you have done on it.

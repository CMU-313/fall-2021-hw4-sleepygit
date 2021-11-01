# Software Engineering for Machine Learning Assignment

(a) Clear documentation for your API. (How it should be called, what data it expects, any pre-conditions for the service, and how to understand the output).

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
The baseline model utilized the features of health, age, and absences, which aren't necessarily the best indicators of performance success in graduate programs. Thus, we retrained our model utilizing what we thought might be better indicators such as their health (they could possibly not do as well if unhealthy), absences (if they miss class a lot, they are bound to do worse), failures (if they have failed in the past, they are more likely to fail), study time (if they study more, then they will tend to do better), free time (less free time is less time to focus on their studies), and family relationships (this might be a distractor if its bad). Our retrained model still uses the random forest classifier. However, we have much better performance in terms of prediction. Our model had a 90% successful classification of predicting quality of graduate students while the baseline model only had a 50%. 

(c) deployment instructions

(d) an explanation and justification of the testing you have done on it.

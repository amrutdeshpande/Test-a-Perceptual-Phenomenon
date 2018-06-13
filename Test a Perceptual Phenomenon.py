
# coding: utf-8

# ### Analyzing the Stroop Effect
# Perform the analysis in the space below. Remember to follow [the instructions](https://docs.google.com/document/d/1-OkpZLjG_kX9J6LIQ5IltsqMzVWjh36QpnP2RYpVdPU/pub?embedded=True) and review the [project rubric](https://review.udacity.com/#!/rubrics/71/view) before submitting. Once you've completed the analysis and write up, download this file as a PDF or HTML file and submit in the next section.
# 
# 
# (1) What is the independent variable? What is the dependent variable?

# Independent variable is the Test Condition i.e Congruent and Incongruent Condition. The Dependent variable is the Time taken to identify the colors of the words image or word data

# (2) What is an appropriate set of hypotheses for this task? What kind of statistical test do you expect to perform? Justify your choices.

# Null Hypothesis(H0) : The population mean of the time taken to identify Congruent data and Incongruent data is same. 
# Alternative Hypothesis(HA) : The population mean of the time taken to identify Incongruent color dataset is greater than the time taken to identify all the congruent color dataset.
# 
# H0: μ(Congruent) = μ(Incongruent)
# HA: μ(Incongruent) > μ(Congruent)
# 
# Statistical Test used:
# As we have each participant undergoing two tests and we need to show if the mean of Incongruent eradings is higher than the Congruent ones, so I choose paired one tail t-test with 95% Confidence Interval and α= 0.05 as the population is paired. 
# 
# Justification:
# One sided T test is chosen because the alternate hypothesis chosen is a "greater than" condition and "not a not equal to" condition. Also, as the population size is less than 30 and the population standard deviation is unknown which approximates normal distribution and thereby limiting the use of z-test.
# 
# 

# (3) Report some descriptive statistics regarding this dataset. Include at least one measure of central tendency and at least one measure of variability. The name of the data file is 'stroopdata.csv'.

# In[7]:


#Place dataset in current working directory and use pandas as pd

import pandas as pd
stroop = pd.read_csv("stroopdata.csv")

#print stroop
print(stroop)

#using describe fucntion gives some descriptive statistics 
stroop.describe()


# The central tendency is showed by the mean values of both the data column and vaiability can be estimated thought the standard deviation shown in the output above. Mean time to identify colors of Congruent data set is 14.05 whereas for Incongruent it is 22.06. Similarly the Standard deviation of Congruent set is 3.56 and Incongruent it is 4.80.

# (4) Provide one or two visualizations that show the distribution of the sample data. Write one or two sentences noting what you observe about the plot or plots.

# In[36]:


#import matplotlib library
import matplotlib.pyplot as plt
import numpy as np

import plotly.plotly as py

#plotting histogram of Congruent and Incongruent Data sets
stroop.hist()



# The Histogram plot shows the presence of postive skew in congruent as well as in Incongruent data set. It also gives a hint of approximate normal distribution.

# (5) Now, perform the statistical test and report the results. What is the confidence level and your critical statistic value? Do you reject the null hypothesis or fail to reject it? Come to a conclusion in terms of the experiment task. Did the results match up with your expectations?

# In[38]:


#import pandas and scipy stats
import pandas as pd
import scipy.stats as stats
stroop = pd.read_csv("stroopdata.csv")

#printing stroop
print(stroop)

a=stroop["Congruent"]
b=stroop["Incongruent"]

#conducting t-test between the Incongruent and Congruent datas.
print(stats.ttest_rel(b,a))


# a) Critical Value approach:
# As t alpha value i.e t-critical value from t-distribution table is 1.71 and the calculated t-statistic value is 8.0207, it clearly states that the t-statistic value is is more than the t-critical value and hence the Null Hypothesis is rejected and alternative Hypothesis is selected.
# 
# b) P-Value approach:
# We know that if the P-Value is less than the α i.e 0.05 considering 95% Confidence Interval then we reject the null hypothesis and accept the alternative hypothesis.
# 
# Conclusion:
# Hence by both approach we state that the Null hypothesis is false i.e the time taken to identify colors of Incongruent set is not same as the congruent set and hence the alternative hypotheis of Incongruent set taking more time turns true. It shows that the results did not match our expectation.

# In[ ]:


References:
https://onlinecourses.science.psu.edu/statprogram/node/138
http://python3.codes/
https://www.socialresearchmethods.net/kb/statdesc.php
https://faculty.math.illinois.edu/~r-ash/BPT.html


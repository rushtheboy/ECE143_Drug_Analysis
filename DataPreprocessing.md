## Data preprocessing requirement from model side



#### 1.unique ID, date

> Remove them



#### 2. drugName, condition

> 1. Assign each drugName/condition a unique ID and construct a two-way mapping between drugName/condition and ID.  In the final output file, please store the ID number instead of the string of drugName/condition.
> 2. Previous data analysis shows that there are some data frames with a null condition entry, remove these data frames.
> 3. If it is possible, merge synonyms together. I am not sure how these two features are collected, if it is entered by the users, then it will be useful to merge synonyms.



#### 3. review

> 1. Follow the preprocessing process of [this](https://www.kaggle.com/sumitm004/eda-and-sentiment-analysis/notebook#Preprocessing) one. One slight difference is that, we do not need to create the ‘sentiment_rate’ feature and implement the sentiment(review) function as we are not doing a sentiment analysis task.
> 2. Split the review sentence into a list of words
> 3. Assign each word a unique ID and construct the two-way mapping. In the final output please store the ID of word. So the final output of each review should be a list of integers.
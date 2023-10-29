import pandas as pd
import numpy as np
import nltk
import re
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

def process_data_f():
    mbti_df=pd.read_csv('./train_data.csv')
    mbti_df.head()
    mbti_df.posts[0]
    mbti_df.info()

    pd.DataFrame(mbti_df.type.value_counts()).plot.bar()
    plt.ylabel('Frequency')
    plt.xlabel('Types of Categories')
    plt.title('Bar graph showing frequency of different types of personalities')
    plt.show()

    mbti_df.type.value_counts().plot(kind='pie',figsize=(12,12), autopct='%1.1f%%', explode=[0.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    plt.title('Pie plot showing different types of personalities')
    plt.show()

    sns.distplot(mbti_df["posts"].apply(len))
    plt.xlabel("Length of posts")
    plt.ylabel("Density")
    plt.title("Distribution of lengths of the post")

    mbti_df["posts"] = mbti_df["posts"].str.lower()       #converts text in posts to lowercase as it is preferred in nlp

    for i in range(len(mbti_df)):
        post_temp=mbti_df._get_value(i, 'posts')
        pattern = re.compile(r'https?://[a-zA-Z0-9./-]*/[a-zA-Z0-9?=_.]*[_0-9.a-zA-Z/-]*')    #to match url links present in the post
        post_temp= re.sub(pattern, ' ', post_temp)                                            #to replace that url link with space
        mbti_df._set_value(i, 'posts',post_temp)

    for i in range(len(mbti_df)):
        post_temp=mbti_df._get_value(i, 'posts')
        pattern = re.compile(r'[0-9]')                                    #to match numbers from 0 to 9
        post_temp= re.sub(pattern, ' ', post_temp)                        #to replace them with space
        pattern = re.compile('\W+')                                       #to match alphanumeric characters
        post_temp= re.sub(pattern, ' ', post_temp)                        #to replace them with space
        pattern = re.compile(r'[_+]')
        post_temp= re.sub(pattern, ' ', post_temp)
        mbti_df._set_value(i, 'posts',post_temp)

    for i in range(len(mbti_df)):
        post_temp=mbti_df._get_value(i, 'posts')
        pattern = re.compile('\s+')                                     #to match multiple whitespaces
        post_temp= re.sub(pattern, ' ', post_temp)                      #to replace them with single whitespace
        mbti_df._set_value(i, 'posts', post_temp)

    from nltk.corpus import stopwords
    nltk.download('stopwords')

    remove_words = stopwords.words("english")
    for i in range(mbti_df.shape[0]):
        post_temp=mbti_df._get_value(i, 'posts')
        post_temp=" ".join([w for w in post_temp.split(' ') if w not in remove_words])    #to remove stopwords
        mbti_df._set_value(i, 'posts', post_temp)

    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    nltk.download('wordnet')

    for i in range(mbti_df.shape[0]):
        post_temp=mbti_df._get_value(i, 'posts')
        post_temp=" ".join([lemmatizer.lemmatize(w) for w in post_temp.split(' ')])   #to implement lemmetization i.e. to group together different forms of a word
        mbti_df._set_value(i, 'posts', post_temp)

    print(mbti_df)

    from sklearn.model_selection import train_test_split
    train_data,test_data=train_test_split(mbti_df,test_size=0.2,random_state=42,stratify=mbti_df.type)

    print(test_data)

    vectorizer=TfidfVectorizer( max_features=5000,stop_words='english')
    vectorizer.fit(train_data.posts)
    train_post=vectorizer.transform(train_data.posts).toarray()
    test_post=vectorizer.transform(test_data.posts).toarray()
    print(test_data.posts)

    from sklearn.preprocessing import LabelEncoder
    target_encoder=LabelEncoder()
    train_target=target_encoder.fit_transform(train_data.type)
    test_target=target_encoder.fit_transform(test_data.type)




    from xgboost import XGBClassifier
    model_xgb=XGBClassifier()
    model_xgb.fit(train_post,train_target)
    pred_xgb=model_xgb.predict(test_post)

    pred_training_xgb=model_xgb.predict(train_post)
    print("The train accuracy score for model trained on XGBoost Classifier is:",accuracy_score(train_target,pred_training_xgb))
    print("The test accuracy score for model trained on XGBoost classifier is:",accuracy_score(test_target,pred_xgb))

    from sklearn.metrics import classification_report
    personality_types=target_encoder.inverse_transform([i for i in range(16)])
    print('Test classification report of XGBoost Classifier\n',classification_report(test_target,model_xgb.predict(test_post),target_names=personality_types))





    tests=pd.read_csv('tweets.csv')
    # tests=tests[0]
    tests['text'] = tests['text'].str.lower()       #converts text in posts to lowercase as it is preferred in nlp
    # print(tests)
    tests=np.array(tests)
    t=""
    for tes in tests:
        t+=tes

    tests=pd.read_csv('linkedin.csv')
    tests=tests.columns
    tests=np.array(tests)
    tests=pd.DataFrame(tests)
    tests[0] = tests[0].str.lower()
    tests=np.array(tests)
    for tes in tests:
        t+=tes
    print(t)
    tests=pd.DataFrame(t)
    print(tests)


    for i in range(len(tests)):
        post_temp=tests._get_value(i, 0)
        pattern = re.compile(r'https?://[a-zA-Z0-9./-]*/[a-zA-Z0-9?=_.]*[_0-9.a-zA-Z/-]*')    #to match url links present in the post
        post_temp= re.sub(pattern, ' ', post_temp)                                            #to replace that url link with space
        tests._set_value(i, 0,post_temp)

    for i in range(len(tests)):
        post_temp=tests._get_value(i, 0)
        pattern = re.compile(r'[0-9]')                                    #to match numbers from 0 to 9
        post_temp= re.sub(pattern, ' ', post_temp)                        #to replace them with space
        pattern = re.compile('\W+')                                       #to match alphanumeric characters
        post_temp= re.sub(pattern, ' ', post_temp)                        #to replace them with space
        pattern = re.compile(r'[_+]')
        post_temp= re.sub(pattern, ' ', post_temp)
        tests._set_value(i, 0,post_temp)

    for i in range(len(tests)):
        post_temp=tests._get_value(i, 0)
        pattern = re.compile('\s+')                                     #to match multiple whitespaces
        post_temp= re.sub(pattern, ' ', post_temp)                      #to replace them with single whitespace
        tests._set_value(i, 0, post_temp)

    remove_words = stopwords.words("english")
    for i in range(tests.shape[0]):
        post_temp=tests._get_value(i, 0)
        post_temp=" ".join([w for w in post_temp.split(' ') if w not in remove_words])    #to remove stopwords
        tests._set_value(i, 0, post_temp)

    for i in range(tests.shape[0]):
        post_temp=tests._get_value(i, 0)
        post_temp=" ".join([lemmatizer.lemmatize(w) for w in post_temp.split(' ')])   #to implement lemmetization i.e. to group together different forms of a word
        tests._set_value(i, 0, post_temp)

    test_post=vectorizer.transform(tests[0]).toarray()
    print(test_post)

    pred_xgb=model_xgb.predict(test_post)
    print(pred_xgb)
    pred_xgb=np.sum(pred_xgb)/len(pred_xgb)
    print(pred_xgb)

    personality=["ENFJ","ENFP","ENTJ","ENTP","ESFJ","ESFP","ESTJ","ESTP","INFJ","INFP","INTJ","INTP","ISFJ","ISFP","ISTJ","ISTP" ]      
    print(personality[round(pred_xgb)])






    # Get user input for MBTI type
    user_mbti = personality[round[pred_xgb]]

    # Convert the user input to uppercase for case-insensitive matching
    user_mbti = user_mbti.upper()

    # Initialize a variable to store the suggested job role
    job_role = "Unknown"

    # Use if-else conditions to suggest a job role based on the MBTI type
    if user_mbti == "ISTJ":
        job_role = "Manager"
    elif user_mbti in ["ISFJ", "INFJ"]:
        job_role = "Doctor"
    elif user_mbti == "INTJ":
        job_role = "Engineer"
    elif user_mbti == "ISTP":
        job_role = "Engineer"
    elif user_mbti in ["ISFP", "INFP"]:
        job_role = "Artist"
    elif user_mbti == "INTP":
        job_role = "Scientist"
    elif user_mbti == "ESTP":
        job_role = "Salesperson"
    elif user_mbti == "ESFP":
        job_role = "Entertainer"
    elif user_mbti == "ENFP":
        job_role = "Teacher"
    elif user_mbti == "ENTP":
        job_role = "Entrepreneur"
    elif user_mbti == "ESTJ":
        job_role = "Manager"
    elif user_mbti == "ESFJ":
        job_role = "Lawyer"
    elif user_mbti == "ENFJ":
        job_role = "Teacher"
    elif user_mbti == "ENTJ":
        job_role = "CEO"

    # Display the suggested job role
    return {"status":"For MBTI type {user_mbti}, a suitable job role is: {job_role}"}

    # return user_mbti, job_role
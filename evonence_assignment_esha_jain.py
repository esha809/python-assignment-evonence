#Scenario 1: Data ValidationTask#

def validate_data(data):
    invalid_enties=[]
    for item in data:
        if not isinstance(item.get("age"), int):
            invalid_enties.append(item)
    return invalid_enties
data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": "25"}]
print(validate_data(data))

#Scenario 2: Logging DecoratorTask #

import time

def log_time(func):
    def wrap(n):
        start=time.time()
        result=func(n)
        print("Time", time.time()- start)
        return result
    return wrap

@log_time
def calculate_sum(n):
    return sum(range(1, n+1))

print(calculate_sum(100))

#Scenario 3: Missing Value Handling#

import pandas as pd

df=pd.DataFrame({'income': [20000, None, 22000, None, 25000]})
skewness = df['income'].skew()

if abs(skewness) < 0.5:
    df['income'].fillna(df['income'].median(), inplace=True)
else:
    df['income'].fillna(df['income'].mode()[0], inplace=True)

print(df)

#Scenario 4: Text Pre-processing#

import pandas as pd
import re

df=pd.DataFrame({'text': ["Hello World!", "Python@123"]})
df['cleaned']=df['text'].str.lower().apply(lambda x: re.sub(r'[^a-z0-9\s]', '', x)).str.split()
print(df)


#Scenario 9: Structured Response Generation#
import json
response = '{"benefits": ["Easy to use", "Supports libraries", "Good community"]}'

try:
    data = json.loads(response)
    print("Valid JSON:", data)
except:
    print("Invalid JSON")
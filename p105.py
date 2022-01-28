import csv
import plotly.express as px
import pandas as pd
import math

with open("data.csv") as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

def mean(data):
    sum=0
    n=len(data)
    for i in data:
        sum=sum+int(i)
    mean=sum/n
    return mean

list=[]

for j in data:
    a=int(j)-mean(data)
    sq=a**2
    list.append(sq)

sum2=0

for k in list:
    sum2=sum2+int(k)

result=sum2/(len(data)-1)
standard_deviation=math.sqrt(result)
print(standard_deviation)


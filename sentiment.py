import json
import boto3
import pickle
import pandas
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
import pyspark.sql.functions as f
from pyspark.streaming import StreamingContext
from textblob import TextBlob
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
import pandas
from collections import namedtuple
import time
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext, HiveContext
import findspark
from pyspark import sql
import pymongo
import sys

# System.setProperty("hadoop.home.dir", "PATH/TO/THE/DIR");
findspark.init("C:\spark-3.0.0-preview2-bin-hadoop2.7")

fields = ("tag", "count")
Tweet = namedtuple('Tweet', fields)


thisdict = {
   "Trump_Positive" : 0,
    "Trump_Negative" : 0,
    "Biden_Positive": 0,
    "Biden_Negative":0,
    "Trump_Neutral":0,
    "Biden_Neutral":0,
    "No_One":0,
    "Name": "2020Election"

}

thisdict1 = {}

tb = Blobber(analyzer=NaiveBayesAnalyzer())

s3 = boto3.client('s3')


def tweet_sentiment(tweet):
    a = ""
    time.sleep(2)
    if "Joe biden" in tweet or "biden" in tweet:
        a += "Biden"
    elif "Donald trump" in tweet or "trump" in tweet:
        a += "Trump"
    sentiment = tb(tweet)
    if a != "":
        if sentiment.polarity > .5:
            return a + "_Positive"
        elif sentiment.polarity < .5:
            return a + "_Negative"
        else:
            return a + "_Neutral"
    else:
        return "No_One"


def show(k):
    global look
    pandas_df = k.toPandas()
    for i in range(pandas_df.shape[0]):
        thisdict[pandas_df['WHO'].iloc[i]] += pandas_df['count'].iloc[i]
    look = 1
    #print("updatedlook",look)
    print(thisdict)
    thisdict1.update(thisdict)
    return k


def hello():
    print("trying to write")
    with open('data1.json', 'w') as fp:
        fp.write(str(thisdict).replace("\'", "\""))
        fp.close()
        s3.upload_file('data1.json', 'sentiment1', 'data.json')

sc = SparkContext()
ssc = StreamingContext(sc, 10)
sqlContext = sql.HiveContext(sc)
# sqlContext = sql.SQLContext(sc)
lines = ssc.socketTextStream("localhost", 8090)

(lines.flatMap(lambda line: tweet_sentiment(line.lower()).split(" "))
 .map(lambda word: (word, 1))
 .reduceByKey(lambda x, y: x + y)
 .map(lambda rec: Tweet(rec[0], rec[1]))
 .foreachRDD(lambda rdd: show(rdd.toDF(['WHO', 'count'])))
 )
if __name__ == "__main__":
    ssc.start()
    look= 0
    count = 0
    while True:
        count += 1
        if look == 1:
            print("calling json")
            hello()
            look = 0
        time.sleep(7)


# ssc.awaitTermination()

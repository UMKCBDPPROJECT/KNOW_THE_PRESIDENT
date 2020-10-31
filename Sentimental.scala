package WordClass

import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.streaming.Durations.seconds
import org.apache.spark.streaming.StreamingContext
import org.apache.spark.streaming.twitter.TwitterUtils

object Sentimental {


  def main(args: Array[String]) {

    // val Array(StreamingExamples.consumer_key, StreamingExamples.consumer_secret, StreamingExamples.access_token, StreamingExamples.access_token_secret) = args.take(4)
    val a: Array[String] = new Array[String](4)

    a(0) = StreamingExamples.consumer_key
    a(1) = StreamingExamples.consumer_secret
    a(2) = StreamingExamples.access_token
    a(3) = StreamingExamples.access_token_secret

      if (a.length < 4) {
        print(a.length)
        //   System.err.println("Usage: TwitterPopularTags <consumer key> <consumer secret> " + "<access token> <access token secret> [<filters>]")
        // System.exit(1)
      }

      val filters = args.takeRight(a.length - 4)

      //Passing our Twitter keys and tokens as arguments for authorization


      // Set the system properties so that Twitter4j library used by twitter stream
      // Use them to generate OAuth credentials
      System.setProperty("twitter4j.oauth.consumerKey", StreamingExamples.consumer_key)
      System.setProperty("twitter4j.oauth.consumerSecret", StreamingExamples.consumer_secret)
      System.setProperty("twitter4j.oauth.accessToken", StreamingExamples.access_token)
      System.setProperty("twitter4j.oauth.accessTokenSecret", StreamingExamples.access_token_secret)




    val sparkConf = new SparkConf().setAppName("twitterSentiment").setMaster("local[2]")
      val ssc = new StreamingContext(sparkConf, seconds(5))
      val stream = TwitterUtils.createStream(ssc,None)

      //Input DStream transformation using flatMap
      val tags = stream.flatMap { status => status.getHashtagEntities.map(_.getText) }

      //RDD transformation using sortBy and then map function
      tags.countByValue()
        .foreachRDD { rdd =>
          val now = org.joda.time.DateTime.now()
          rdd
            .sortBy(_._2)
            .map(x => (x, now))
            //Saving our output to local directory
            .saveAsTextFile("C:Users/Chaitanya/Fall2020/BDP/Streaming/$now")
        }

      //DStream transformation using filter and map functions
      val tweets = stream.filter { t =>
        val tags = t.getText.split(" ").filter(_.startsWith("DonaldTrump")).map(_.toLowerCase)
        tags.exists { x => true }
      }

      /*  val data = tweets.map { status =>
        val sentiment = SentimentAnalysisUtils.detectSentiment(status.getText)
        val tagss = status.getHashtagEntities.map(_.getText.toLowerCase)
        (status.getText, sentiment.toString, tagss.toString())
      }
*/
      tweets.print()
      //Saving our output at ~/ with filenames starting like twitters
        print("Saving into files")
      tweets.saveAsTextFiles("\"C:Users/Chaitanya/Fall2020/BDP/Streaming/$now\"", "20000")
      print("Saved to files")
      ssc.start()
      ssc.awaitTermination()
    }
}

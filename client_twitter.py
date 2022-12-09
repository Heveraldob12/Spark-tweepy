from pyspark.sql import SparkSession
from pyspark.sql import functions as f


spark = SparkSession.builder.appName('SparkStreaming').getOrCreate()


lines=spark.readStream\
    .format('socket')\
        .option('host','localhost')\
        .option('port',9009)\
            .load()
            
words = f.explode(f.split(lines.values, ' ')).alias('word')

wordCounts = words.groupBy('word').count()

query = lines.writeStream\
    .outputMode('append')\
    .format('console')\
    .start()

query.awaitTermination()

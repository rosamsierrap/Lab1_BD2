#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /logstat2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /logstat2/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /logstat2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../data/access.log /logstat2/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/logstat2/mapper2.py -mapper ../../mapreduce-test-python/logstat2/mapper2.py \
-file ../../mapreduce-test-python/logstat2/reducer2.py -reducer ../../mapreduce-test-python/logstat2/reducer2.py \
-input /logstat2/input/* -output /logstat2/output/
/usr/local/hadoop/bin/hdfs dfs -cat /logstat2/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /logstat2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /logstat2/output/
../../stop.sh

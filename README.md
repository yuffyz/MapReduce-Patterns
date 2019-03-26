# MapReduce Patterns

This repo contains Hadoop mapreduce programs written in python and java. 

The patterns in this repo includes: 
* Filter
* Top-N
* Summariztion
* Numerical Summariztion: mean
* Combiner
* Structural Patterns


## Applications

Log file
Sales record
Text file


## Data 

[Log file](http://content.udacity-data.com/courses/ud617/access_log.gz)
[Purchase file](http://content.udacity-data.com/courses/ud617/purchases.txt.gz)

## Setup 

```bash

# https://github.com/ShanLu1984/Hadoop-and-MapReduce

# 1. Upload file from local machine to a 3-node cluster on GCP
scp -i ~/.ssh/my-ssh-key [LOCAL_FILE_PATH] [USERNAME]@[IP_ADDRESS]:~

# 2. copy file from GCP to HDFS
hadoop fs -put access_log myinput

```

To test locally, the data was sampled and then tested with: 

```bash

# 1. make a sample testfile 
head -100 ../data/access_log > testfile

# 2. a pipeline for testing
cat testfile | ./mapper.py | sort | ./reducer.py


```



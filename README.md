# MapReduce Patterns

Mapreduce programs have general patterns for batch processing. The patterns could be applied to abstract statistics from large dataset. Common patterns are summarized here for reuse, which includes: 
* Filter
* Top-N
* Summariztion
* Numerical Summariztion: mean
* Combiner
* Structural Patterns


## Application & Dataset

* Log file: [Data](http://content.udacity-data.com/courses/ud617/access_log.gz)
* Sales record: [Data](http://content.udacity-data.com/courses/ud617/purchases.txt.gz)
* Text file


## Setup 

1. Upload the dataset to Hadoop on Google Cloud 

```bash

# 1) Upload file from local machine to a 3-node cluster on GCP
scp -i ~/.ssh/my-ssh-key [LOCAL_FILE_PATH] [USERNAME]@[IP_ADDRESS]:~

# 1) copy file from GCP to HDFS
hadoop fs -put access_log myinput

```

2. To test locally, the data was sampled and then tested with: 

```bash

# 1) make a sample testfile 
head -100 ../data/access_log > testfile

# 2) a pipeline for testing
cat testfile | ./mapper.py | sort | ./reducer.py


```

## Reference

* Udacity Intro to Hadoop and MapReduce: [MOOC](https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617)
* CISC5950 Big Data Programming: [Website](https://yingmao.github.io/cisc5950s19/)
* CS246 Mining Massive Data Sets: [Website](http://web.stanford.edu/class/cs246/), [Video](https://www.youtube.com/channel/UC_Oao2FYkLAUlUVkBfze4jg/videos), [MOOC](https://lagunita.stanford.edu/courses/course-v1:ComputerScience+MMDS+SelfPaced/about), [Book](http://infolab.stanford.edu/~ullman/mmds/bookL.pdf)
* Data-Intensive Text Processing with MapReduce: [Book](https://lintool.github.io/MapReduceAlgorithms/)



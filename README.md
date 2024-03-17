# Vehicle_collision

## Overview

This project aims at creating a data pipeline, extracting data from Raw csv file of vehicle collision data and transforming using **python script** and loading data to **AWS S3** to see data in much structered form. Which is can be used to gain insight on the different reasons of vehicle collision.

## Data Architecture

![aws 2](https://github.com/MohammmadAnas/Vehicle_collision/assets/127856326/168094fe-3906-4ae5-bc72-12c0f4bca0f5)


## Tools 

- ### Python
            
   
- ### Dataset- [New York Motor Vehicle Collisions](https://www.kaggle.com/datasets/ishmaelkiptoo/motor-vehicle-collisions)

- ### Amazon Web Services

     1. Amazon S3 (Simple Storage Services): **Storage**
        - Amazon S3 provides scalable object storage, like a virtual hard drive in cloud.
                   
     2. Crawler: **Discovery**
        - Automatically discovers and organizes metadata about you data for use in AWS Glue.
          
     3. AWS Glue Data Catalog: **Metadata**
        - A centralized metadata repository that stores information about data sources, tranformations and targets.
          
     4. Athena: **Query**
        - Enables you to analyze data stored in S3 using standard SQL queries.

## Execution Process

 + ### Download data from Kaggle and clean the data using Python script.
    
    - Download the data either using the **Kaggele API** or you can manually download the data extract it and put it in the same folder as the python script.
    - Run the python script to get the transformed data a file named **cleaned_data.csv** will be produced in the directory of the python script.
      
+ ### Store files in Amazon S3
  
    - The **cleaned_data.csv** created will now be stored in S3, the data after transformation is now made to store in form of CSV files inside our S3 bucket folder- **vehicle-collision-data-raw-useast1-dev**.
          
+ ### Generate AWS Glue crawlers to crawl CSV files and create tables
  
    - AWS Glue Crawlers are helpful in crawling the data from the source and then storing the data inside the databases.
    - Here a crawler for extracting data from S3 was created in order to create table.
      
+ ### Build analytical tables using Amazon Athena
  
    - The databases are ready to be analyzed.
    - You can see the CRASH DATE, CRASH YEAR, CRASH MONTH and other coulmns of the data.
  
## Some of the visualization of the data is shown below :

![1](https://github.com/MohammmadAnas/Vehicle_collision/assets/127856326/f9eedea8-5d17-4945-a593-503824e8b2f5)

![2](https://github.com/MohammmadAnas/Vehicle_collision/assets/127856326/b82cd723-c91c-4ae9-9b95-2fa7bf35d190)

![3](https://github.com/MohammmadAnas/Vehicle_collision/assets/127856326/b2cd49f7-fdd8-4623-8977-86a76d1ace6a)


      

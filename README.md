# Vehicle_collision

## Overview

This project aims at creating a data pipeline, extracting data from Raw csv file of vehicle collision data and transforming using **python script** and loading data to **AWS S3** to see data in much structered form.

## Data Architecture

![aws 1](https://github.com/MohammmadAnas/Vehicle_collision/assets/127856326/25b6f8f0-3b8b-446d-9054-ba39f3dfc2b9)

## Tools 

- ### Python
            
   
- ### Dataset- [New York Motor Vehicle Collisions](https://www.kaggle.com/datasets/ishmaelkiptoo/motor-vehicle-collisions)

- ### Amazon Web Services

     1. Amazon S3 (Simple Storage Services): **Storage**
        - Amazon S3 provides scalable object storage, like a virtual hard drive in cloud.
          
     2. Amazon Cloudwatch: **Monitoring**
        - This AWS service is for collecting and tracking metrics, monitoring log files, and setting alarms.
          
     3. Crawler: **Discovery**
        - Automatically discovers and organizes metadata about you data for use in AWS Glue.
          
     4. AWS Glue Data Catalog: **Metadata**
        - A centralized metadata repository that stores information about data sources, tranformations and targets.
          
     5. Athena: **Query**
        - Enables you to analyze data stored in S3 using standard SQL queries.

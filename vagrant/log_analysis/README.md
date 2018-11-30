Logs Analysis

The project goal is to take a database containing access logs of a news web page and answer these questions about them:

1 - What are the most popular three articles of all time?
2 - Who are the most popular article authors of all time?
3 - On which days did more than 1% of requests lead to errors?

Prerequisites

This project was developed using python programming language and PostgreSQL database. These are the recommended versions:

PostgreSQL 9.5.14
Python 3.5.2 / Bleach 3.0.2 / Psycopg2 2.7.6.1
Python 2.7.12 / Bleach 3.0.2 / Psycopg2 2.7.6.1

Database setup

Steps required to setup database. 

1- Download database from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
2- Extract file newsdata.sql
3- Import database
    vagrant@vagrant:/vagrant/log_analysis$ psql -d news -f newsdata.sql

Views creation

View created to add a column called article_name to log information in order to simplify the join to the table articles

news=> create view log_article as select *,substring(path,10) as Article_Name from log;


View created to consolidate information about logs, articles and authors into a single place

news=> create view complete_log as select path,ip,method,status,la.time,la.id,article_name,title,a.name from log_article la left join articles on la.article_name = articles.slug left join authors as a on a.id = articles.author;


Views created to make the calculation of status error codes percentage easier

Total views per day
news=> create view total_views_by_day as select count(*) as views, time::date as day from complete_log group by day;

Daily access by status
news=> create view views_by_status as select count(*) as views, time::date as day, status from complete_log group by day,status order by day desc;


How to run the software

From the folder logs_analysis, run reports.py

vagrant@vagrant:/vagrant/log_analysis$ ./reports.py
# AnalyseLogs
https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004


The script can simply be run with
```
$ python analyse_log.py
```
you need to have setted up the vagrant server and the news database like described at the according Udacity course page.

It contains the following functions:

# connect()
- connects to the database 'news'
- returns database object

# run_query(query)
- opens a connection to the database
- fetches the 'query' which simply is a string like "SELECT .. FROM..."
- closes the connection
- returns the result of the query as database object

# popular_articles()
- defines the query to fetch the answer for question 1 of the Udacity task, which is:
> What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
- Example:
```
"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views
```

# popular_authors()
- defines the query to fetch the answer for question 2 of the Udacity task, which is:
> Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
- Example:
```
Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views
```

# error_prone_days()
- defines the query to answer question 3, which is:
> On which days did more than 1% of requests lead to errors?
- Example:
```
July 29, 2016 — 2.5% errors
```

# make_report()
- runs the three functions that return the answers to Question 1-3
- creates a log-file "log_report.log"
- appends the answers nicely formatted to the log-file

# if \_\_name_\_ == \'\_\_main\_\_\'
- ensures that one can just run the script via command line

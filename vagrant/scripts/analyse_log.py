#!/usr/bin python
# -*- coding: utf-8 -*-

import psycopg2
import datetime
import os
import sys


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except Exception as e:
        print(e)
        sys.exit(0)


def run_query(query):
    """ returned cursor object is iterable: for res in result: print res """
    db, cur = connect()
    cur.execute(query)
    result = cur.fetchall()
    db.close()

    return result


def popular_articles():
    query = ("SELECT articles.title, count(log.path) AS views "
             "FROM articles, log "
             "WHERE log.path LIKE '%'||articles.slug "
             "GROUP BY articles.title "
             "ORDER BY views DESC "
             "LIMIT 3")

    return run_query(query)


def popular_authors():
    query = ("SELECT authors.name, count(log.path) AS views "
             "FROM log, authors JOIN articles ON articles.author = authors.id "
             "WHERE log.path LIKE '%'||articles.slug "
             "GROUP BY authors.name "
             "ORDER BY views DESC "
             "LIMIT 3")

    return run_query(query)


def error_prone_days():
    query = ("SELECT * FROM ( "
             "SELECT time::date,  "
             "ROUND(100.0 * "
             "SUM(CASE WHEN status != '200 OK' THEN 1 ELSE 0 END)::numeric "
             "/ COUNT(*)::numeric, 1) as error_rate "
             "FROM log "
             "GROUP BY time::date "
             "ORDER BY error_rate DESC "
             ") as _ WHERE error_rate > 1")

    return run_query(query)


def make_report():
    """ create a log file containing info for the current time """
    articles = popular_articles()
    authors = popular_authors()
    errors = error_prone_days()

    # open the report file, or create if not exists yet
    filename = "log_report.log"
    if os.path.exists(filename):
        append_or_write = 'a'  # append if file exists already
    else:
        append_or_write = 'w'  # create a new file to write to
    report = open(filename, append_or_write)

    ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    report.write(ts + '\n \n')

    report.write("The most popular three articles of all time are: \n")
    for article in articles:
        report.write('"' + str(article[0]) + '" - ' + str(article[1]) +
                     ' views \n')

    report.write('\n')

    report.write("The most popular article authors of all time are: \n")
    for author in authors:
        report.write(str(author[0]) + ' - ' + str(author[1]) + ' views \n')

    report.write('\n')

    report.write("These days showed more than 1% of request errors: \n")
    for error in errors:
        report.write(str(error[0].strftime('%B %d, %Y')) + ' - ' +
                     str(error[1]) + '% errors \n')

    report.write('\n \n======\n \n')

    report.close()


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    make_report()

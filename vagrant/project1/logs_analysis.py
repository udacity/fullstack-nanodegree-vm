#!/usr/lib/python2.7
import psycopg2
import sys


def query_db(query):
    try:
        db = psycopg2.connect("dbname=news")
    except psycopg2.Error as e:
        print "Unable to connect!"
        print e.pgerror
        print e.diag.message_detail
        sys.exit(1)
    else:
        c = db.cursor()
        c.execute(query)
        results = c.fetchall()
        db.close()
    return results


def answer_question_1():
    query = """ SELECT at.title, count(l.id) as num
                FROM log as l, articles as at
                WHERE l.path = '/article/'||at.slug
                AND l.status = '200 OK'
                GROUP BY at.id
                ORDER BY num desc
                LIMIT 3;"""

    results = query_db(query)
    for i in results:
        print '{article} - {count} views'.format(article=i[0], count=i[1])


def answer_question_2():
    query = """ SELECT at.name, count(l.id) as num
                FROM log as l, articles as ar, authors as at
                WHERE l.path = '/article/'||ar.slug
                AND ar.author = at.id
                AND l.status = '200 OK'
                GROUP BY at.id
                ORDER BY num DESC
                LIMIT 3;"""

    results = query_db(query)
    for i in results:
        print '{author} - {count} views'.format(author=i[0], count=i[1])


def answer_question_3():
    query = """ SELECT to_char(ds.date_day,'Mon DD, YYYY'),
                to_char(ds.num_failure::float/ds.total::float * 100,'99D99%')
                FROM day_summary AS ds
                WHERE ds.num_failure::float/ds.total::float > 0.01;"""

    results = query_db(query)
    for i in results:
        print '{date} - {percent} errors'.format(date=i[0], percent=i[1])


print("--- Results Q1 ---")
answer_question_1()
print("\n--- Results Q2 ---")
answer_question_2()
print("\n--- Results Q3 ---")
answer_question_3()

import psycopg2
import sys
from datetime import datetime


def make_query(query):
    conn = psycopg2.connect("dbname=news user=vagrant")
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchall()
    cur.close()
    conn.close()

if sys.argv[1] == 'top-3-articles':
    results = make_query(
        """
        SELECT a.title,
            count(*) AS views
        FROM log l,
            articles a
        WHERE l.path = concat('/article/', a.slug)
        GROUP BY l.path,
                a.title
        ORDER BY views DESC
        LIMIT 3;
        """
    )
    for result in results:
        print "\"%s\" - %s views" % result

if sys.argv[1] == 'top-authors':
    results = make_query(
        """
        SELECT auth.name,
            count(*) AS views
        FROM authors auth
        JOIN articles art ON auth.id = art.author
        JOIN log l ON l.path = concat('/article/', art.slug)
        GROUP BY auth.id
        ORDER BY views DESC
        """
    )
    for result in results:
        print "%s - %s views" % result

if sys.argv[1] == 'failure-days':
    results = make_query(
        """
        SELECT requests.day,
            cast(failure.failure_count * 1.0/requests.request_count AS decimal)
                AS failure_ratio
        FROM
        ( SELECT count(*) AS failure_count,
                date_trunc('day', TIME) AS DAY
        FROM log
        WHERE status != '200 OK'
        GROUP BY DAY ) AS failure
        JOIN
        ( SELECT count(*) AS request_count,
                date_trunc('day', TIME) AS DAY
        FROM log
        GROUP BY DAY ) AS requests ON failure.day = requests.day
        WHERE cast(
            failure.failure_count * 1.0/requests.request_count AS decimal
            ) > 0.01
        """
    )
    for result in results:
        print "%s - %s%% errors" % (
            result[0].strftime('%b %d, %Y'),
            round(result[1] * 100, 2)
        )

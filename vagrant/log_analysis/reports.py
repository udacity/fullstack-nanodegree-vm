# -*- coding: utf-8 -*-

import psycopg2
import bleach

DBNAME = "news"


def get_errors(percentage):
    conn = None
    try:
        conn = psycopg2.connect(database=DBNAME)
        cur = conn.cursor()
        print('Em quais dias mais de 1% das requisicoes'
              ' resultaram em erros')

        cur.execute("select vd.views as total, vs.views, vs.day from "
                    "views_by_status as vs, total_views_by_day as vd "
                    "where vs.day = vd.day and vs.status != '200 OK' "
                    "and (vs.views*100/vd.views) > %s",
                    (bleach.clean(str(percentage)), ))

        # display the PostgreSQL database server version
        errors = cur.fetchall()

        for property in errors:
            requests = float(property[0])
            num_of_errors = float(property[1])
            errors_percentage = num_of_errors * 100 / requests

            print ('{0:%B} {0:%d}, {0:%Y} - {1}% errors'
                   .format(property[2], round(errors_percentage, 2)))
        print("\n")

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def most_popular_articles(quantity):
    conn = None
    try:
        conn = psycopg2.connect(database=DBNAME)
        cur = conn.cursor()
        print('\nQuais são os três artigos mais populares de todos os tempos?')
        cur.execute("select title,count(*) as views from complete_log "
                    "where title != '' group by title order by views "
                    "desc limit %s", (bleach.clean(str(quantity)), ))

        # display the PostgreSQL database server version
        errors = cur.fetchall()

        for property in errors:
            name = property[0]
            views = property[1]

            print ('"{0}" - {1:} views'.format(name, views))
        print("\n")

    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def most_popular_authors():
    conn = None
    try:
        conn = psycopg2.connect(database=DBNAME)
        cur = conn.cursor()
        print('Quem são os autores de artigos mais populares '
              'de todos os tempos?')
        cur.execute("select name, count(*) as views from complete_log "
                    "where name != '' group by name order by views desc")

        # display the PostgreSQL database server version
        errors = cur.fetchall()

        for property in errors:
            name = property[0]
            views = property[1]
            print ('{0} - {1:}'.format(name, views))
        print("\n")
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    most_popular_articles(3)
    most_popular_authors()
    get_errors(1)

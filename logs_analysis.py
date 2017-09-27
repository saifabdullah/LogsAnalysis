#!/usr/bin/env python
# Python version 2.7.12

import psycopg2   # import Postgresql library

DBNAME = 'news'   # Store global database name


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except BaseException:
        print("Unable to connect to the database")


def top_three_articles():
    """Return the top three articles by most views"""

    db, cursor = connect()
    query = "select articles.title,cast(count(log.path)as integer)"\
        "as views from articles,log where log.path="\
        "CONCAT('/article/',articles.slug) group by "\
        "articles.title order by views DESC limit 3;"
    cursor.execute(query)
    rows = cursor.fetchall()
    row_count = 0
    print('**** Top Three Articles by Page View **** ')
    print(" ")
    for (title, views) in rows:
        print("    {} - {} views".format(title, views))
    print(" ")
    print("-" * 70)
    print(" ")

    db.close()
    return rows
    top_three = cursor.execute(query)


def popular_authors():
    """Return the most popular authors based on overall page views"""

    db, cursor = connect()
    query = "select authors.name,cast(sum(views)as integer) as "\
            "total_views from authors, viewcount " \
            " where authors.id=viewcount.author group by authors.name "\
            "order by total_views DESC;"
    cursor.execute(query)
    rows = cursor.fetchall()
    print('**** Most Popular Authors Based on Total Article Views ****')
    print(" ")
    for (name, total_views) in rows:
        print("    {} - {} views".format(name, total_views))
    print(" ")
    print("-" * 70)
    print(" ")
    db.close()
    return rows

    author_popularity = cursor.execute(query)


def high_error_days():
    """Return the days where errors exceeded 1%"""
    db, cursor = connect()
    query = "select to_char(a.date, 'Mon DD, YYYY'), (a.errors * 100"\
            " / b.requests) from (select time::date as date, count(*) "\
            "as errors from log where status !=  '200 OK' group by date)"\
            " as a, (select time::date as date, count(*) as requests "\
            "from log group by date) as b where a.date = b.date "\
            "and (a.errors * 100 / b.requests) >=1;"
    cursor.execute(query)
    rows = cursor.fetchall()
    print('**** Days When errors are more than 1% ****')
    print(" ")
    for (date, errors) in rows:
        print("    {} - {} % errors ".format(date, errors))
    print(" ")
    print("-" * 70)
    print(" ")
    db.close()
    return rows

    high_error_results = cursor.execute(query)


if __name__ == '__main__':
    print(" ")
    print("--- Generating Results ---")
    print(" ")
    top_three_articles()
    popular_authors()
    high_error_days()

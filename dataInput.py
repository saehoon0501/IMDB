#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 10:27:00 2021

@author: saehoonbyun
"""


import mysql.connector
import time


def load_title_akas():
    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                   db='university', auth_plugin='mysql_native_password')
    cur = conn.cursor(mysql.connector.cursor.MySQLCursor())
    filename = 'title.akas.tsv'

    f = open(filename, "r")

    insert_sql = """insert into title_akas (title_id, ordering, title, region, language, types, attributes, isOriginalTitle)
                    values (%s, %s, %s, %s, %s, %s, %s, %s)"""

    oneline = f.readline()

    oneline = f.readline()[:-1]

    rows = []
    i = 0

    while oneline:
        attrs = tuple(oneline.split('\t'))
        rows.append(attrs)
        i += 1
        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows" % i)

        oneline = f.readline()[:-1]

    if rows:
        cur.executemany(insert_sql, rows)
        conn.commit()
        print("%d rows" % i)

    f.close()
    cur.close()
    conn.close()


def load_title_basics():
    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                   db='university', auth_plugin='mysql_native_password')
    cur = conn.cursor(mysql.connector.cursor.MySQLCursor())
    filename = 'title.basics.tsv'

    f = open(filename, "r")

    insert_sql = """insert into title_basics (tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres)
                    values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    oneline = f.readline()
    oneline = f.readline()[:-1]

    rows = []
    i = 0

    while oneline:
        attrs = (oneline.split('\t'))
        attrs[5] = attrs[5].replace('\\N', '0')
        attrs[6] = attrs[6].replace('\\N', '0')
        attrs[7] = attrs[7].replace('\\N', '0')
        attrs[8] = attrs[8].replace('\\N', 'Null')
        if attrs[8].__len__() > 1:
            temp = attrs[8].split(',')
            for x in temp:
                a = (attrs[0], attrs[1], attrs[2], attrs[3],
                     attrs[4], attrs[5], attrs[6], attrs[7], x)
                rows.append(a)
                i += 1
        else:
            a = (attrs[0], attrs[1], attrs[2], attrs[3],
                 attrs[4], attrs[5], attrs[6], attrs[7], attrs[8])
            rows.append(a)
            i += 1

        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows" % i)

        oneline = f.readline()[:-1]

    if rows:
        cur.executemany(insert_sql, rows)
        conn.commit()
        print("%d rows" % i)

    f.close()
    cur.close()
    conn.close()


def load_title_crew():
    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                   db='university', auth_plugin='mysql_native_password')
    cur = conn.cursor(mysql.connector.cursor.MySQLCursor())
    filename = 'title.crew.tsv'

    f = open(filename, "r")

    insert_sql = """insert into title_crew(tconst, directors, writers)
                    values (%s, %s, %s)"""

    oneline = f.readline()

    oneline = f.readline()[:-1]

    rows = []
    i = 0

    while oneline:
        attrs = (oneline.split('\t'))
        attrs[1] = attrs[1].replace('\\N', 'Null')
        attrs[2] = attrs[2].replace('\\N', 'Null')
        if attrs[1].__len__() > 1:
            temp = attrs[1].split(',')
        if attrs[2].__len__() > 1:
            temp2 = attrs[2].split(',')
        for x in temp:
            for y in temp2:
                a = (attrs[0], x, y)
                rows.append(a)
                i += 1

        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows" % i)

        oneline = f.readline()[:-1]

    if rows:
        cur.executemany(insert_sql, rows)
        conn.commit()
        print("%d rows" % i)

    f.close()
    cur.close()
    conn.close()


def load_title_episode():
    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                   db='university', auth_plugin='mysql_native_password')
    cur = conn.cursor(mysql.connector.cursor.MySQLCursor())
    filename = 'title.episode.tsv'

    f = open(filename, "r")

    insert_sql = """insert into title_episode (tconst, parentTconst, seasonNumber, episodeNumber)
                    values (%s, %s, %s, %s)"""

    oneline = f.readline()

    oneline = f.readline()[:-1]

    rows = []
    i = 0

    while oneline:
        attrs = (oneline.split('\t'))
        attrs[2] = attrs[2].replace('\\N', '0')
        attrs[3] = attrs[3].replace('\\N', '0')
        rows.append(attrs)
        i += 1

        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows" % i)

        oneline = f.readline()[:-1]

    if rows:
        cur.executemany(insert_sql, rows)
        conn.commit()
        print("%d rows" % i)

    f.close()
    cur.close()
    conn.close()


def load_title_principals():
    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                   db='university', auth_plugin='mysql_native_password')
    cur = conn.cursor(mysql.connector.cursor.MySQLCursor())
    filename = 'title.principals.tsv'

    f = open(filename, "r")

    insert_sql = """insert into title_principals (tconst, ordering, nconst, category, job, characters)
                    values (%s, %s, %s, %s, %s, %s)"""

    oneline = f.readline()

    oneline = f.readline()[:-1]

    rows = []
    i = 0

    while oneline:
        attrs = tuple(oneline.split('\t'))
        rows.append(attrs)
        i += 1
        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows" % i)

        oneline = f.readline()[:-1]

    if rows:
        cur.executemany(insert_sql, rows)
        conn.commit()
        print("%d rows" % i)

    f.close()
    cur.close()
    conn.close()


def load_title_ratings():
    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                   db='university', auth_plugin='mysql_native_password')
    cur = conn.cursor(mysql.connector.cursor.MySQLCursor())
    filename = 'title.ratings.tsv'

    f = open(filename, "r")

    insert_sql = """insert into title_ratings (tconst, averageRating, numVotes)
                    values (%s, %s, %s)"""

    oneline = f.readline()

    oneline = f.readline()[:-1]

    rows = []
    i = 0

    while oneline:
        attrs = tuple(oneline.split('\t'))
        rows.append(attrs)
        i += 1
        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows" % i)

        oneline = f.readline()[:-1]

    if rows:
        cur.executemany(insert_sql, rows)
        conn.commit()
        print("%d rows" % i)

    f.close()
    cur.close()
    conn.close()


def load_name_basics():
    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                   db='university', auth_plugin='mysql_native_password')
    cur = conn.cursor(mysql.connector.cursor.MySQLCursor())
    filename = 'name.basics.tsv'

    f = open(filename, "r")

    insert_sql = """insert into name_basics (nconst, primaryName, birthYear, deathYear, primaryProfession, knownForTitles)
                    values (%s, %s, %s, %s, %s, %s)"""

    oneline = f.readline()

    oneline = f.readline()[:-1]

    rows = []
    i = 0

    while oneline:
        attrs = (oneline.split('\t'))
        attrs[2] = attrs[2].replace('\\N', '0')
        attrs[3] = attrs[3].replace('\\N', '0')
        if attrs[4].__len__() > 1:
            temp = attrs[4].split(',')
            if attrs[5].__len__() > 1:
                temp2 = attrs[5].split(',')
            for x in temp:
                for y in temp2:
                    a = (attrs[0], attrs[1], attrs[2], attrs[3], x, y)
                    rows.append(a)
                    i += 1
            else:
                for x in temp:
                    a = (attrs[0], attrs[1], attrs[2], attrs[3], x, attrs[5])
                    rows.append(a)
                    i += 1
        else:
            if attrs[5].__len__() > 1:
                temp2 = attrs[5].split(',')
                for y in temp2:
                    a = (attrs[0], attrs[1], attrs[2], attrs[3], attrs[4], y)
                    rows.append(a)
                    i += 1
            else:
                a = (attrs[0], attrs[1], attrs[2],
                     attrs[3], attrs[4], attrs[5])
                rows.append(a)
                i += 1

        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows" % i)

        oneline = f.readline()[:-1]

    if rows:
        cur.executemany(insert_sql, rows)
        conn.commit()
        print("%d rows" % i)

    f.close()
    cur.close()
    conn.close()


def load_Movie():
    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                   db='university', auth_plugin='mysql_native_password')
    cur = conn.cursor(mysql.connector.cursor.MySQLCursor())
    filename = 'title.basics.tsv'

    f = open(filename, "r")

    insert_sql = """insert into title_basics (tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes)
                    values (%s, %s, %s, %s, %s, %s, %s, %s)"""

    oneline = f.readline()
    oneline = f.readline()[:-1]

    rows = []
    i = 0

    while oneline:
        attrs = (oneline.split('\t'))
        attrs[5] = attrs[5].replace('\\N', '0')
        attrs[6] = attrs[6].replace('\\N', '0')
        attrs[7] = attrs[7].replace('\\N', '0')
        attrs[8] = attrs[8].replace('\\N', 'Null')

        a = (attrs[0], attrs[1], attrs[2], attrs[3],
             attrs[4], attrs[5], attrs[6], attrs[7])
        rows.append(a)
        i += 1

        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows" % i)

        oneline = f.readline()[:-1]

    if rows:
        cur.executemany(insert_sql, rows)
        conn.commit()
        print("%d rows" % i)

    f.close()
    cur.close()
    conn.close()


def load_Genre():
    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                   db='university', auth_plugin='mysql_native_password')
    cur = conn.cursor(mysql.connector.cursor.MySQLCursor())
    filename = 'title.basics.tsv'

    f = open(filename, "r")

    insert_sql = """insert into Genre (mykey, title_id, genres)
                    values (%s, %s, %s)"""

    oneline = f.readline()
    oneline = f.readline()[:-1]

    rows = []
    i = 0

    while oneline:
        attrs = (oneline.split('\t'))
        attrs[5] = attrs[5].replace('\\N', '0')
        attrs[6] = attrs[6].replace('\\N', '0')
        attrs[7] = attrs[7].replace('\\N', '0')
        attrs[8] = attrs[8].replace('\\N', 'Null')
        if attrs[8].__len__() > 1:
            temp = attrs[8].split(',')
            for x in temp:
                a = (i, attrs[0], x)
                rows.append(a)
                i += 1

        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows" % i)

        oneline = f.readline()[:-1]

    if rows:
        cur.executemany(insert_sql, rows)
        conn.commit()
        print("%d rows" % i)

    f.close()
    cur.close()
    conn.close()


def load_Person():
    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                   db='university', auth_plugin='mysql_native_password')
    cur = conn.cursor(mysql.connector.cursor.MySQLCursor())
    filename = 'name.basics.tsv'

    f = open(filename, "r")

    insert_sql = """insert into Person (name_id, primaryName, birthYear, deathYear)
                    values (%s, %s, %s, %s)"""

    oneline = f.readline()

    oneline = f.readline()[:-1]

    rows = []
    i = 0

    while oneline:
        attrs = (oneline.split('\t'))
        attrs[2] = attrs[2].replace('\\N', '0')
        attrs[3] = attrs[3].replace('\\N', '0')

        a = (attrs[0], attrs[1], attrs[2], attrs[3])
        rows.append(a)
        i += 1

        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows" % i)

        oneline = f.readline()[:-1]

    if rows:
        cur.executemany(insert_sql, rows)
        conn.commit()
        print("%d rows" % i)

    f.close()
    cur.close()
    conn.close()


def load_Review():
    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                   db='university', auth_plugin='mysql_native_password')
    cur = conn.cursor(mysql.connector.cursor.MySQLCursor())
    filename = 'title.ratings.tsv'

    f = open(filename, "r")

    insert_sql = """insert into Review (tconst, averageRating, numVotes)
                    values (%s, %s, %s)"""

    oneline = f.readline()

    oneline = f.readline()[:-1]

    rows = []
    i = 0

    while oneline:
        attrs = tuple(oneline.split('\t'))
        rows.append(attrs)
        i += 1
        if i % 10000 == 0:
            cur.executemany(insert_sql, rows)
            conn.commit()
            rows = []
            print("%d rows" % i)

        oneline = f.readline()[:-1]

    if rows:
        cur.executemany(insert_sql, rows)
        conn.commit()
        print("%d rows" % i)

    f.close()
    cur.close()
    conn.close()



search_input = input("사용할 Query를 입력하세요 :")
start_time = time.time()
#사용할 함수 입력해 시간 재보기.
elapsed_time = time.time() - start_time
print(elapsed_time, 'seconds')

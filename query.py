#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 10:27:00 2021

@author: saehoonbyun
"""

import mysql.connector
import time

def query(a):
    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                   db='university', auth_plugin='mysql_native_password')
    cur = conn.cursor(mysql.connector.cursor.MySQLCursor())

    row = []

    insert_sql = """%s""" % a
    cur.execute(insert_sql)
    row = cur.fetchall()
    print(row)

    cur.close()
    conn.close()
    
    
search_input = input("사용할 Query를 입력하세요 :")
start_time = time.time()
query(search_input)
elapsed_time = time.time() - start_time
print(elapsed_time, 'seconds')   
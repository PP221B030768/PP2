# CREATE OR REPLACE PROCEDURE public.insert_list(
# 	IN p_name character varying,
# 	IN p_phone_number character varying)
# LANGUAGE 'plpgsql'
# AS $BODY$
# begin
# 	insert into phonebook(name, phone_number) values(p_name, p_phone_number);
# end;
# $BODY$;

data = [('Aliya', '87023981276'), ('Dan', '87789127359'), ('Val', '87778126349')]

import psycopg2
from config import config

def check(object):
    list = []
    cnt = -1
    for i in object:
        cnt += 1
        if not i[1].isdigit():
            del object[cnt]
    return object

def insert_list(object):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany('call insert_list(%s, %s)', object)
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
            
insert_list(data)
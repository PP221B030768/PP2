# CREATE OR REPLACE FUNCTION public.pattern(
# 	)
#     RETURNS TABLE(user_id integer, user_name character varying) 
#     LANGUAGE 'plpgsql'

# AS $$
# begin
#     return query
#     select snake_score.user_id, snake_score.user_name from snake_score where snake_score.user_name like '%na%';
# end;
# $$;

# ALTER FUNCTION public.pattern()
#     OWNER TO postgres;

import psycopg2
from config import config

def pattern():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.callproc('pattern', ())
        row = cur.fetchone()
        while row is not None:
            print(*row)
            row = cur.fetchone()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

pattern()
import psycopg
from config import config

def get_icon(icon):

    conn = None
    icon_get = "SELECT reference_table FROM icon_reference_table WHERE reference_id = %s"
    
    try:
        params = config()
        conn = psycopg.connect(**params)
        cur = conn.cursor()
        cur.execute(icon_get, (icon))
        tbr = cur.fetchone()[0]
        cur.close
        return tbr
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    print(get_icon([1]))

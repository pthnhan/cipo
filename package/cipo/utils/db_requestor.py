import pandas as pd
import psycopg2

def get_query_from_file(sql_file, id_coin):
    with open(sql_file, 'r') as rf:
        query = rf.read()
    query = query.replace('$id_coin', str(id_coin))
    return query

class DBRequestor():
    def __init__(self):
        self.info_db = None

    def get_info_db(self, **kwargs):
        self.info_db = kwargs

    def get_df_by_query(self, query):
        conn = psycopg2.connect(**self.info_db)
        if conn is None:
            return None
        with conn.cursor() as cur:
            cur.execute(query)
            columns = [desc[0] for desc in cur.description]
            data = cur.fetchall()
            cur.close()
        conn.close()
        if not len(data):
            return pd.DataFrame(data)
        return pd.DataFrame(data, columns=columns)


if __name__ == "__main__":
    a = DBRequestor()
    database = 'ipv_db'
    username = 'uspto'
    password = 'uspto'
    host = "192.168.250.24"
    port = "8888"
    a.get_info_db(database = database, user = username, password = password, host = host, port = port)
    df = a.get_df_by_query("select * from ca_tm_index_heading limit 100")
    print(df)
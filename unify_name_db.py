import pandas as pd
from impala.dbapi import connect
import os
# settings.py
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
print(find_dotenv())


def query_table(impala_cur, table_name, no_of_rows=1000):
    query_data = f"""
        with ca_tm_drop_duplicate as
    (   
        select *
        from
        (
            select *,
            ROW_NUMBER() over (partition by st13applicationnumber order by st13applicationnumber asc) as index_st13,
            ROW_NUMBER() over (partition by legalentityname order by st13applicationnumber asc) as index_legalname
            from ipv_db.{table_name}
            where nationallegalentitycode = 'CA'
        ) a
        where index_st13 = 1 and index_legalname = 1
    ), 
    ca_tm_fix_legalname as
    (
        select *, replace(
                    replace(
                    replace(
                    replace(
                    lower(
                        replace(
                            translate(legalentityname, '-,.;!?@#$%^&*()/"«»', ''), '"', ''
                            )
                        ), 'inc', ''), 'ltd', ''), 'limited', ''), ' ', '')
                        as legalentityname_fix from ca_tm_drop_duplicate
    ),
    ca_tm_drop_new_duplicate as
    (
        select *
        from
        (
            select *,
            ROW_NUMBER() over (partition by legalentityname_fix order by st13applicationnumber asc) as index_legalnamefix
            from ca_tm_fix_legalname
        ) b
        where index_legalnamefix = 1
    )
    select * from ca_tm_drop_new_duplicate
    """
    if no_of_rows is not None:
        query_data += f" limit {no_of_rows}"
    impala_cur.execute(query_data)
    columns = [column[0] for column in impala_cur.description]
    data = impala_cur.fetchall()
    df = pd.DataFrame(data)
    df.columns = columns
    return df

def merge_postalcode(df):
    df = df.sort_values(by=["postalcode_encode"])
    print(df[['st13applicationnumber', 'legalentityname_fix', 'postalcode', 'postalcode_encode']])

def process_data(datapath):
    df = pd.read_csv(datapath)
    df = df.sort_values(by=["legalentityname_fix"])
    df['postalcode_encode']=df.postalcode.astype('category').cat.codes
    # print(len(set(df.postalcode_encode.to_list())))
    # print(df)
    merge_postalcode(df)

if __name__ == "__main__":
    # impala_con = connect(host=os.getenv('HOST'))
    # impala_cur = impala_con.cursor()
    # df = query_table(impala_cur, 'ca_tm_applicant', no_of_rows=None)
    # df.to_csv("data/applicant_.csv")
    process_data("/mnt/d/work/cipo/data/applicant_.csv")


# with ca_tm_drop_duplicate as
# (   
#     select *
#     from
#     (
#         select *,
#         ROW_NUMBER() over (partition by st13applicationnumber order by st13applicationnumber asc) as index_st13,
#         ROW_NUMBER() over (partition by legalentityname order by st13applicationnumber asc) as index_legalname
#         from ca_tm_applicant
#         -- where nationallegalentitycode = 'CA'
#     ) a
#     where index_st13 = 1 and index_legalname = 1
# ), 
# ca_tm_fix_legalname as
# (
#     select *, replace(
#                 replace(
#                 replace(
#                 replace(
#                 lower(
#                     replace(
#                         translate(legalentityname, '-,.;!?@#$%^&*()/"«»', ''), '"', ''
#                         )
#                     ), 'inc', ''), 'ltd', ''), 'limited', ''), ' ', '')
#                     as legalentityname_fix from ca_tm_drop_duplicate
# ),
# ca_tm_drop_new_duplicate as
# (
#     select *
#     from
#     (
#         select *,
#         ROW_NUMBER() over (partition by legalentityname_fix order by st13applicationnumber asc) as index_legalnamefix
#         from ca_tm_fix_legalname
#     ) b
#     where index_legalnamefix = 1
# )

# -- select st13applicationnumber, legalentityname, legalentityname_fix from ca_legalname
# -- order by legalentityname asc

# -- select count(*) from ca_tm_fix_legalname

# select count(*) from ca_tm_drop_new_duplicate


import pandas as pd
import connect
from etl_sql_queries import sharesale_insert
from create_tables import drop_tables, create_tables



def process_data(cur, conn, filepath):
    df = pd.read_csv(filepath)
    print('Read df')
    df['ts'] = df.date.astype(str).str.cat(df.time.astype(str), sep=' ')
    print('converted times')

    share_data = df[['ts', 'price', 'size']].values
    print('processed share_data')
    i = 0
    for s in share_data:
        cur.execute(sharesale_insert, s)
        if i % 10000 == 0:
            print(i)
            conn.commit()
            break
            # print('  Inserting:', s)
        i += 1

    conn.commit()
    print('  -- Finished!')


def show_first_rows(cur, conn, table, n):
    cur.execute('SELECT * FROM {} LIMIT {}'.format(table, n))
    conn.commit()
    for row in cur.fetchall():
        print(row, row[1].timestamp())


if __name__ == '__main__':
    try:
        input('This will drop all tables, press Enter to continue.')
        cur, conn = connect.connect(autocommit=False)
        drop_tables(cur, conn)
        create_tables(cur, conn)
        process_data(cur, conn, './data/ticks.csv')
        show_first_rows(cur, conn, 'sharesales', 12)
    finally:
        conn.close()

import connect

class SelectLargestOrders:
    select_largest_orders = ("""
        SELECT ts, size FROM sharesales WHERE size > %(min_size)s;
    """)
    result_cur = None

    def __init__(self, min_size):
        self.min_size = min_size
        self.description = 'Select share sales with size > ' + str(min_size)

    def run(self, cur, conn):
        cur.execute(self.select_largest_orders, {'min_size': self.min_size})
        conn.commit()

        self.result_cur = cur

    def display_sample(self, n=12):
        if self.result_cur is None:
            print('Cursor has not be set')
        print(self.description)
        print('Rows found:', self.result_cur.rowcount, '(printing first {})'.format(n))
        i = 0
        for row in self.result_cur.fetchall():
            self.print_row(row)

            if i > n:
                break
            i += 1

        self.result_cur = None

    def print_row(self, row):
        print(row[0].strftime("%d-%b-%Y (%H:%M:%S.%f)"), row[1])


def run(cur, conn):
    select = SelectLargestOrders(min_size=500)
    select.run(cur, conn)
    select.display_sample(20)


if __name__ == '__main__':
    try:
        cur, conn = connect.connect(autocommit=True)
        run(cur, conn)
    finally:
        conn.close()

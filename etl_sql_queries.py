

sharesale_table_create = ("""
    CREATE TABLE IF NOT EXISTS sharesales
    (
        sharesale_id SERIAL PRIMARY KEY,
        ts timestamp(5) NOT NULL,
        price numeric NOT NULL,
        size int NOT NULL
    );
""")

sharesale_table_drop = ("""
    DROP TABLE IF EXISTS sharesales;
""")

sharesale_insert = ("""
    INSERT INTO sharesales (ts, price, size)
    VALUES (%s, %s, %s);
""")

create_table_queries = [sharesale_table_create]
drop_table_queries = [sharesale_table_drop]

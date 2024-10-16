from sqlite3 import Row, connect

from jankenschema import DbColumn, get_ts_code, get_rs_code


def test_ts(snapshot):
    conn = connect(":memory:")
    cursor = conn.cursor()
    column_defs = [
        DbColumn(Row(cursor, (1, "id", "INTEGER", 0, None, 1))),
        DbColumn(Row(cursor, (2, "name", "TEXT", 1, None, 0))),
        DbColumn(Row(cursor, (3, "age", "INTEGER", 0, "9", 0))),
        DbColumn(Row(cursor, (4, "cash", "REAL", 0, "4.2", 0))),
        DbColumn(Row(cursor, (5, "dep", "TEXT", 0, "dev-\"big\"'BIG'", 0))),
    ]

    ts_code = get_ts_code("ts_test_table", column_defs)
    rs_code = get_rs_code("rs_test_table", column_defs)

    snapshot.assert_match(ts_code, "test_ts_code.ts")
    snapshot.assert_match(rs_code, "test_rs_code.rs")

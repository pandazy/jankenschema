import sqlite3

import pytest

from jankenschema import get_schemas, DbColumn


@pytest.fixture(scope="function")
def mem_db():
    conn = sqlite3.connect(":memory:")
    conn.execute(
        "CREATE TABLE test_table (id INT PRIMARY KEY, name TEXT NOT NULL, age INT DEFAULT 9, cash REAL DEFAULT 4.2)"
    )
    yield conn


def test_read(mem_db):
    with mem_db as conn:
        cursor = conn.cursor()
        schemas = get_schemas(conn.cursor())

        expected = {
            "test_table": [
                DbColumn(sqlite3.Row(cursor, (1, "id", "INT", 0, None, 1))),
                DbColumn(sqlite3.Row(cursor, (2, "name", "TEXT", 1, None, 0))),
                DbColumn(sqlite3.Row(cursor, (3, "age", "INT", 0, "9", 0))),
                DbColumn(sqlite3.Row(cursor, (4, "cash", "REAL", 0, "4.2", 0))),
            ]
        }
        assert schemas == expected

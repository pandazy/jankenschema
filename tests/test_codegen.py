import os
from sqlite3 import connect, Row
from jankenschema import generate_code


TEST_INIT_SQL = """
CREATE TABLE user (
    id INT PRIMARY KEY,
    name TEXT NOT NULL,
    age INT DEFAULT 9,
    cash REAL DEFAULT 4.2
);
CREATE TABLE vendors (
    id INT PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT,
    phone TEXT
);
"""

TEST_ASSET_PATH = os.path.join(os.getcwd(), "tests/assets")
TEST_DB_PATH = os.path.join(TEST_ASSET_PATH, "test.db")


def clean_assets():
    for root, dirs, files in os.walk(TEST_ASSET_PATH, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(
                filename, 0o777
            )  # Change permissions to ensure delete ability on all platforms
            os.remove(filename)
            print(f"Deleted file: {filename}")
        for name in dirs:
            dir_path = os.path.join(root, name)
            os.rmdir(dir_path)
            print(f"Deleted directory: {dir_path}")


def init():
    clean_assets()
    with connect(TEST_DB_PATH) as conn:
        conn.executescript(TEST_INIT_SQL)
        conn.commit()


def test_generating_ts_code():
    init()
    assert not os.path.exists(os.path.join(TEST_ASSET_PATH, "user.ts"))
    assert not os.path.exists(os.path.join(TEST_ASSET_PATH, "vendors.ts"))

    generate_code(TEST_DB_PATH, TEST_ASSET_PATH, "ts")
    assert os.path.exists(os.path.join(TEST_ASSET_PATH, "user.ts"))
    assert os.path.exists(os.path.join(TEST_ASSET_PATH, "vendors.ts"))

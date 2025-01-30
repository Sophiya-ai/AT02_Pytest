import pytest

from HW_DB import init_db, add_user, get_user


@pytest.fixture
def db_conn():
    conn = init_db()
    yield conn
    conn.close()


def test_add_get_user(db_conn):
    add_user(db_conn, 'Alexey', 45)
    user = get_user(db_conn, 'Alexey')
    assert user == ('Alexey', 45)

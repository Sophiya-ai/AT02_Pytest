import pytest

from HW_DB import init_db, add_user, get_user, get_all_records


@pytest.fixture
def db_conn():
    conn = init_db()
    yield conn
    conn.close()


@pytest.mark.parametrize("name, age", [
    ("Ali", 30),
    ("Bob", 25),
    ("Carlie", 35)
])
def test_add(db_conn, name, age):
    add_user(db_conn, name, age)
    user = get_user(db_conn, name)
    assert user is not None
    assert user[0] == name
    assert user[1] == age


def test_add_get_user(db_conn):
    add_user(db_conn, 'Alexey', 45)
    user = get_user(db_conn, 'Alexey')
    assert user == ('Alexey', 45)

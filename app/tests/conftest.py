
"""FitTrack PostgreSQL API test fixture. Run only against fittrack_test."""

import os

import psycopg
import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient

load_dotenv()

TEST_DB_NAME = os.getenv("TEST_DB_NAME")

REQUIRED_TABLES = {
    "foods",
    "food_entries",
    "goals",
    "body_weights"
}


def _verify_database(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT current_database()")
        actual = cursor.fetchone()[0]

        if actual != "fittrack_test":
            raise RuntimeError(
                f"REFUSING test database operation: "
                f"connected to {actual!r}, not fittrack_test"
            )

        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
        """)

        existing = {row[0] for row in cursor.fetchall()}
        missing = REQUIRED_TABLES - existing

        if missing:
            raise RuntimeError(
                f"Missing tables in fittrack_test: {sorted(missing)}"
            )


def _clear_database(connect):
    with connect() as connection:
        _verify_database(connection)

        with connection.cursor() as cursor:
            cursor.execute("""
                TRUNCATE TABLE
                    food_entries,
                    foods,
                    goals,
                    body_weights
                RESTART IDENTITY CASCADE
            """)


@pytest.fixture
def client(monkeypatch):

    if TEST_DB_NAME != "fittrack_test":
        raise RuntimeError(
            "Set TEST_DB_NAME=fittrack_test in your local .env "
            "before running tests"
        )

    original_connect = psycopg.connect

    def test_connect(*args, **kwargs):

        if args:
            raise RuntimeError(
                "Test fixture cannot safely redirect "
                "a positional PostgreSQL DSN"
            )

        # Start with the test database credentials.
        test_config = {
            "host": os.getenv("DB_HOST"),
            "port": os.getenv("DB_PORT", "5432"),
            "dbname": TEST_DB_NAME,
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD")
        }

        # Preserve any additional connection options.
        kwargs = dict(kwargs)
        kwargs.pop("database", None)
        kwargs.pop("dbname", None)

        test_config.update(kwargs)

        # Never allow application arguments to override the test database.
        test_config["dbname"] = TEST_DB_NAME

        connection = original_connect(**test_config)

        try:
            _verify_database(connection)

        except BaseException:
            connection.close()
            raise

        return connection

    # Verify the database before redirecting application connections.
    _clear_database(test_connect)

    monkeypatch.setattr(psycopg, "connect", test_connect)

    try:
        from main import app

        with TestClient(app) as test_client:
            yield test_client

    finally:
        _clear_database(test_connect)

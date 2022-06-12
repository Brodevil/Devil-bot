from logging import getLogger

from src.constants import Client, DB_Scripts
from mysql.connector import connect, Error
import config

__all__ = ["Database"]
log = getLogger(__name__)


class Database:
    def __init__(self) -> None:
        """Connect to database"""
        self.connection = self.connect_db()
        self.cursor = self.connection.cursor()
        self.create_tables()

    def connect_db(self) -> connect:
        """Connect to database"""
        try:
            connection = connect(
                host=Client.DB_HOST,
                user=Client.DB_USER,
                passwd=Client.DB_PASSWORD,
                database=Client.DB_NAME,
                port=Client.DB_PORT,
            )
            log.info("Connected to database")
            return connection
        except Error as error:
            log.error(error)

    def reconnect(self) -> None:
        """Reconnect to database"""
        self.connection.reconnect(attempt=2, deplay=0)

    def run(self, query: str, commit: bool = False) -> None:
        """Execute query"""
        try:
            self.cursor.execute(query)
            if commit:
                self.connection.commit()
        except Error as error:
            log.error(error)

    def create_tables(self) -> None:
        """Create tables"""
        if config.SETUP:
            self.run(DB_Scripts.bans, commit=True)

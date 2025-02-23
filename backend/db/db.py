import mysql.connector
from typing import Any, Tuple, Dict, Any, List, cast
from config import Config

class DB:
    closed = False
    def __init__(self):
        self.conn = mysql.connector.connection.MySQLConnection(
            host = Config.DB_HOST,
            user = Config.DB_USER,
            password = Config.DB_PASS,
            database = Config.DB_SCHEMA
        )
    
    def close(self):
        self.conn.close()
        self.closed = True

    def insert(self, query: str, args: Tuple = (), lastrowid=True):
        """
        Executes a query and returns the result.
        
        Args:
            conn: MySQL connection object
            query: SQL query string
            args: Query parameters as tuple
            
        Returns:
            List of dictionaries for SELECT queries
            Last insert id for INSERT queries
            Number of affected rows for UPDATE/DELETE queries
        """
        if self.closed is True:
            raise ValueError("DB connection was already closed!")
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query, args)
        self.conn.commit()
        if lastrowid:
            result = cursor.lastrowid
        else:
            result = cursor.rowcount
        
        return result

    def read(self, query: str, args: Tuple = ()) -> List[Dict[str, Any]]:
        """
        Executes a query and returns the result.
        
        Args:
            conn: MySQL connection object
            query: SQL query string
            args: Query parameters as tuple
            
        Returns:
            List of dictionaries for SELECT queries
            Last insert id for INSERT queries
            Number of affected rows for UPDATE/DELETE queries
        """
        if self.closed is True:
            raise ValueError("DB connection was already closed!")
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query, args)
        
        result = cast(List[Dict[str, Any]], cursor.fetchall())
            
        cursor.close()
        return result


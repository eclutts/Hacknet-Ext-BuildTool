# Instantiates the entire thing.

import psycopg
from config import config

def init_this(name):
    """ Creates a database, then creates all tables """
    commands = (
        """
        CREATE DATABASE 
        """
    )
import datetime

import asyncio
import asyncpg

from config import settings


async def connect_db():
    conn = await asyncpg.connect(**settings.PG_CREDS)
    await conn.execute('''
            CREATE TABLE users(
                id serial PRIMARY KEY,
                name text,
                dob date
            )
        ''')


    # Insert a record into the created table.
    await conn.execute('''
            INSERT INTO users(name, dob) VALUES($1, $2)
        ''', 'Bob', datetime.date(1984, 3, 1))

    # Select a row from the table.
    row = await conn.fetchrow(
        'SELECT * FROM users WHERE name = $1', 'Bob')
    # *row* now contains
    # asyncpg.Record(id=1, name='Bob', dob=datetime.date(1984, 3, 1))

    # Close the connection.
    await conn.close()

# db.py
import aiosqlite

DB_PATH = "bot.db"

async def init_db():
    """Initialize the database and tables"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT
            )
        """)
        await db.commit()

async def add_user(user_id: int, first_name: str, last_name: str):
    """Add a new user or ignore if already exists"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (user_id, first_name, last_name) VALUES (?, ?, ?)",
            (user_id, first_name, last_name)
        )
        await db.commit()

async def get_users():
    """Get all registered users"""
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            return await cursor.fetchall()

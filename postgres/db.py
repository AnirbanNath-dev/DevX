from asyncpg import Connection , connect
from bot.settings import POSTGRES_URI

async def setup_db():
    try:
        conn : Connection = await connect(
            POSTGRES_URI
        )
        print(f"Connected to postgres:{conn.get_server_version()} successfully")
        
        return conn
    
    except Exception as e:
        print("Failed to connect to db : " , str(e))
        return None


    
async def close_db(conn : Connection):
    try:
        await conn.close()
        print(f"Disconnected from postgres:{conn.get_server_version()} successfully")
    except Exception as e:
        print("Failed to disconnect from db : " , e)
        
        
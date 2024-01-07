from fastapi import FastAPI
from datetime import datetime

from .transport_bd.CONSTANTS import bd_connect_root
from .transport_bd.select_all_table import select_all_table
from .transport_bd.write_sql_information import write_sql_information

app = FastAPI()

bd_connect = bd_connect_root()

@app.post("/transport")
async def connect_nfc_transport(uid: str, owner: str):
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

    write_sql_information(bd_connect, uid, owner, formatted_date)

@app.get("/")
async def root():
    return select_all_table(bd_connect)

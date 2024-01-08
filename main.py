from flask import Flask, request
from datetime import datetime

from transport_bd.CONSTANTS import bd_connect_root
from transport_bd.select_all_table import select_all_table
from transport_bd.write_sql_information import write_sql_information

app = Flask(__name__)

bd_connect = bd_connect_root()


@app.route('/transport', methods=['POST'])
async def connect_nfc_transport():
    connect_data = request.form
    uid = connect_data.get('uid')
    owner = connect_data.get('owner')

    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

    write_sql_information(bd_connect, uid, owner, formatted_date)

    return {"status": "ok"}


@app.route('/', methods=['GET'])
async def root():
    transports = select_all_table(bd_connect)

    if transports:
        return {"transport_bd": transports}
    else:
        return {"status": "В базе данных нету информации"}


if __name__ == '__main__':
    app.run()

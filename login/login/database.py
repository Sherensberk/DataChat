from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import urllib
from login.settings import Settings

params = urllib.parse.quote_plus(
    'Driver=%s;' % Settings().DATABASE_DRIVER +
    'Server=tcp:%s,1433;' % Settings().DATABASE_SERVER +
    'Database=%s;' % Settings().DATABASE +
    'Uid=%s;' % Settings().DATABASE_USERNAME +
    'Pwd={%s};' % Settings().DATABASE_PASSWORD +
    'Encrypt=yes;' +
    'TrustServerCertificate=no;' +
    'Connection Timeout=30;')

conn_str = 'mssql+pyodbc:///?odbc_connect=' + params
engine = create_engine(conn_str)

def get_session():
    with Session(engine) as session:
        yield session

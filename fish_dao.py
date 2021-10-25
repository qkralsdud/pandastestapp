import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import sqlalchemy as db
from data.fish_traindata import getTrain_Data
from data.fish_testdata import getTest_Data

# dict타입으로 insert하고 dict타입으로 select하는게 가장 편함 - pymysql 라이브러리(mysql, maria)

# DataFrame도 DB에 insert하고 select가능 - SQLAlchemy(ORM)
# class타입으로도 insert하고 select가능

engine = db.create_engine("mariadb+mariadbconnector://python:python1234@127.0.0.1:3306/pythondb")

def insert():
    fishs = getTrain_Data()
    fishs.to_sql("train", engine, index=False, if_exists="replace")

def insert_Test():
    fish_test = getTest_Data()
    fish_test.to_sql("test", engine, index=False, if_exists = "replace")

insert_Test()

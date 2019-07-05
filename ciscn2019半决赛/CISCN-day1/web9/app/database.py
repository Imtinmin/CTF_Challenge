from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
	__tablename__ = 'user'
	uid = Column(Integer, primary_key=True, autoincrement=True)
	username = Column(String(1024))
	password = Column(String(64))


class Blog(Base):
	__tablename__ = 'blog'
	bid = Column(Integer, primary_key=True, autoincrement=True)
	uid = Column(Integer)
	content = Column(String(1024))
	timestamp = Column(DateTime, default=datetime.utcnow)


# 初始化数据库连接:
engine = create_engine('sqlite:///main.db' , connect_args={'check_same_thread': False})

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
session = DBSession()

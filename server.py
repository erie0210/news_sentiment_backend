from datetime import datetime
from flask import Flask, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import DateTime, Integer, String

# Model의 예시
class TestTable(Base):
    __tablename__ = 'Test Table'
    id   = Column(Integer, primary_key=True)
    key  = Column(String, nullable=False)
    val  = Column(String)
    date = Column(DateTime, default=datetime.utcnow)


db_uri = 'mysql://test...'
engine = create_engine(db_uri)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

app = Flask(__name__)

def getDatabase(category):
  result = session.query('CRAWLING').filter(TestTable.category==category).all()
  session.commit()
  session.close()
  return jsonify(result)

@app.route('/politics')
def selectpolitics():
  getDatabase('politics')

@app.route('/economic')
def selectpolitics():
  getDatabase('economic')

@app.route('/digital')
def selectpolitics():
  getDatabase('digital')

@app.route('/editorial')
def selectpolitics():
  getDatabase('editorial')

@app.route('/society')
def selectpolitics():
  getDatabase('society')

@app.route('/foreign')
def selectpolitics():
  getDatabase('foreign')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='80')
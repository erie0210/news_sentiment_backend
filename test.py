import unittest
from flask import Flask
from server import getDatabase

class Test(unittest.TestCase):

    def test_get_database(self):
      category = ['politics', '/economic', 'digital'] # 나머지 카테고리 생략
      for cat in category:
        result = getDatabase(cat)
        self.assertTrue(result)

    def test_transaction_donnot_persist(db_session):
      politics_result = getDatabase('politics')
      economic_result = getDatabase('economic')
      assert politics_result[0] != economic_result[0]


if __name__ == '__main__':
    unittest.main()
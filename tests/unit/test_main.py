import unittest
from main import DataBase

class TestMain(unittest.TestCase):

    def test_connect(self):
        self.assertEqual(DataBase.connect,)
        pass

    def test_session(self):
        pass

    def test_create_database(self):
        pass

    def test_status(self):
        pass

    def test_cursor(self):
        pass

    def test_select_table(self):
        pass

    def test_create_table(self):
        pass

    def test_insert_rows(self):
        pass

    def test_show_table(self):
        pass

    def test_drop_table(self):
        pass

    def test_close(self):
        pass

if __name__ == '__main__':
    unittest.main()
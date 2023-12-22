import unittest

from hash_table import HashTable


# table-driven unit tests for HashTable class
class HashTableTest(unittest.TestCase):

    def test_hash_function_collision(self):
        table = HashTable(10)
        self.assertEqual(table.hash_function('cinema'), table.hash_function('iceman'))

    def test_insert(self):
        table = HashTable(10)
        table.insert('key', 'value')
        self.assertEqual(table.get('key'), 'value')

    def test_insert_collision(self):
        table = HashTable(10)
        table.insert('cinema', 'value')
        table.insert('iceman', 'value2')
        self.assertEqual(table.get('cinema'), 'value')
        self.assertEqual(table.get('iceman'), 'value2')

    def test_get_missing(self):
        table = HashTable(10)
        self.assertIsNone(table.get('key'))

    def test_get_collision(self):
        table = HashTable(10)
        table.insert('cinema', 'value')
        self.assertIsNone(table.get('iceman'))

    def test_delete(self):
        table = HashTable(10)
        table.insert('key', 'value')
        self.assertEqual(table.get('key'), 'value')
        table.delete('key')
        self.assertIsNone(table.get('key'))

    def test_delete_collision(self):
        table = HashTable(10)
        table.insert('cinema', 'value')
        table.insert('iceman', 'value2')
        self.assertEqual(table.get('cinema'), 'value')
        self.assertEqual(table.get('iceman'), 'value2')
        table.delete('cinema')
        self.assertIsNone(table.get('cinema'))
        self.assertEqual(table.get('iceman'), 'value2')


if __name__ == '__main__':
    unittest.main()

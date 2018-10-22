#!/usr/bin/python3
import unittest
from models.base import Base


class TestBaseClassID(unittest.TestCase):

    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base("hi!")
        self.assertEqual(b3.id, "hi!")
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base(-1)
        self.assertEqual(b5.id, -1)
        b6 = Base(1.5)
        self.assertEqual(b6.id, 1.5)
        b7 = Base(["hi", "there"])
        self.assertEqual(b7.id, ["hi", "there"])
        b8 = Base(("what's", "up"))
        self.assertEqual(b8.id, ("what's", "up"))
        b9 = Base({"greeting": "Hey!", "number": 9})
        self.assertEqual(b9.id, {"greeting": "Hey!", "number": 9})

if __name__ == '__main__':
    unittest.main()

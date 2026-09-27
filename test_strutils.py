"""strutils 的单元测试。"""

import unittest

from strutils import count_words, is_palindrome, reverse_words


class TestIsPalindrome(unittest.TestCase):
    """is_palindrome 的测试。"""

    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("level"))

    def test_ignores_case_and_punctuation(self):
        """带大小写、逗号、冒号和空格的长回文。"""
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_char(self):
        self.assertTrue(is_palindrome("a"))

    def test_not_a_palindrome(self):
        """反向用例：确认函数不会无脑返回 True。"""
        self.assertFalse(is_palindrome("hello"))


class TestExistingFunctions(unittest.TestCase):
    """既有函数的基础测试，防止改动时误伤。"""

    def test_count_words(self):
        self.assertEqual(count_words("hello world"), 2)

    def test_reverse_words(self):
        self.assertEqual(reverse_words("hello world"), "world hello")


if __name__ == "__main__":
    unittest.main()

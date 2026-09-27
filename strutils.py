"""strutils —— 一组常用的字符串处理小工具。"""

import re


def count_words(text: str) -> int:
    """返回文本中的单词数量。"""
    return len(text.split())


def reverse_words(text: str) -> str:
    """反转文本中单词的顺序。"""
    return " ".join(reversed(text.split()))


def is_palindrome(text: str) -> bool:
    """判断文本是否为回文（忽略大小写、标点与空格）。"""
    normalized = re.sub(r"[^a-z0-9]", "", text.lower())
    return normalized == normalized[::-1]

"""strutils —— 一组常用的字符串处理小工具。"""


def count_words(text: str) -> int:
    """返回文本中的单词数量。"""
    return len(text.split())


def reverse_words(text: str) -> str:
    """反转文本中单词的顺序。"""
    return " ".join(reversed(text.split()))

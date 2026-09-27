# strutils

一组常用的字符串处理小工具。

## 函数一览

| 函数 | 说明 |
| --- | --- |
| `count_words(text)` | 返回文本中的单词数量 |
| `reverse_words(text)` | 反转文本中单词的顺序 |
| `is_palindrome(text)` | 判断文本是否为回文 |

## 使用

```python
from strutils import count_words, reverse_words

count_words("hello world")      # 2
reverse_words("hello world")    # "world hello"
```

## 开发约定

本仓库采用 feature 分支 + Pull Request 的方式协作，禁止直接向 `main` 推送。

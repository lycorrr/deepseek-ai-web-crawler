# config.py

BASE_URL = "https://book.douban.com/latest"
# 抓取每本书所在的 li.media 节点，保留结构化 HTML
CSS_SELECTOR = ".list li.media"
REQUIRED_KEYS = [
    "name",
    "author",
    "publisher",
    "pub_date",
    "rating",
    "reviews",
    "description",
]

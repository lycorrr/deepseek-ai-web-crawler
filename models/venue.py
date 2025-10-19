from pydantic import BaseModel


class Venue(BaseModel):
    """
    Represents the data structure of a Book (for Douban).
    """

    name: str              # 书名
    author: str            # 作者
    publisher: str         # 出版社
    pub_date: str          # 出版日期
    rating: float          # 评分
    reviews: int           # 评价人数
    description: str       # 简介

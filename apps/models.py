from exts import db
from datetime import datetime

# 板块
class BoardModel(db.Model):
    __tablename__ = 'board'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)

# 发布帖子
class PostModel(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(200),nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)

    author_id = db.Column(db.String(100),db.ForeignKey("cms_user.id"),nullable=False)
    # 一对多关联,backref,反向引用的字段名，相当于在关联模型中自动添加了一个字段，

    author = db.relationship("CMSUser",backref='posts')

from flask import Blueprint,render_template,request,g
from ..models import BoardModel ,PostModel
from .forms import AddPostForm
from utils import restful
from exts import db
bp=Blueprint("front",__name__)


@bp.route('/')
def index():
    # banners = BannerModel.query.order_by(BannerModel.priority.desc()).all()
    boards = BoardModel.query.all()
    context = {
        # 'banners': banners,
        'boards': boards
    }
    return render_template('front/front_index.html', **context)


# 帖子列表
@bp.route('/posts/')
def posts():
    content = {
        'questions': db.session.query(PostModel).order_by(PostModel.create_time.desc()).all()
    }
    return render_template('front/front_index.html', **content)


# 发布帖子
@bp.route('/apost/', methods=['POST'])
def apost():
        form = AddPostForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            # board_id = form.board_id.data
            # board = BoardModel.query.get(board_id)
        # if not board:
        #     return restful.params_error(message='没有这个板块！')
            post = PostModel(title=title,content=content)
            # post.board = board
            post.author = g.cms_user
            db.session.add(post)
            db.session.commit()
            return "发布成功"
        else:
            return restful.params_error(message=form.get_error())

# 帖子详情
@bp.route('/detail/<question_id>/')
def detail(question_id):
    question_model = PostModel.query.filter_by(id=question_id).first()
    return render_template('detail.html', question=question_model)



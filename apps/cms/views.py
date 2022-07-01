from flask import  Blueprint,views,render_template,request,redirect,url_for,g,session
from .forms import LoginForm,AddBoardForm,UpdateBoardForm
bp=Blueprint("cms",__name__,url_prefix='/cms')
from .models import CMSUser
from ..models import BoardModel
    # ,PostModel
import config,string
# from flask_mail import Message
from utils import restful
from exts import db

@bp.route('/')
def index():
    return render_template('cms/cms_index.html')

# 登录
class LoginView(views.MethodView):
    def get(self,message=None):
        return render_template('cms/cms_login.html')
    def post(self):
        form=LoginForm(request.form)
        if form.validate():
            email=form.email.data
            password=form.password.data
            remember=form.remember.data
            # save_log(email)
            user=CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID]=user.id#保存用户的登录信息
                if remember:
                    session.permanent = True  # 过期时间为31天

                return redirect(url_for('cms.index'))
            else:
                return "邮箱或密码错误"
        else:
            return "表单验证错误"
            # return redirect(url_for('front.signup'))
bp.add_url_rule('/login/',view_func=LoginView.as_view('login'))

#个人信息详情页
@bp.route('/profile/')
def profile():
    return render_template('cms/cms_profile.html')


# 引入g对象，验证用户是否已登陆；g 是一个特殊对象，独立于每一个请求。在处理请求过程中，它可以用于储存 可能多个函数都会用到的数据。把连接储存于其中，可以多次使用，而不用在同一个 请求中每次调用 get_db 时都创建一个新的连接。
@bp.before_request
def before_request():
    if config.CMS_USER_ID in session:
        user_id = session.get(config.CMS_USER_ID)
        user = CMSUser.query.get(user_id)
        if user:
            g.cms_user=user

# 模块
@bp.route('/boards/')
def boards():
    all_boards = BoardModel.query.all()
    context = {
        'boards': all_boards
    }
    return render_template('cms/cms_boards.html',**context)

# 增加板块
@bp.route('/aboard/',methods=['POST'])
def aboard():
    form=AddBoardForm(request.form)
    if form.validate():
        name=form.name.data
        board = BoardModel(name=name)
        db.session.add(board)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(message=form.get_error())

# 编辑板块
@bp.route('/uboard/',methods=['POST'])
def uboard():
    form = UpdateBoardForm(request.form)
    if form.validate():
        board_id = form.board_id.data
        name = form.name.data
        board = BoardModel.query.get(board_id)
        if board:
            board.name = name
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message='没有这个板块！')
    else:
        return restful.params_error(message=form.get_error())

# 删除板块
@bp.route('/dboard/',methods=['POST'])
def dboard():
    board_id = request.form.get("board_id")
    if not board_id:
        return restful.params_error('请传入板块id！')

    board = BoardModel.query.get(board_id)
    if not board:
        return restful.params_error(message='没有这个板块！')

    db.session.delete(board)
    db.session.commit()
    return restful.success()



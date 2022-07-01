from ..forms import BaseForm
from wtforms import StringField,IntegerField,SubmitField
from wtforms.validators import Regexp,EqualTo,ValidationError,InputRequired
# from utils import zlcache


class AddPostForm(BaseForm):
    title = StringField(validators=[InputRequired(message='请输入标题！')])
    content = StringField(validators=[InputRequired(message='请输入内容！')])
    board_id = IntegerField(validators=[InputRequired(message='请输入板块id！')])
    submit=SubmitField('发表')

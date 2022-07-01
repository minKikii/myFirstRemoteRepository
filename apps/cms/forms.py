from wtforms import Form,StringField,IntegerField,FileField
from wtforms.validators import Email,InputRequired,Length
from  flask_wtf.file import FileRequired,FileAllowed
from wtforms.validators import InputRequired#必须输入
from ..forms import BaseForm

class LoginForm(BaseForm):
    email=StringField(validators=[Email(message='请输入正确的邮箱格式'),InputRequired(message='请输入邮箱')])
    password=StringField(validators=[Length(6,20,message='请输入正确格式的密码')])
    remember=IntegerField()#html中置记住为1

# 增加板块
class AddBoardForm(BaseForm):
    name=StringField(validators=[InputRequired(message='请输入板块名称！')])


# 更新板块
class UpdateBoardForm(AddBoardForm):
    board_id = IntegerField(validators=[InputRequired(message='请输入板块id！')])
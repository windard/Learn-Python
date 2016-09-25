#!/usr/bin/env python
#coding=utf-8

import os
import string
import random
import StringIO
import Image, ImageDraw, ImageFont, ImageFilter

from flask import Flask,session,render_template,flash

from flask_wtf import Form
from flask_wtf.csrf import CsrfProtect
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo,Length

#map:将str函数作用于后面序列的每一个元素
chars = (string.uppercase + string.digits).replace('0','').replace('O','').replace('1','').replace('I','').replace('2','').replace('Z','').replace('Q','')

def create_validate_code(size=(120, 30),
                         chars=chars,
                         mode="RGB",
                         bg_color=(255, 255, 255),
                         fg_color=(255, 0, 0),
                         font_size=22,
                         font_type="Monaco.ttf",
                         length=4,
                         draw_points=True,
                         point_chance = 4):
    '''''
    size: 图片的大小，格式（宽，高），默认为(120, 30)
    chars: 允许的字符集合，格式字符串
    mode: 图片模式，默认为RGB
    bg_color: 背景颜色，默认为白色
    fg_color: 前景色，验证码字符颜色
    font_size: 验证码字体大小
    font_type: 验证码字体，默认为 Monaco.ttf
    length: 验证码字符个数
    draw_points: 是否画干扰点
    point_chance: 干扰点出现的概率，大小范围[0, 50]
    '''

    bg_color = tuple(random.randint(196,256) for x in xrange(3))
    # bg_color = (127,231,185)
    fg_color = tuple(random.randint(0,125) for x in xrange(3))
    # fg_color = (78,12,36)

    width, height = size
    img = Image.new(mode, size, bg_color) # 创建图形
    draw = ImageDraw.Draw(img) # 创建画笔

    def get_chars():
        '''''生成给定长度的字符串，返回列表格式'''
        return random.sample(chars, length)

    def create_points():
        '''''绘制干扰点'''
        chance = min(50, max(0, int(point_chance))) # 大小限制在[0, 50]

        for w in xrange(width):
            for h in xrange(height):
                tmp = random.randint(0, 50)
                if tmp > 50 - chance:
                    draw.point((w, h), fill=(0, 0, 0))

    def create_strs():
        '''''绘制验证码字符'''
        c_chars = get_chars()
        strs = '%s' % ''.join(c_chars)

        font = ImageFont.truetype(font_type, font_size)
        font_width, font_height = font.getsize(strs)

        draw.text(((width - font_width) / 3, (height - font_height) / 4),
                    strs, font=font, fill=fg_color)

        return strs

    if draw_points:
        create_points()
    strs = create_strs()

    # 图形扭曲参数
    params = [1 - float(random.randint(1, 2)) / 100,
              0,
              0,
              0,
              1 - float(random.randint(1, 10)) / 100,
              float(random.randint(1, 2)) / 500,
              0.001,
              float(random.randint(1, 2)) / 500
              ]
    img = img.transform(size, Image.PERSPECTIVE, params) # 创建扭曲

    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE) # 滤镜，边界加强（阈值更大）

    return img,strs

csrf = CsrfProtect()
app = Flask(__name__)
csrf.init_app(app)
app.secret_key = os.urandom(30)

class RegisterForm(Form):
    """注册表单"""
    # SECRET_KEY = os.urandom(30)
    username = StringField(u'昵称', validators=[DataRequired(message=u'用户名必填')])
    email = StringField(u'邮箱', validators=[DataRequired(), Email(message=u'邮箱格式不正确')])
    password = PasswordField(u'密码', validators=[DataRequired(), Length(6, 12, message=u'密码长度在6到12为')])
    password1 = PasswordField(u'确认密码', validators=[DataRequired(), Length(6, 12, message=u'密码长度在6到12为'), EqualTo('password', message=u'密码必须一致')])
    verification_code = StringField(u'验证码', validators=[DataRequired(), Length(4, 4, message=u'填写4位验证码')])
    submit = SubmitField(u'注册')

class User(object):
  """docstring for User"""
  def __init__(self, username,password,email):
    self.username = username
    self.password = password
    self.email = email

def get_user(username):
  if username == "123":
    return True
  return False


@app.route('/')
def index():
    return 'test'

@app.route('/login')
def login():
  return "login"

@app.route('/logout')
def logout():
  return "logout"

@app.route('/code')
def code():
    #把strs发给前端,或者在后台使用session保存
    code_img,strs = create_validate_code()
    buf = StringIO.StringIO()
    code_img.save(buf,'JPEG',quality=70)
    session['code_text'] = strs
    buf_str = buf.getvalue()
    response = app.make_response(buf_str)
    response.headers['Content-Type'] = 'image/jpeg'
    return response

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        print username
        if get_user(username):
            flash(u'账号已被注册','error')
            # code_img, code_text = create_validate_code()
            # session['code_text'] = code_text
            # return render_template('register.html', form=form, code_img=code_img)
            return render_template('register.html', form=form)
        if 'code_text' in session and session['code_text'] != form.verification_code.data:
            flash(u'验证码错误 ','error')
            # code_img, code_text = create_validate_code()
            # session['code_text'] = code_text
            # return render_template('register.html', form=form, code_img=code_img)
            return render_template('register.html', form=form)
        email = form.email.data
        password = form.password.data
        user = User(username=username, password=password, email=email)
        try:
            # session.add(user)
            # session.commit()
            flash(u'注册成功','flash')
            return redirect(url_for('/'))
        except:
            # print traceback.print_exc()
            # session.rollback()
            flash(u'注册失败','error')
            # code_img, code_text = create_validate_code()
            # session['code_text'] = code_text
            return render_template('register.html', form=form)
    # code_img, code_text = create_validate_code()
    # session['code_text'] = code_text
    return render_template('register.html', form=form)

@csrf.error_handler
def csrf_error(reason):
    return render_template('csrf_error.html', reason=reason), 400

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=18888,debug=True,threaded=True)


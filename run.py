# coding:utf-8

import importlib, sys
importlib.reload(sys)

# 引入flask模块
from flask import *

# 关闭警告信息
import warnings
warnings.filterwarnings('ignore')

# 引入MYSQL
import pymysql
# from config import *
import time
app = Flask(__name__)
app.config.from_object(__name__)

# 连接数据库
def connectdb():
    db = pymysql.connect(host='127.0.0.1', port=3306, db='blogDB', user='root', passwd='zhangzk123', charset='utf8')
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)  # 默认元组 设置成字典
    return (db, cursor)

# 关闭数据库
def closedb(db, cursor):
    cursor.close()
    db.close()

# 首页
@app.route('/')
def index():
    return render_template('index.html')


# 处理表单提交
@app.route('/handle', methods=['post'])
def handle():
    # # 获取POST数据
    # data = request.form
    # # 连接数据库
    # (db, cursor) = connectdb()
    # # 添加数据
    # cursor.execute("INSERT INTO post(title,content,timestamp) VALUES(%s,%s,%s)",
    #                [data['title'], data['content'], str(int(time.time()))])
    # # 最后添加行的id
    # post_id = cursor.lastrowid
    # # 关闭数据库
    # closedb(db, cursor)
    # return redirect(url_for('post', post_id=post_id))
    return redirect(url_for('post'))


# 文章列表页
@app.route('/list')
def list():
    # # 连接数据库
    # (db, cursor) = connectdb()
    # # 查询数据库
    # cursor.execute('SELECT * FROM post')
    # data = cursor.fetchall()
    # # 格化时间
    # for i in range(0, len(data)):
    #     data[i]['timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(data[i]['timestamp'])))
    # # 关闭数据库
    # closedb(db, cursor)
    # return render_template('list.html', posts=data)
    return render_template('list.html')


# 文章详情页
# @app.route('/post/<post_id>')
# def post(post_id):
#     # 连接数据库
#     (db, cursor) = connectdb()
#     # 查询数据库
#     cursor.execute('SELECT * FROM post WHERE id=%s', [post_id])
#     data = cursor.fetchone()
#     # 格化时间
#     data['timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(data['timestamp'])))
#     # 关闭数据库
#     closedb(db, cursor)
#     return render_template('post.html', post=data)

#关于
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
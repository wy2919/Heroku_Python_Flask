from flask import Flask
from datetime import datetime
import pymysql.cursors
app = Flask(__name__)

@app.route('/')
def homepage():
    
    # 连接数据库
    connect = pymysql.Connect(
        host='remotemysql.com',  # 服务器地址
        port=3306,  # 端口
        user='JATwLEkzc0',  # 数据库用户名
        passwd='SOc711GD3A',  # 数据库密码
        db='JATwLEkzc0',  # 要连接的数据库
        charset='utf8'  # 连接编码，存在中文的时候，连接需要添加charset='utf8'，否则中文显示乱码。
    )

    # 获取游标
    cursor = connect.cursor()
    sql = "select * from qx_activity"
    # sql='insert into table_name (name)values ("asd")'
    cursor.execute(sql)
    aa = cursor.fetchall()

    print(len(aa))
    return len(aa)
#     the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

#     return """
#     <h1>Hello heroku</h1>
#     <p>It is currently {time}.</p>

#     <img src="http://loremflickr.com/600/400" />
#     """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


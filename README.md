
> [![Deploy](https://www.herokucdn.com/deploy/button.png)](https://dashboard.heroku.com/new?template=https://github.com/wy2919/Heroku_Python_Flask)


##  `Procfile`

启动命令 和启动脚本文件   web: gunicorn 文件名:app --log-file=-   启动app.py文件
~~~
web: gunicorn app:app --log-file=-
~~~

~~~
web: gunicorn gettingstarted.wsgi
# 运行gettingstarted文件夹下的wsgi.py
~~~



##  `requirements.txt`

这是pip库 一行一个

~~~
Flask
~~~


~~~
Flask
gunicorn
~~~


##  `runtime.txt`
指定py版本 

~~~sh
python-3.5.1
~~~




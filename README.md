##  `Procfile`

启动命令 和启动脚本文件   web: gunicorn 文件名:app --log-file=-   启动app.py文件
~~~
web: gunicorn app:app --log-file=-
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




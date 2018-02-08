import orm
from models import User, Blog, Comment


def test():
    #创建连接池,里面的host,port,user,password需要替换为自己数据库的信息
    yield from orm.create_pool(host='127.0.0.1', port=3306,user='root', password='Lj18119929389',db='awesome')
    #没有设置默认值的一个都不能少
    u = User(name='Test3', email='test@example2.com', passwd='12345678902', image='about:blank1',id="3")
    yield from u.save()


# SQL数据库擅长于用高效且紧凑的形式存储结构化数据
# NoSQL 数据库放宽一致性要求，从而获得性能的优势
# 对中小型程序来说，SQL和NoSQL数据库都是很好的选择，而且性能相当
# 数据库抽象层 ORM object-Relational Mapper 或 Object-Document Mapper ODM
# 在用户不知觉的情况下把高层的面向对象操作转换成低层的数据库指令
# flask-SQLAlchemy flask 扩展SQLAlchemy 框架 flask-sqlalchemy
# 数据库迁移框架 flask-Migrate 或 Alembic  flask-migrate 对Alembic轻量级包装并且可以在Flask-Script中使用
''' 大型项目的组织方式
|-flasky
|-app/
 |-templates/
 |-static/
 |-main/
  |-__init__.py
  |-errors.py
  |-forms.py
  |-views.py
 |-__init__.py
 |-email.py
 |-models.py
|-migrations/
|-tests/
 |-__init__.py
|-test*.py
|-venv/
|-requirements.txt
|-config.py
|-manage.py

Flask 程序一般都保存在名为app的包中
单元测试编写在tests包中
venv包含Python的虚拟环境
requirements.txt 依赖包
config.py 存储配置
manage.py 启动程序以及其他程序任务

pip3 freeze 打印所有的依赖
’‘’
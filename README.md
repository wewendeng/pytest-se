# pytest-se
本项目是一个基于pytest + selenium 的UI自动化框架，主要用来记录学习和总结，并且是根据目前所在公司的业务需求定制，可能并不适合所有的项目，但仍然希望可以给测试同学带来一点点帮助。最后感谢测试前辈们的指导。

# 目录结构
```
|----common/ 存放自定义工具类、方法类等常用方法
|    |----config.py
|    |----mail.py
|    |----util.py
|----conf/ 存放配置文件数据，比如数据库配置等
|    |----conf.ini
|----data/ 存放测试所需要的数据，可以是Excel等
|----libs/ 存放第三方工具包(没有提供pip安装的三方包)
|----logs/ 存放项目运行的日志，不一定在该项目下，根据具体需求
|----main/ 项目的主函数入口，或者测试流程组装
|    |----main.py
|----pom/ 存放页面对象，和UI的实际交互都在这里完成
|    |----base_page.py
|    |----register_page.py
|    |----login_page.py
|----reports/ 存放测试报告
|----screenshots/ 存放测试过程中产生的截图
|----testcases/ 存放测试用例，可以按需是否继续划分子文件夹，文件夹命名需符合pytest规范，test_*
|    |----test_user_register.py
|    |----test_user_login.py
|    |----test_admin_login.py
|----pytest.ini pytest的配置文件，此文件名不可更改，为官方固定
|----pytest_runner 项目的启动文件
|----requirements.txt 项目依赖包目录
|----README.md 项目介绍
|----.gitignore git需要忽略的文件/文件夹，比如pycharm产生的__pycache__，pytest产生的.pytest_cache等
```

# pytest运行测试用例方式
1.文件内启动
```
pytest.main(['-v', path]) 执行指定路径下的测试用例
main方法的参数必须是一个列表
```
2.命令行启动
```
pytest test.py 执行指定测试用例
```

3.标签参数和用例选择(同时适用命令启动和main函数启动)

**标签参数**

* '-s’: 关闭捕捉，输出打印信息。
* ‘-v’: 用于增长测试用例的冗长。
* ‘q’: 减小测试的运行冗长。
* ‘-k’: 运行包含某个字符串的测试用例
* ‘-x’: 出现一条测试用例失败就退出测试

标签可以组合，比如 pytest.main(['-sv', path])，但'-k'需要单独使用，因为后面需要关联关键词

**运行哪些用例**

* pytest.main('-v', base_path + '/test_admin_login.py') 执行指定模块测试用例
* pytest.main('-v', base_path + '/test_admin_login.py::test_admin_login_success') 执行指定模块下的测试用例
* pytest.main('-v', base_path + '/test_admin_login.py::TestAdminLogin::test_admin_login_success')  执行指定模块下指定用例类下的测试用例
* pytest.main('-vs', '-k', 'login', base_path) 执行指定目录下且文件名包含'login'的测试用例




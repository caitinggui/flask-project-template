## 如何选择工程模板
- 如果你的应用的组件之间的联系较为紧密，使用功能式架构会更好(functional-organization)
- 如果你的应用是由独立的，仅仅共享模型和配置的各组件组成，分区式将是个好选择(partition-organization)


## 注意事项
- online中的配置在修改之后切勿提交到版本库中
- flask首先会搜索app默认templates(默认在根目录的templates文件夹),找不到然后在blueprint的templates文件夹,但顺序不定，所以各个blueprint的模板文件名不能相同，如果不想使用blueprint的模板文件，可以在app默认templates建立模板文件覆盖

## 参考资料
- [1][Flask之旅](https://spacewander.github.io/explore-flask-zh/index.html)
- [1][欢迎进入Flask大型教程项目](http://www.pythondoc.com/flask-mega-tutorial)

class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert x in 'hello'
        # 如何编写pytest测试样例
        #
        # 通过上面2个实例，我们发现编写pytest测试样例非常简单，只需要按照下面的规则：
        #
        # 测试文件以test_开头（以_test结尾也可以）
        # 测试类以Test开头，并且不能带有
        # init
        # 方法
        # 测试函数以test_开头
        # 断言使用基本的assert即可

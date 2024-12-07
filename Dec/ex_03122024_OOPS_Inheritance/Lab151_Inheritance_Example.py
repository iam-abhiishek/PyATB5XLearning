class BaseTest:

    def start_browser(self):
        print("starting the browser")

    def stop_browser(self):
        print("stopping the browser")

class TestCase1(BaseTest):

    def test_positive(self):
        self.start_browser()
        print("test case P-1 executed")
        self.stop_browser()

    def test_negative(self):
        self.start_browser()
        print("test case N-1 executed")
        self.stop_browser()

class TestCase2(BaseTest):
    def test2(self):
            self.start_browser()
            print("test case 2 executed")
            self.stop_browser()


# baseTest_obj = BaseTest()
# baseTest_obj.start_browser()

testcase_obj = TestCase1()
testcase_obj.test_positive()
testcase_obj.test_negative()
print("-----------")
testcase_obj = TestCase2()
testcase_obj.test2()

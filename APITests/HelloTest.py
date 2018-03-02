import APITests.APITest

class HelloTest(APITests.APITest.APITest):
    def __init__(self):
        pass

    def Init(self):
        print("HelloTest: Init")
        #raise RuntimeError("Cannot create inch-vor ban")

    def Test(self):
        print("HelloTest: Test")

    def Validate(self):
        print("HelloTest: Validate")

    def Cleanup(self):
        print("HelloTest: Cleanup")

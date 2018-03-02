class TestInitException(BaseException):
    'Test init exception => Unresolved test'
    pass

class TestRunException(BaseException):
    'Test run exception => Failed test'
    pass

class TestValidateException(BaseException):
    'Test validation exception => Failed test'
    pass

class TestCleanupException(BaseException):
    'Test cleanup exception => Passed test'
    pass
    
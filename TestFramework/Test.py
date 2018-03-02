from abc import ABC, abstractmethod
import TestFramework.Exceptions

class BaseTest(ABC):
    'Base class for tests'

    def __init__(self):        
        #raise NotImplementedError      
        pass
    
    def Run(self):
        try:
            self.Init()
        except Exception as ex:
            raise TestFramework.Exceptions.TestInitException(ex)

        try:
            self.Test()
        except Exception as ex:
            raise TestFramework.Exceptions.TestRunException(ex)

        try:
            self.Validate()
        except Exception as ex:
            raise TestFramework.Exceptions.TestValidateException(ex)

        try:
            self.Cleanup()
        except Exception as ex:
            raise TestFramework.Exceptions.TestCleanupException(ex)

    
    @abstractmethod
    def Init(self):
        pass

    @abstractmethod
    def Test(self):
        pass

    @abstractmethod
    def Validate(self):
        pass

    @abstractmethod
    def Cleanup(self):
        pass
import pkgutil
import inspect
import sys
import traceback

from .Exceptions import TestInitException, TestRunException, TestValidateException, TestCleanupException
from .Test import BaseTest

class TestRunner:
    'Test execution framework'

    def __init__(self, package_name):
        self.PackageName = package_name

    def Run(self):
        print('Starting...')
        print('')

        numberOfTests = 0
        failsInInit = 0
        failsInRun = 0
        failsInValidation = 0
        failsInCleanup = 0
        unexpectedFails = 0

        for _, module_name, _ in pkgutil.iter_modules([self.PackageName]):
            module = __import__(self.PackageName + "." + module_name, fromlist=[''])
            for name,c in inspect.getmembers(module, lambda c : inspect.isclass(c) and not inspect.isabstract(c) and issubclass(c, BaseTest)):
                obj = c()
                numberOfTests += 1

                try:
                    print('')
                    print("---------------------------------------------------- Running Test : " + type(obj).__name__)
                    obj.Run()
                except TestInitException as ex:
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Init Issue")
                    failsInInit += 1
                    traceback.print_exc()

                except TestRunException as ex:
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Run Issue")
                    failsInRun += 1
                    traceback.print_exc()

                except TestValidateException as ex:
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Validate Issue")
                    failsInValidation += 1
                    traceback.print_exc()

                except TestCleanupException as ex:
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Cleanup Issue")
                    failsInCleanup += 1
                    traceback.print_exc()

                except Exception as ex:
                    unexpectedFails += 1
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Unexpected Issue")
                    traceback.print_exc()
                else:
                    print("Passed")

        print('')
        print('')
        print('')
        print("Number of tests = " + str(numberOfTests))
        print("Passed = " + str(numberOfTests - failsInInit - failsInRun - failsInValidation - failsInCleanup))
        print("Fails in Init = " + str(failsInInit))
        print("Fails in Run = " + str(failsInRun))
        print("Fails in Validation = " + str(failsInValidation))
        print("Fails in Cleanup = " + str(failsInCleanup))
        print("Unexpected fails = " + str(unexpectedFails))

        print('')
        print('TestCompleted')

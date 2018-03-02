import APITests.APITest

class GetJobList(APITests.APITest.APITest):
    def __init__(self):
        super().__init__("http://10.67.36.30:5000/api/")
        pass

    def Init(self):
        super().login("user", "passwd")
        self.api.add_resource(resource_name="jobs")
        
        
    def Test(self):
        self.response = self.sendGetRequest(self.api.jobs)

    def Validate(self):
        expectedCount = 3
        if (self.response == None):
            raise RuntimeError("Empty response")

        if ( len(self.response.body) != expectedCount):
            raise RuntimeError("Response size is different than " + str(expectedCount) + ": " + str(len(self.response.body)))
            
        print("HelloTest: Validate")

    def Cleanup(self):
        print("HelloTest: Cleanup")

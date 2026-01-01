import pytest

class ABC:
    def __init__(self):
        self.a=10
        self.b=20
    def get_data(self):
        return [self.a,self.b]
    def cleanup(self):
        return "Cleaning up...."

@pytest.fixture(scope="function")
def setup():
    obj=ABC()
    print("Setting up bro")
    yield obj
    print("Tearing down bro")
    obj.cleanup()


@pytest.fixture(scope="function")
def teardown():
    yield "Object deleted"


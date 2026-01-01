import pytest
@pytest.mark.parametrize("dummy",[None],ids=["001"])
def test_create_user(setup,dummy):
    assert setup.a==10
    assert setup.b==20

def test_modify_user(setup):
    setup.a=55
    setup.b=45
    assert setup.get_data()==[55,45]

def test_modify_user2(setup):
    setup.a=59
    setup.b=49
    assert setup.get_data()==[59,49]

def test_delete_user(teardown):
    assert "Object deleted"==teardown




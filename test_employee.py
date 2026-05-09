import pytest
from employee import Employee


@pytest.fixture
def employee():
    """一个可供所有测试使用的实例"""
    employee = Employee('junchao', 'zhang', 100_000)
    return employee


def test_give_default_raise(employee):
    """年薪能正确地增加默认值吗"""
    # employee = Employee('junchao', 'zhang', 100_000)
    employee.give_raise()
    assert employee.annual_salary == 105_000

def test_give_custom_raise(employee):
    """年薪能正确地增加自定义值吗"""
    # employee = Employee('junchao', 'zhang', 100_000)
    employee.give_raise(9000)
    assert employee.annual_salary == 109_000
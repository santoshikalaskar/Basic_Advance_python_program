import pytest

from employee_wage.EmployeeWageComputation import EmployeeWage


@pytest.fixture
def instance_of_main_class():
    employee_wage = EmployeeWage()
    return employee_wage


def test_employee_wage_company_name(instance_of_main_class):
    company = instance_of_main_class.add_company("reliance", 20, 100, 20)
    assert company.get_name() == "reliance"


def test_employee_wage_maximum_working_hours(instance_of_main_class):
    company = instance_of_main_class.add_company("bigbazar", 25, 75, 15)
    assert company.get_maximum_working_hours() == 75


def test_employee_wage_maximum_working_days(instance_of_main_class):
    company = instance_of_main_class.add_company("flipkart", 20, 60, 30)
    assert company.get_maximum_working_days() == 30


def test_employee_wage_per_hour(instance_of_main_class):
    company = instance_of_main_class.add_company("dMart", 15, 95, 25)
    assert company.get_wage_per_hour() == 15


def test_employee_check(instance_of_main_class):
    assert instance_of_main_class.employee_check(1) == 8


def test_given_company_list_should_calculate_total_employee_wage_for_each_company(instance_of_main_class):
    reliance = instance_of_main_class.add_company("reliance", 20, 100, 20)
    bigbazar = instance_of_main_class.add_company("bigbazar", 25, 75, 15)
    flipkart = instance_of_main_class.add_company("flipkart", 20, 60, 30)
    dMart = instance_of_main_class.add_company("dMart", 15, 95, 25)
    for _ in EmployeeWage.company_list:
        instance_of_main_class.compute_wage(_)
    assert instance_of_main_class.get_company(bigbazar) == EmployeeWage.company_dictionary.get("bigbazar")

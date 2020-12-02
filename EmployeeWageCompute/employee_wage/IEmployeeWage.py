from abc import ABC, abstractclassmethod, abstractmethod


class IEmployeeWage:

    #  abstract method for compute wage method is declared
    @abstractmethod
    def compute_wage(self, employee_wage_info):
        pass

    # abstract method for attendance check is declared
    @abstractmethod
    def employee_check(self, attendance):
        pass

    # abstract method for adding company is declared
    @abstractmethod
    def addCompany(self, name, employee_wage_per_hour, maximum_working_hour, maximum_working_days):
        pass

    # abstract method for returning respective company's total wage
    @abstractmethod
    def get_company(self, employee_wage_info):
        pass

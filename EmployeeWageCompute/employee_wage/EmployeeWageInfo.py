class EmployeeWageInfo:
    """
    Initialising private attributes of a company
    """
    __name = None
    __wage_per_hour = None
    __maximum_working_hours = None
    __maximum_working_days = None

    def __init__(self, name, wage_per_hour, maximum_working_hours, maximum_working_days):
        """
           Constructs all the necessary attributes for the employee object.

               Parameters:
                   name : string
                       name of the company
                   maximum_working_days : int
                       maximum working days a employee has to work in a month
                   maximum_working_hours : int
                       maximum working hours a employee has to work in a month
                   wage_per_hour
                       amount getting paid per hour for employee
           """
        self.__name = name
        self.__maximum_working_days = maximum_working_days
        self.__maximum_working_hours = maximum_working_hours
        self.__wage_per_hour = wage_per_hour

    def __str__(self):
        return "{} {} {} {} ".format(self.__name, self.__maximum_working_hours, self.__maximum_working_days,
                                     self.__wage_per_hour)

    def get_name(self):
        return self.__name

    def get_maximum_working_days(self):
        return self.__maximum_working_days

    def get_maximum_working_hours(self):
        return self.__maximum_working_hours

    def get_wage_per_hour(self):
        return self.__wage_per_hour

    def set_name(self, name):
        self.__name = name

    def set_maximum_working_days(self, maximum_working_days):
        self.__maximum_working_days = maximum_working_days

    def set_maximum_working_hours(self, maximum_working_hours):
        self.__maximum_working_hours = maximum_working_hours

    def set_wage_per_hour(self, wage_per_hour):
        self.__wage_per_hour = wage_per_hour


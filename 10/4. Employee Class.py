class Employee:
    def __init__(self, name, ident, dept, job_title):
        self.__name = name
        self.__ident = ident
        self.__dept = dept
        self.__job_title = job_title

    def set_name(self, name):
        self.__name = name

    def set_id(self, ident):
        self.__ident = ident

    def set_dept(self, dept):
        self.__dept = dept

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__ident

    def get_dept(self):
        return self.__dept

    def get_job_title(self):
        return self.__job_title


def main():
    emp1 = Employee('Susan Meyers', '47899\t', 'Accounting\t', 'Vice President')
    emp2 = Employee('Mark Jones\t', '39119\t', 'IT\t\t\t', 'Programmer')
    emp3 = Employee('Joy Rogers\t', '81774\t', 'Manufacturing', 'Engineer')
    print('Name\t\t\tID Number\tDepartment\t\tJob Title')
    print_empl(emp1)
    print_empl(emp2)
    print_empl(emp3)


def create_employee():
    nm = input('input name: ')
    i = input('input ID Number: ')
    dpt = input('input Department: ')
    jt = input('input Job Title: ')
    empl = Employee(nm, i, dpt, jt)
    return empl


def print_empl(empl):
    print(f'{empl.get_name()}\t'
          f'{empl.get_id()}\t'
          f'{empl.get_dept()}\t'
          f'{empl.get_job_title()}')


main()

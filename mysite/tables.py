from table import Table
from table.columns import Column
from mysite.models import Employee

class EmployeeTable(Table):
    user = Column(field = 'user', header='Name')
    emp_id = Column(field='emp_id', header='Emp Id')
    no_of_mentors = Column(field='no_of_mentors' , header='No. of Mentors')
    no_of_student = Column(field='no_of_student', header= 'No. of Students')
    
    class Meta:
        model = Employee

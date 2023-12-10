--List the manager of each department along with their department number, department name, employee number, last name, and first name.
select dept_manager.dept_num, departments.dept_name, dept_manager.emp_num, employees.last_name, employees.first_name
from dept_manager
inner join departments on dept_manager.dept_num=departments.dept_num
inner join employees on dept_manager.emp_num=employees.emp_num;
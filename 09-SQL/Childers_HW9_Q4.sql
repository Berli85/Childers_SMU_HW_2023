--List the department number for each employee along with that employee’s employee number, 
--last name, first name, and department name.
select dept_emp.dept_num, dept_emp.emp_num, employees.last_name, employees.first_name, departments.dept_name
from dept_emp
inner join departments on dept_emp.dept_num=departments.dept_num
inner join employees on dept_emp.emp_num=employees.emp_num;
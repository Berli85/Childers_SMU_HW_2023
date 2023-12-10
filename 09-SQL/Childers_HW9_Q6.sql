--List each employee in the Sales department,including their employee number, last name, and first name.
select departments.dept_name, dept_emp.dept_num, dept_emp.emp_num, employees.last_name, employees.first_name 
from dept_emp
inner join departments on dept_emp.dept_num=departments.dept_num
inner join employees on dept_emp.emp_num=employees.emp_num
where dept_name = 'Sales';
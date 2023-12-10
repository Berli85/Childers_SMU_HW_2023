--List the frequency counts, in descending order, 
--of all the employee last names (that is, how many employees share each last name).
select employees.last_name, count(last_name) as count
from employees
group by last_name
order by last_name desc;

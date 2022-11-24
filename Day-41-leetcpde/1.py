# My interview with Zoom
# every months:(last 2 years work data(partioned on yearmo))
#
# Source: FDP(Datawarehouse (GCS+Metastore))
# Transform:
# Sink:
#
#
# Data Validation Job(Wrapper on top of pydeequ)
#
#
# validation_of_source -> The actual_job(ETL) -> validation of ETL Output
# validation_of_source :
#     1. Metric: Min, max, stddev, null_count,
#     2. Validation: contstains


# employee_table
#     emp_id
#     salary
#
# project_table
#     project_id
#     emp_id
#     start_date
#     end_date
#
# 1:N
#
# # 1. Take the 5 lowest paid employees who have done atleast 10 projects
#
# emp_id, salary, project_id, end_date
#
# with finished_poject as(
#     SELECT emp_id, count(*) as project_count from project_table WHERE end_date IS NOT NULL AND count(*) >= 10
#     )
#     SELECT
#
#
# # 2. What is the SUM of salaries of employees that have not finished a project
#
# emp1: salary
# emp2: salary
#
# total_salary
#
# emp_id, salary
#
# with CTE as(
#     SELECT distinct(emp_id) from project_table WHERE end_date IS NULL)
#     SELECT sum(e.salary) from CTE  c INNER JOIN employee_table e ON emp_id;























-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/3MUafA
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "departments" (
    "dept_num" varchar(10)   NOT NULL,
    "dept_name" varchar(50)   NOT NULL,
    CONSTRAINT "pk_departments" PRIMARY KEY (
        "dept_num"
     )
);

CREATE TABLE "titles" (
    "title_id" varchar(10)   NOT NULL,
    "title" varchar(50)   NOT NULL,
    CONSTRAINT "pk_titles" PRIMARY KEY (
        "title_id"
     )
);

CREATE TABLE "employees" (
    "emp_num" integer   NOT NULL,
    "emp_title_id" varchar(10)   NOT NULL,
    "birth_date" date   NOT NULL,
    "first_name" varchar(100)   NOT NULL,
    "last_name" varchar(100)   NOT NULL,
    "sex" varchar(5)   NOT NULL,
    "hire_date" date   NOT NULL,
    CONSTRAINT "pk_employees" PRIMARY KEY (
        "emp_num"
     )
);

CREATE TABLE "salaries" (
    "emp_num" integer   NOT NULL,
    "salary" integer   NOT NULL,
    CONSTRAINT "pk_salaries" PRIMARY KEY (
        "emp_num"
     )
);

CREATE TABLE "dept_emp" (
    "emp_num" integer   NOT NULL,
    "dept_num" varchar(10)   NOT NULL,
    CONSTRAINT "pk_dept_emp" PRIMARY KEY (
        "emp_num","dept_num"
     )
);

CREATE TABLE "dept_manager" (
    "dept_num" varchar(10)   NOT NULL,
    "emp_num" integer   NOT NULL,
    CONSTRAINT "pk_dept_manager" PRIMARY KEY (
        "dept_num","emp_num"
     )
);

ALTER TABLE "employees" ADD CONSTRAINT "fk_employees_emp_title_id" FOREIGN KEY("emp_title_id")
REFERENCES "titles" ("title_id");

ALTER TABLE "salaries" ADD CONSTRAINT "fk_salaries_emp_num" FOREIGN KEY("emp_num")
REFERENCES "employees" ("emp_num");

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_emp_num" FOREIGN KEY("emp_num")
REFERENCES "employees" ("emp_num");

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_dept_num" FOREIGN KEY("dept_num")
REFERENCES "departments" ("dept_num");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_dept_num" FOREIGN KEY("dept_num")
REFERENCES "departments" ("dept_num");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_emp_num" FOREIGN KEY("emp_num")
REFERENCES "employees" ("emp_num");


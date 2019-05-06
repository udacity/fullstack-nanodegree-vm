# Overview
The attached Python script along with the dependent SQL views return the answers for Project 1 of the FSND.

Run three steps to execute the script. Each of those steps is broken down in more detail below.
1. Run the Vagrant virtual machine
2. Set up the SQL data base
3. Run the Python script

### 1. Run the Vagrant virtual machine
Spin up the virtual Vagrant machine: `vagrant up`.
Once the VM is running, log in via `vagrant ssh`.

The terminal should now indidcate that you're on the VM `vagrant@vagrant:`

### 2. Set up the SQL data base
For easier understanding, let's break this step further down into three sub-steps.

##### 2.1 Download the raw data
Download the `newsdata.zip` file from this [link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

Move the file into your `vagrant` folder.

##### 2.2 Load the data into your data base
`cd` into the `vagrant` folder and then execute the following command, which create the required tables and populate them with data:
`psql -d news -f newsdata.sql`

##### 2.3 Create SQL view
This view is required to answer Question 3. 

Run the following SQL command to create the view:
```sql
CREATE VIEW day_summary AS
SELECT l.time::date AS date_day,
count(*) AS total,
count(*) FILTER (WHERE l.status = '200 OK') AS num_success,
count(*) FILTER (WHERE l.status <> '200 OK') AS num_failure
FROM log as l`
GROUP BY l.time::date;
```

You have now create a new SQL view called `day_summary`, which the Python script depends on.

Don't forget to log out of the data base with `\q` before running the Python script.

### 3. Run the Python script
Here's where the actual fun starts. All 3 questions are answered in a single Python script. You run it with the following command:
`python logs_analysis.py`

This script executes three functions, which print out the answers for each of the questions respectively:
`answer_question_1()`
`answer_question_2()`
`answer_question_3()`

Woop woop. Onwards to Project 2!

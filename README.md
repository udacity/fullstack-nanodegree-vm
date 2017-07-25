# Log_Analysis_Project

### Project Description
Create a reporting tool that prints out reports (in plain text) based on the data in the news database. This reporting tool is a Python program using the psycopg2 module to connect to the news database. Reports details are as follows:

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. 

### How to Run?

#### PreRequisites:
  * [Python3](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)
  
#### Setup Project:
  1. Install Vagrant and VirtualBox
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/mdjolieca/fullstack-nanodegree-vm/tree/Log_Analysis_Project)     repository.
  
#### Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
  ```
    $ vagrant up
  ```
  2. Then Log into this using command:
  
  ```
    $ vagrant ssh
  ```
  3. Change directory to /vagrant/news and look around with ls.
  ```
    $ cd /vagrant/news
  ```
     all of the file related to this project are in this directory.
  
#### Setting up the database:

   1. Unzip the /vagrant/news/newsdata.zip  file.  
  
   2. Load the data into the news database using the newsdata.sql script from step 1 zip file:
  
  ``` 
    psql -d news -f newsdata.sql
  ```
   3. (Optional)Use `psql -d news` to connect to database and veiw the table structure.
      The database includes three tables:
        * The authors table includes information about the authors of articles.
        * The articles table includes the articles themselves.
        * The log table includes one entry for each time a user has accessed the site.
  
 
  #### Generate the reports:
  1. From the /vagrant/news directory inside the virtual machine, run::
  ```
    $ python3  newsreports.py
  ```
  results should be identical to the thoose the sampleReport file provided.
 
  
  ### Adding reports:
  Please see comments in the newreports.py file for instructions on adding new reports.

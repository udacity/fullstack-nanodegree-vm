fullstack-nanodegree-vm
=============

This is a project that analyzes the article, author and log table in a news database to extract relevant question.

Getting Started
=============

In other to get this program running, you will have to download this repository.

### Prerequisites

* The virtual machine
This project makes use of the same Linux-based virtual machine (VM).

If you don't have VM installed you can do so here [virtual machine](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1), you will also need to install vagrant [vagrant](https://www.vagrantup.com/). <br>
For a complete to installation on `vagrant` and `virtual machine` can be found [here](https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)

Clone this repo using this command `git clone URL`. After download is completed `cd folderName/vagrant` and then within vagrant directory type `vagrant up` and then `vagrant ssh`

![image](https://user-images.githubusercontent.com/15640112/52252280-de223280-2901-11e9-942b-92619ef8ef1a.png)

This will give you the PostgreSQL database and support software needed to run this project and connects you to the VM.

![image](https://user-images.githubusercontent.com/15640112/52252639-c77cdb00-2903-11e9-9355-45d5e6c7926c.png)

* Dowload and extract the newsdata.sql zipped file and save it in the vagrant directory which is shared with your virtual     machine.

 To load the data, `cd` into the `vagrant` directory  using `cd /vagrant` and use the command `psql -d news -f           newsdata.sql`.
 this will install a copy of the DB and grants you access to manipulate it.<br>
The command above is explained here:<br>
`psql` — the PostgreSQL command line program<br>
`-d news` — connect to the database named news which has been set up for you<br>
`-f newsdata.sql` — run the SQL statements in the file newsdata.sql<br><br>

* Connect tot the BD with `psql -d news` command and copy and paste all the views from the createView.txt file 

![screenshot from 2019-02-05 05-24-45](https://user-images.githubusercontent.com/15640112/52253236-f2b4f980-2906-11e9-96c6-7ac14ab6baf0.png)

* This should be done in order e.g ` create view percentageerror as ....` followed by `create view badreport as select` and so on.

* After this is done, you can either open another command line and navigate to `cd /vagrant` or you exit from DB with `\q` and then `enter` and from VM `exit`

* Run the news.py file with `python news.py`

* View the results by going to the r espective URL<br>
— `localhost:8000/populararticles` <br>
— `localhost:8000/popularauthors` <br>
— `localhost:8000/highesterror` <br>
— `localhost:8000/allerror` <br>

![articles](https://user-images.githubusercontent.com/15640112/52273183-5fe97e80-2949-11e9-844d-7467cf3c1088.png)<br>


![authors](https://user-images.githubusercontent.com/15640112/52273080-fb2e2400-2948-11e9-9f10-f9875488dd52.png)<br>


![error](https://user-images.githubusercontent.com/15640112/52273126-231d8780-2949-11e9-8fd1-8b546db0e619.png)<br>


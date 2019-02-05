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
`-f newsdata.sql` — run the SQL statements in the file newsdata.sql<br>

* Run all the views 
![screenshot from 2019-02-05 05-24-45](https://user-images.githubusercontent.com/15640112/52253236-f2b4f980-2906-11e9-96c6-7ac14ab6baf0.png)


```
Give examples
```
### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [vagrant](https://www.vagrantup.com/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc


# Item Catalog

### Project Overview
To Develop an application that provides a list of items within a variety of categories as well as to provide a user registration and authentication system ( like gmail) . Registered users will have the ability to post, edit and delete their own items.

### What Will I Learn?
  * Develop a RESTful web application using the Python framework Flask
  * Implementing CRUD (create, read, update and delete) operations.
  * Implementing third-party OAuth authentication.
  * JSON Endpoints.
  
### How to Run?

#### PreRequisites
  * [Python ~2.7](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)
  
#### Setup Project:
  1. Install Vagrant and VirtualBox
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Find the catalog folder and replace it with the the catalog folder of the zipped file.
 
#### Launch Project
  1. Launch the Vagrant VM using command:
  
  ```
    $ vagrant up
  ```

  2. Login into the VM using command:
  
  ```
    $ vagrant ssh
  ```

  3. Run your application within the VM
  
  ```
    $ python /vagrant/catalog/dbp.py
  ```

  4. Access and test your application by visiting (http://localhost:5000).

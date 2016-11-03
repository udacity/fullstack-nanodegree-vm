# Udacity FSND tournament assignment
---
This is a python program that has functionality for a basic swiss-pariing style tournament using a PostGreSQL database. 
The project is as described in this [document](https://docs.google.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true)

### Functionalities
Users can be created which can create posts, comment on posts and like posts from other users.
Posts and comments can also be edited and deleted.


---

### Requirements for local deployment ###

* Vagrant
* VirtualBox
* GitBash

---

### Quickstart (for local app) ###

1. Clone or download this repository from https://github.com/Kaisaurus/p03-blog
2. Install GitBash, [Vagrant](http://vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
3. Open GitBash
4. Launch the Vagrant VM in the cloned folder with its containing settings by typing:
    - ``` $ cd ../fullstack-nanodegree-vm/vagrant ```
    - ``` $ vagrant up ```
    - ``` $ vagrant ssh ``` (this should connect you to the VM)
    - ``` $ cd /vagrant/tournament ```
    - ``` $ python tournament_test.py ```
   
---

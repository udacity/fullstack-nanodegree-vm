Gamerater
=========

A website for rating video games.

# Installation:

* Install Virtual Box and Vagrant.
* Clone this repository.
* Run `vagrant up` from /vagrant
* Once the VM has been created, run `vagrant ssh` from /vagrant
* Navigate back to the catalog folder in the VM (by default use `cd /vagrant/catalog`)
* Run the server (i.e. `python gamerater.py`)
* Open your browser to http://localhost:8000/gamerater/
* ????
* Profit

### Files Included:

> fullstack-nanodegree-vm
>   |
>   catalog
>     |
>     |- README.md
>     |- client_secrets.json
>     |- database_setup.py
>     |- fb_client_secrets.json
>     |- gamerater.py
>     |- static
>     |    |- bootstrap.min.css
>     |    |- bootstrap-theme.min.css
>     |    |- main.css
>     |    |- img
>     |        |- logo.png
>     |        |- zero.png
>     |- templates
>          |- add_game.html
>          |- all_base.html
>          |- delete_rating.html
>          |- game.html
>          |- game_details.html
>          |- home.html
>          |- login.html
>          |- messages.html
>          |- my_games.html
>          |- rate_game.html
>          |- update_user.html
>          |- user.html
>          |- user_small.html 

### Authors:
Paul Castillo

Udacity, for the vagrant vm
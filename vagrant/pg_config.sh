apt-get -qqy update
apt-get -qqy install postgresql python-psycopg2
apt-get -qqy install python-flask python-sqlalchemy
apt-get -qqy install python-pip
pip install bleach
pip install oauth2client
pip install requests
pip install httplib2
su postgres -c 'createuser -dRS vagrant'
su vagrant -c 'createdb'
su vagrant -c 'createdb forum'
su vagrant -c 'psql forum -f /vagrant/forum/forum.sql'

alertAlreadyAdded=$(grep -c "vagrantTip.txt" /home/vagrant/.bashrc)
if [ $alertAlreadyAdded -eq 0 ]
then
    echo -e "\n# Print instructions to access vagrant shared directory\ncat /vagrant/.vagrantTip.txt\n" >> /home/vagrant/.bashrc
    echo "Shared folder alert added to .bashrc"
else
    echo "Shared folder alert already present"
fi


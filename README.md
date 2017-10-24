# README v0.1.0 #

This README documents what steps are necessary to get the **EnergyCoin BlockExplorer** up and running. It's tested and working on **Ubuntu 16.04.1 LTS**.
The average time for the setup is about 30 minutes if there are no errors. If there are errors the average setup time is *forever*.

## Prerequisites (~10min)##

Do the following:

* Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* Enable virtualization in your BIOS settings
* Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* Install [Vagrant](https://www.vagrantup.com/docs/installation/)
* **If you're using Windows** install [cmder](http://cmder.net/)
* Relax

## Starting the virtual machine for the first time ##

### Prerequisites ###
In order to start your machine you have to clone the repository with the hot storage and download the virtual machine image file from the vagrantcloud repository.

* Clone this repository, let's say it's cloned inside a folder called: `energycoinblockexplorer`

* Navigate inside the `env` directory thats inside the directory you just cloned: `cd energycoinblockexplorer/env`

* Boot up the vagrant machine: `vagrant up`

* Login into the vagrant machine: `vagrant ssh`

* Install pip: `sudo apt-get install python-pip`

* Install ansible: `sudo pip install -I ansible==2.3.0`

* Run ansible configuration: `ansible-playbook /energyexploder/env/configure-vagrant.yml`


# FAQ #

### Unsupported locale settings ###

If you get the unsupported locale settings error while trying to install pip, follow the next commands:

* `export LC_ALL="en_US.UTF-8"`
* `export LC_CTYPE="en_US.UTF-8"`
* `sudo dpkg-reconfigure locales` - Just press Enter button twice


### Failed to mount folders in Linux guest. This is usually because the "vboxsf" file system is not available ###

Type this in the directory where you have initialized your Vagrant machine

* `vagrant plugin install vagrant-vbguest`
* `vagrant halt`
* `vagrant up`
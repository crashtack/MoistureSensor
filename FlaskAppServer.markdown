# Pi Setup continued
## Git Setup
https://kbroman.org/github_tutorial/pages/first_time.html

set git globals
```
$ git config --global user.name "Your name here"
$ git config --global user.email "your_email@example.com"
$ git config --global color.ui true
$ git config --global core.editor emacs <vim>
```

Add ssh pub key to github
```
$ ssh-keygen -t rsa -C "your_email@example.com"
```
copy id_rsa.pub to new key on GitHub account
```
cat ~/.ssh/id_rsa.pub
```

Git Commands
$ git status
$ git remote
$ git checkout -b new-branch-name

*Git Flow*
Make a change:
$ git add <changed file>
$ git commit
$ git push


# Run Flask App Server on Raspberry Pi
## Setup virtualenv
Install python virtualenv
https://docs.python-guide.org/dev/virtualenvs/
```
$ pip3 install --user pipenv
$ source ~/.profile           # I don't know why i had to run this command to use virtualenvs and pipenv
$ cd project_folder (~/Projects/DataVis)
$ pipenv install requests
$ pip3 install virtualenv
```
to create a virtualenv
```
$ cd to project_folder
$ virtualenv venv #creates the venv dir in the project dir
$ source venv/bin/activate    # Activates the virtual environment
```

to install package in venv
```
$ pip install <package>
```

to deactivate venv
```
$ deactivate
```

to remove a venv
```
$ rm -rf venv
```

## Create Project folder and initialize git
```
$ git clone https://github.com/crashtack/MoistureSensor.git
$ cd MoistureSensor
$ virtualenv venv
$ source venv/bin/activate
```

## NGINX
https://www.raspberrypi.org/documentation/remote-access/web-server/nginx.md
```
$ sudo apt-get update
$ sudo apt-get install nginx
$ sudo /etc/init.d/nginx start
$ hostname -I     # what's my ip
```

## uWSGI
https://hackersandslackers.com/deploy-flask-uwsgi-nginx/
```
$ sudo apt update
$ sudo apt upgrade -y
$ sudo apt upgrade -y --fix-missing
$ sudo apt install python3.8 python3.8-dev python3-distutils uwsgi uwsgi-src uuid-dev libcap-dev libpcre3-dev python3-pip python3.8-venv
*This command failed for me*
$ sudo apt install python3-distutils uwsgi uwsgi-src uuid-dev libcap-dev libpcre3-dev python3-pip
$ sudo apt-get install uwsgi-plugin-python3
$ sudo apt-get install ufw
$ sudo ufw allow 5000

$ cd ~/Projects/MoistureSensor
$ source venv/bin/activate
```

## *Install Python 3.8*
https://installvirtual.com/how-to-install-python-3-8-on-raspberry-pi-raspbian/
```
$ sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev tar wget vim
$ wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
$ sudo tar zxf Python-3.8.0.tgz
$ sudo ./configure --enable-optimizations
$ sudo make -j 4
$ sudo make altinstall
$ python3.8 --version
```

GO Install Flask


## Flask
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
```
$ pip install flask
$ flask run --host=0.0.0.0    # make flask externally visable ip:5000
```
create files

Back to uWSGI instal tutorial
```
$ python3.8 -m venv myenv
$ source myenv/bin/activate
$ python3 -m pip install -r requirements.txt  # If you have an app already built
```

## Dash
Following this: https://dash.plotly.com/layout
```
$ pip install dash==1.11.0
```

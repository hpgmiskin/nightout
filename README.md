#nightout

NightOut is the shell of a web application designed during a Hackathon. Over weekend I designed the front end web application while other members of the group worked on the mobile app and the back end. This is written using Django web framework to provide the interface for both the prospective business and personal customers.

##Aims

* Provide users with an easy interface to browse events in the area
* Give mobile app users the ability to record where they had been on a night out
* Provide business customers with a location based advertising platform
* Deliver tailored offers to users when they are in the vicinity of a location


##To Run

To run this application its best to use a virtual environment. The requirements of the files that should be installed in the virtual environment can be found in `requirements.txt`. The process I suggest for this is as follows.

- Install Python3 *- Python 3.4 comes with pip as standard*

- Install virtualenv by typing the following into the terminal

```
$ pip3 install vitualenv
```

- Navigate to the local directory containing this repository in terminal

```
$ cd FOLDER_PATH
```

- Create a new virtual environment in this directory

```
$ virtualenv -p python3 venv
```

- Activate the virtual environment

```
$ source venv/bin/activate
```

- Install requirements using pip3

```
$ pip3 install -r requirements.txt --allow-all-external
```

- Run the server

```
$ python3 manage.py runserver
```

- Open you internet browser and navigate to

```
localhost:8000
```

- To end the server press `Ctrl + C` in the terminal window 

##Licence

Please feel free to use any code contained within the repository for non commercial purposes however I request that credit is given to myself for any direct copying.
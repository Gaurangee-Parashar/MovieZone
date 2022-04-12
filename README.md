# MovieZone

# Snapshots
<img width="500px" src="snapshots/1.png"/>
<img width="500px" src="snapshots/2.png"/>
<img width="500px" src="snapshots/3.png"/>
<img width="500px" src="snapshots/4.png"/>
<img width="500px" src="snapshots/5.png"/>
<img width="500px" src="snapshots/6.png"/>
<img width="500px" src="snapshots/7.png"/>
<img width="500px" src="snapshots/8.png"/>
<img width="500px" src="snapshots/9.png"/>

# Build Instructions

### Clone the project

`git clone --recursive https://github.com/Gaurangee-Parashar/MovieZone.git` <br>
`cd MovieZone`

### Create a new virtual env inside the cloned repository

`virtualenv env`

<p>(Make sure to have the virtual env module installed through pip)</p>

### Installing the required dependencies

`pip install -r requirements.txt`

### Migrating the sqlite3 database tables

`python manage.py makemigrations`<br>
`python manage.py migrate`

### Running the django development server

`python manage.py runserver`


![alt text](https://github.com/elizabethlarkinnelson/FindIt/blob/master/FindItPhotos/FindIt2.jpg)

# FindIt is easy to get up and running! 

1. In the terminal run:
``` 
$ git clone https://github.com/elizabethlarkinnelson/FindIt.git
```
2. Navigate into project.
```
$ cd FindIt
```
3. Install virtualenv (if you don't already have it!). You'll need pip too (instructions for installing pip [here](https://pip.pypa.io/en/stable/installing/)).
```
$ pip install --user virtualenv
```
4. Create virtual environment
```
$ virtualenv env
```
5. Activate virtual enviroment 

MAC:
```
$ source env/bin/activate
```
WINDOWS:
```
$ source env/Scripts/activate
```
6. Yay, you're in your virtual enviroment! Last set up part: pip install requirements.txt.
```
$ pip install -r requirements.txt
```
7. Navigate into the findit django project one directory down and start the server (path is *Findit/findit*).
```
$ cd findit
$ python manage.py runserver
```
8. This project is built for Python3 so be careful with that last command if Python2 is your computer's default.
9. Navigate to http://127.0.0.1:8000/jobs/ to see all the amazing jobs at your fingertips!


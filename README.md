# ****Airbnb Clone****

This project challenged us to Create our own Airbnb Console

### Description of Airbnb Clone
* This Is A clone of Airbnb<br/>
* in this repository you can find A command interpreter and classes and methods<br/>
exemple class(BaseModel) and methods(State, City, Place, Review ...)<br/>
* The Console is command interpreter like the Shell project in C<br/>
* Currently, the project simply implements the back-end console<br/>
### This is the supported commands in Airbnb Clone<br/>




### How to use our Airbnb clone:<br/>
```
root@user:/AirBnB_clone$ ./console.py
(hbnb)help

Documented commands (type help <topic>):

========================================
EOF  help  quit

(hbnb)
(hbnb) help quit
Quit command to exit the program

(hbnb)
(hbnb) help EOF
Quit command to exit the program
(hbnb)
(hbnb) quit
root@user:/AirBnB_clone$
```

```
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
*["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293)...
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
*[BaseModel] (49faff9a-6318-451f-87b6-910505c55907)...
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
*["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9'...
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb)
```

### Known bugs :

No bugs know. if there is a bug you can contact us in email.



### Authors

* Rayen Hedri - https://github.com/rayenhdr93

* Aymen Ben Slima - https://github.com/Aymenbs22


###### Project made for Holberton school by Rayen Hedri and Aymen Ben Slima.

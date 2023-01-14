# UWEFlix

Click on the following to the each sub-header:-  
[How to Run](#how-to-run)<br />
[CRUD Operators](#crud-operators)<br />

## How to Run
1) Make sure the project is opened as directory in VSCode terminal
if you downloaded the .zip folder it should be in :-
```
../foonyeecust
```

2) Run this line in the VSCode terminal to build image based from the Dockerfile
```
docker build -t desdcustomerslim:1.0 .
``` 

3) Run this line to start/run the container
```
docker run -p 8000:8000 desdcustomerslim:1.0
```

4) copy and paste the below to the web browser
```
127.0.0.1:8000
```
This is how it will look on a web brower:-
![foonyeecust](images/foonyeecust.png)

## CRUD Operators
The term "CRUD" refers to the four operations that are thought to be required to develop a persistent storage application: creation, read, update, and delete. It originates from the area of computer programming. Any data storage device, such as a solid-state drive or a hard disc, that keeps power after the device is turned off is referred to as persistent storage.

The CRUD acronym identifies all of the major functions that are inherent to relational databases and the applications used to manage them.


![sc](images/sc.png)

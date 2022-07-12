# she-codes-crowdfunding-api-project-neets1981
she-codes-crowdfunding-api-project-neets1981 created by GitHub Classroom

1.	Git hub link : 
https://github.com/SheCodesAus/she-codes-crowdfunding-api-project-neets1981

2.	Heroku link : https://dashboard.heroku.com/apps/tranquil-ravine-60150

3.	GET post: Access all projects.

 


4.	Post : Create new project 
 




5.	PUT : Update project
 

6.	DELETE : Delete project 

 








7.	Login token  Returned


 


8.	Register new user : 

•	Post method  
•	Enter url ; http://localhost:8000/users/
•	Enter body as 
          {"username": "jpatankar ",
           "email": "asp@test.com.au",
           "password": "neeta2022"}
•	Click on ‘Send’ shows endpoint : 201 created
•	view Token in Preview as per attached screenshot 
 



















Create a new project

•	Post method – 
•	Enter url ; http://localhost:8000/projects/
•	Enter body as 
{ "title": "she code6",
	"description": "proj 6",
	"goal":300,
	"image": "https://via.placeholder.com/300.jpg",
"is_open": true,
	"date_created": "2020-03-20T14:28:23.382748Z"}            
•	Click on ‘Send’ shows endpoint : 201 created
•	 view project created in Preview as per attached screenshot 




 












9.	An API specification.
GET
POST
PUT
DELETE 



HTTP method	URL	Purpose	Req Body	Successful Response Code	Authentication
GET	/projects/	Returns all projects	N/A	200	N/A
POST	/projects/	Create a new project	Project object	201	Must be logged in
GET	/projects/id/	Returns the project with ID	N/A	200	N/A
PUT	/projects/id/	Updates the project with ID	Project object	200	Must be logged in
Must be project owner
DELETE	/projects/id/	Deletes the project with ID	Project object	204	Must be logged in
Must be project owner
					
POST	/pledges/	Create a new pledge	Pledge object	201	Must be logged in

GET	/pledges	Returns all projects	N/A	200	Must be logged in

GET	/pledges/id/	Get the pledge with ID	N/A	200	Must be logged in

DELETE	/pledges/id/	Deletes the pledge with ID	N/A	204	Must be logged in
Must be pledge owner
GET	/users/	Returns all user	N/A	200	N/A
POST	/users/	Create new user	User object	201	N/A
GET	/users/id	Returns the user with ID	N/A	200	N/A
PUT	/user/id/	Updates the user with ID	User object	200	Must be logged in and own user
DELETE	/user/id/	Deletes the user with ID	N/A	204	Must be logged in and own user


















10.	Database Schema


Project: 

Id	Integer
Description	string
Image	string
title	string
goal	integer
Is_open	Boolean
Date created	Date time
Owner 	string


Pledge: 
Id	Integer
Amount	Integer
Project	Integer
user	Integer
Comment	String
Anonymous	Boolean


User: 
id	Integer
Username 	String
Password	String
Email	String

![image](https://user-images.githubusercontent.com/29352007/178422832-b383eed3-bc9b-44c1-950d-4a03d031b06f.png)

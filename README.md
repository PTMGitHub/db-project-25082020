# Git Repo: 
git@github.com:PTMGitHub/db-project-25082020.git

# Task
Create an API that has POST and GET methods. Use a relational database for persistence.

Suggested minimal architecture:

- Docker compose containing a flask api and postgres.

Tips:

- Investigate mounting the storage for your database solution so that you don’t lose your data if you lose the docker container.

Suggested Options / Extensions:
- Nginx reverse proxy/ load balancer
- Host in AWS
- Create a frontend web application that uses your api
- Learn how to use mocking to test the api code that interacts with the db

Resources:
- https://wiki.postgresql.org/wiki/Python
- https://hub.docker.com/_/postgres
- https://opensource.com/article/18/4/flask

***

## Project idea: 
DB - Movie Diary.

Need 
- DB - 
	- MySQl
	- id
	- movie name
	- year
	- rating

- Front end
	- Landing
		- input for movie to rate
		- list of rated movie
	- post 
		- posts the info inpute info into the 
	- get 
-

***

## Log

- 4th Sept 
    - has 3 contianers nginx, flask and postgres container. 
    - A db table is created (movies) and one row of data is inputted during dockert-compose up
    - goint to localhost brings up a html page which lists the movie names from the DB
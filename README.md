



# Employee Survey System 


  - [Features](#features)
  - [Demos](#demos)
  - [Run-App](#run-app)

## Features
##### **The system has three data objects:**
- Question
- Answers 
- Survey --> list of rating questions - has three types (general, followers, reversed) - has start date - has an end date 

---
##### views (implemented as a restful API and template view):
1.  **Employee tree view**  -> *set up by the admin*     Every employee can have a parent employee that they report to as the above fig 
    ![Untitled Diagram drawio (1)](https://user-images.githubusercontent.com/30774866/187946789-b02f8be0-4a84-424b-89bd-6b33170aaa99.png)
	
2. **survey view** 

    1. view for due surveys [list]
    2. View for submitted surveys [list]
    3. View for fetching a single survey question [detail]
    4. view for submitting the answer for the survey  [POST - Form]
    5. Employee real-time chatting system using WebSockets 
---



## Demos

### Reconstruction Demo 
![volume](./docs/1.jpeg) 
![volume](./docs/2.jpeg) 
![volume](./docs/3.jpeg) 
![volume](./docs/4.jpeg)


## Run-App
1. **_install project dependencies_**
```sh
pip install -r requirements.txt
```
2. **_Run the application_**
```sh
docker compose up



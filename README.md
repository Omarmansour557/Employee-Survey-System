# Intern Final Project: Employee Survey System 

###### Start Date:
###### Milestone one date: 
###### Milestone two date: 
###### End Date:

---
##### **system actors:**

- **Admin** 
- **Employee (Name - JobTitle - department  ) ( Allow self-register)**


---
##### **The system has three data objects:**
- question
- Answers 
- survey --> list of rating questions - has three types (general, followers, reversed) - has start date - has an end date 

---
##### views (needed to be implemented as a restful API and template view):---
1.  **employee tree view**  -> *set up by the admin*
    Every employee can have a parent employee that they report to 
	
2. **survey view** 

    1. view for due surveys [list]
    2. View for submitted surveys [list]
    3. View for fetching a single survey question [detail]
    4. view for submitting the answer for the survey  [POST - Form]
---
##### **Admin flow**

1.  Admin only can create (question, surveys)
2.  Admin can lunch survey for three different channel 
	- general --> means that all the system users besides the Admins will get that survey 
	- followers --> mean that all the parents will get a survey on every child in their tree (for example a senior software engineer reviewing his team juniors engineer  )
	- reversed --> means all the children will receive a survey on the parent employee
---
##### bonus points:

- Admin can lunch a survey for certain job titles or department
- Employee real-time chatting system using WebSockets 

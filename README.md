# lylab-test

Lylab Credit Evaluator

This App/Project allows a financial institution Credit Evaluator employee to Approve or
Deny Client's Credits.

Credits inside the DB must be below $50,000 in order to be handled by the employee.

The current Credit model structure is:

```
 id | client_id |  amount  | sbs_debt  | ai_index | sentinel_index | status
----+-----------+----------+-----------+----------+----------------+---------
  1 |         1 | 20000.00 | 200000.00 |        2 | BAD            | CREATED

Where:
-amount < 50,000
-sbs_debt is an amount that comes from the national regulator's database
-ai_index is an AI index from our internal Algorithm [1-10]
-sentinel_index comes from the Sentinel Risk Center which can be GOOD, REGULAR or BAD.

Also Client model:

 id | name | gender |  birthday
----+------+--------+------------
  1 | Fran | M      | 2021-09-11

```

# Instructions to Run

`The BackEnd was created with Django and PostgreSQL. In order to Run this project's backEnd you have to:`

```
-Create a virtual env
-Run venv/Scripts => activate inside the terminal
-Navigate to where the file "manage.py" is located
-exec pip install -r requeriments.txt
-exec pip install psycopg2
-exec python manage.py runserver
-If there's no database called 'clients' inside pgAdmin, create One.
-http://localhost:8000/credits/
-EndPoints are:
    * / (getAll)
    * /:id/approve
    * /:id/deny
    * /:id (delete method)

    * /clients (get all clients)
- you can use http://localhost:8000/credits/ and http://localhost:8000/credits/clients
 to administrate the data or just use pgAdmin.
```

`The FrontEnd was created with Angular. In order to Run this project's FrontEnd you have to:`

```
-npm install -g @angular/cli
-Navigate to where the "package.json" is inside "ui" folder
-exec ng serve
-use http://localhost:4200/ in your browser
```

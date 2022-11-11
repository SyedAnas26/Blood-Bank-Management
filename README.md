# Blood-Bank-Management - Tkinter

### Application Screenshots:

![Login Page](/output-screenshots/login.jpg?raw=true "Login Page")

![Hospital Dashboard](/output-screenshots/hosp_dash.jpg?raw=true "Hospital Dashboard")

![Querying Donors](/output-screenshots/query.jpg?raw=true "Querying Donors")

### Setting up:

Database:
  * Create a database in MySQL named ``` blood_bank ``` 
  * Set up your root password in the main.py file
  * Create donors and hospital tables in the Database
  ```
    create table donors
  (
      id            int auto_increment
          primary key,
      first_name    varchar(50)  not null,
      last_name     varchar(50)  not null,
      age           int          not null,
      gender        varchar(50)  not null,
      mobile_number varchar(50)  null,
      city          varchar(50)  not null,
      address       varchar(100) not null,
      user_name     varchar(50)  not null,
      password      varchar(50)  not null,
      blood_group   varchar(50)  not null,
      constraint user_name
          unique (user_name),
      constraint user_name_2
          unique (user_name)
  );
  
  create table hospital
  (
      id             int auto_increment
          primary key,
      hosp_name      varchar(100) not null,
      contact_number varchar(50)  not null,
      city           varchar(50)  not null,
      address        varchar(100) not null,
      user_name      varchar(50)  not null,
      password       varchar(50)  not null
  );
  
  ```

<br/>
  
  
Running the Script:   

* Clone the repository using git clone https://github.com/SyedAnas26/Blood-Bank-Management.git
* Make sure you have installed python3, tkinter, mysql connector
* Run the main.py file using python ``` python main.py ```



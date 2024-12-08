# Terminal management system

This project is a RESTful application designed for managing terminal cooperatives and their associated operations, such as vehicle management, travel planning, and ticket reservations.

## Features

- **Cooperative Management**: Add and manage cooperatives with their details, including vehicles and staff.
- **Vehicle Management**: Register vehicles for each cooperative, including details such as license plate, capacity, color, and model.
- **Travel Management**: Schedule and manage travels, specifying departure and return times, ticket prices, and seating capacity.
- **Reservation System**: Allow users to book tickets for scheduled travels.
- **Cancellation System**: Handle ticket cancellations and returned amounts.
- **User and Group Management**: Manage users, permissions, and groups to control access to different parts of the system.

---


## Installation

- 1- Clone the repository: <br><br>
     ```bash
       git clone https://github.com/Aliasghar-Salimi/django-vue-terminal-ticket-system.git
       cd django-vue-terminal-ticket-system

- 2- Setup a virtual environment and install dependencies: <br><br>
    ```bash 
        python3 -m venv venv
        source venv/bin/activate
        cd terminal-ticket-system-backend/core
        pip install -r requirements.txt
  

- 3- Applay migrations and create a superuser (using phone and password): <br><br>
    ```bash  
        python3 manage.py migrate
        python3 manage.py createsuperuser

- 4- Run the development server:
  ```bash
      python3 manage.py runserver
  

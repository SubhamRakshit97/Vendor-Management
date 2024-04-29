# Vendor Management API

This is a Django project that provides API endpoints for managing vendors and purchase orders.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/your_username/vendor-management-api.git
   ```
2. Follow this to navigate to project directory and run the code:
    ```
    cd backend
    python -m venv env
    (For Mac) source env/bin/activate
    (For Windows) env/Scripts\activate
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
3. The API should now be accessible at http://127.0.0.1:8000/

## Testing
   To run the test suite:

   1. Make sure you are in the project directory and the virtual environment is activated.
   2. Run the following command:
   ```
    python manage.py test
   ```
## API Endpoints
   ### Vendors
  
 #### List / Create Vendors
   1. Endpoint: `/api/vendors/`
   2. Methods: GET, POST
   3. Description: Retrieve a list of all vendors or create a new vendor.
      
 #### Retrieve / Update / Delete Vendor
   1. Endpoint: `/api/vendors/<int:pk>/`
   2. Methods: GET, PUT, PATCH, DELETE
   3. Description: Retrieve, update, or delete a specific vendor by its primary key.

 #### Vendor Performance
 1. Endpoint: `/api/vendors/<int:pk>/performance/`
 2. Methods: GET
 3. Description: Retrieve the performance metrics of a specific vendor.

  ### Purchase Orders
   #### List / Create Purchase Orders
   1. Endpoint: `/api/purchase_orders/`
   2. Methods: GET, POST
   3. Description: Retrieve a list of all purchase orders or create a new purchase order.

  #### Retrieve / Update / Delete Purchase Order
   1. Endpoint: `/api/purchase_orders/<int:pk>/`
   2. Methods: GET, PUT, PATCH, DELETE
   3. Description: Retrieve, update, or delete a specific purchase order by its primary key.



This README file should provide clear instructions for setting up the project, running the test suite, and using the API endpoints.

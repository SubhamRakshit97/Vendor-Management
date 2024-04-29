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
  
  1. Create Vendor
  2. URL: `/api/vendors/`
  3. Method: POST
  4. Request Body:
  ``` 
  {
      "name": "Vendor Name",
      "contact_details": "Contact details",
      "address": "Vendor Address",
      "vendor_code": "1234"
  }
  ```
 5. Response:
    1. Status Code: 201 (Created)
    2. Body:
    ```
    {
    "id": 1,
    "name": "Vendor Name",
    "contact_details": "Contact details",
    "address": "Vendor Address",
    "vendor_code": "1234",
    "on_time_delivery_rate": 0,
    "quality_rating_avg": null,
    "average_response_time": 0,
    "fulfillment_rate": 0
    }
    ```
6. Retrieve, Update, Delete Vendor
   1. URL: /api/vendors/<vendor_id>/
   2. Methods: GET, PUT, PATCH, DELETE
      
  ### Purchase Orders
  1. Create Purchase Order
  2. URL: `/api/purchase_orders/`
  3. Method: POST
  4. Request Body:
  ```
    {
    "po_number": "PO123",
    "vendor": 1,
    "order_date": "2024-04-30T10:00:00Z",
    "delivery_date": "2024-05-10T10:00:00Z",
    "items": ["item1", "item2"],
    "quantity": 10,
    "status": "pending",
    "issue_date": "2024-04-30T10:00:00Z"
    }
 ```
 5. Response:
    1. Status Code: 201 (Created)
    2. Body:
  ```
    {
    "id": 1,
    "po_number": "PO123",
    "vendor": 1,
    "order_date": "2024-04-30T10:00:00Z",
    "delivery_date": "2024-05-10T10:00:00Z",
    "items": ["item1", "item2"],
    "quantity": 10,
    "status": "pending",
    "issue_date": "2024-04-30T10:00:00Z",
    "acknowledgment_date": null,
    "quality_rating": null
    }
```
6. Retrieve, Update, Delete Purchase Order
   1. URL: `/api/purchase_orders/<purchase_order_id>/`
   2. Methods: GET, PUT, PATCH, DELETE



This README file should provide clear instructions for setting up the project, running the test suite, and using the API endpoints.

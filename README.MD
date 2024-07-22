# ATM API

## Overview
This is a simple ATM-like application built with Flask that provides RESTful endpoints for account management and transactions (deposit and withdraw). The application also includes Swagger UI for API documentation.

## Setup

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd atm_app
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python app.py
    ```

5. Open your browser and navigate to `http://127.0.0.1:5000/api/docs` to view the API documentation.

## Endpoints

- **GET /account/{account_id}**: Get account details.
- **POST /account/{account_id}**: Create a new account.
- **DELETE /account/{account_id}**: Delete an account.
- **POST /account/{account_id}/deposit**: Deposit amount to account.
- **POST /account/{account_id}/withdraw**: Withdraw amount from account.

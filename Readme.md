# FastAPI Project

This is a simple FastAPI project with a basic API and tests.

## Setup

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd fastapi_project
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv env
    source env/bin/activate

    OR for PowerShell

    .\env\Scripts\Activate.ps1
    (use https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.4 in case of execution failure)
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    uvicorn app.main:app --reload
    ```

5. Run the tests:

    ```bash
    pytest
    ```

## Docker

1. Build the Docker image:

    ```bash
    docker build -t fastapi-project .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 80:80 fastapi-project
    ```

## Endpoints

- `GET /` - Returns a welcome message
- `GET /items/{item_id}` - Returns item details with optional query parameter `q`

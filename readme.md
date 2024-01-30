# Django ChatGPT Project

## Setup

1. Clone the repository:

```bash
git clone https://github.com/ObaidOIS/djangp-chatgpt.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Apply database migrations:

```bash
python manage.py migrate
```

4. Create a Superuser (Optional):

```bash
python manage.py createsuperuser
```

5. Start the development server:

```bash
python manage.py runserver
```

## Usage

### Register User

**Endpoint:** `/api/register/`

**Method:** `POST`

**Request Body:**
`username` (string): User's username
`password` (string): User's password

### Login User

**Endpoint:** `/api/login/`

**Method:** `POST`

**Request Body:**
`username` (string): User's username
`password` (string): User's password

### Chat Interaction

**Endpoint:** `/api/chat/`

**Method:** `POST`

**Request Headers:**
`Authorization`: Bearer <access_token> (Include the access token obtained after login)

**Request Body:**
`message` (string): User's message for ChatGPT

### Get User Conversations

**Endpoint:** `/api/getChat/`

**Method:** `GET`

**Request Headers:**
`Authorization`: Bearer <access_token> (Include the access token obtained after login)

### Authentication Token

To authenticate requests to protected endpoints (e.g., /chat/ and /getChat/), include the following header:

```bash
Authorization: Bearer <access_token>
```

Replace <access_token> with the access token obtained after successful login.
To authenticate requests to protected endpoints (e.g., /chat/ and /getChat/), include the following header:

```bash
Make sure to replace the placeholder URLs, project name, and other details with your actual project information. This README provides a brief overview of the project, setup
instructions, and details about API endpoints and authentication.
```

# Blog App - Backend

This repository contains the **Django backend** for the Blog App. It provides RESTful API endpoints for managing and fetching blog posts.

## Features

- **Blog List API**: Returns a list of blogs with titles and descriptions.
- **Blog Detail API**: Returns the full content of a selected blog post.
- **Submodule Integration**: Can be included as a submodule in the frontend repository.

---

### Prerequisites

- Python 3.x installed on your system.
- Django and other required packages installed.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/Backend-Repo.git
   cd Backend-Repo
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## Folder Structure

```
backend/
├── blog_backend/         # Main Django project folder
├── blog/                 # Blog app for managing blog posts
├── manage.py             # Django project manager
└── requirements.txt      # List of dependencies
```

---

## API Endpoints

### Blog List

- **Endpoint**: `/api/blogs/`
- **Method**: GET
- **Response**:
  ```json
  [
      {
          "id": 1,
          "title": "First Blog",
          "description": "This is the first blog post.",
          "content": "Full content of the blog.",
          "created_at": "2023-01-01T00:00:00Z"
      }
  ]
  ```

### Blog Detail

- **Endpoint**: `/api/blogs/<id>/`
- **Method**: GET
- **Response**:
  ```json
  {
      "id": 1,
      "title": "First Blog",
      "description": "This is the first blog post.",
      "content": "Full content of the blog.",
      "created_at": "2023-01-01T00:00:00Z"
  }
  ```

---

## Integration with Frontend (Submodule)

This backend can be included as a submodule in the Flutter frontend repository.

### Adding the Backend as a Submodule

If using this backend in a frontend repository:

1. Navigate to the root of the frontend repository:
   ```bash
   cd path/to/frontend-repo
   ```

2. Add this repository as a submodule:
   ```bash
   git submodule add https://github.com/YourUsername/Backend-Repo.git backend
   ```

3. Commit the submodule reference:
   ```bash
   git add .gitmodules backend
   git commit -m "Add backend as a submodule"
   ```

4. Push the changes:
   ```bash
   git push
   ```

---

## Contributions

Contributions are welcome! Please open an issue or submit a pull request.

---

##license
---

These `README.md` files can be directly copied into their respective repositories (`Frontend-Repo` and `Backend-Repo`). Let me know if there’s anything else you’d like to modify! 🚀

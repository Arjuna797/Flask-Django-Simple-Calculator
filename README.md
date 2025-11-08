# Flask-Django-Simple-Calculator
A lightweight, educational web application demonstrating how Flask and Django can coexist within a single Python project to serve the same frontend (HTML, CSS, JavaScript). This project showcases how to run and containerize both frameworks for comparison and learning purposes.
| Category                 | Technology        | Version | Purpose                                               |
| ------------------------ | ----------------- | ------- | ----------------------------------------------------- |
| **Frontend**             | HTML5             | —       | Structure of the calculator interface                 |
|                          | CSS3              | —       | Styling and layout design                             |
|                          | JavaScript (ES6)  | —       | Handles calculator logic and user interaction         |
| **Backend Frameworks**   | Flask             | 3.0.3   | Lightweight Python web framework serving static files |
|                          | Django            | 5.1.2   | Full-featured Python framework serving same frontend  |
| **Programming Language** | Python            | 3.11    | Core language for both Flask and Django               |
| **Containerization**     | Docker            | Latest  | Containerization of Flask and Django apps             |
|                          | Docker Compose    | Latest  | Manages multi-container setup (Flask + Django)        |
| **Environment / Tools**  | pip               | Latest  | Python dependency manager                             |
|                          | virtualenv        | Latest  | Virtual environment for isolated development          |
|                          | VS Code / PyCharm | —       | Recommended IDEs for editing and debugging            |
| **Version Control**      | Git & GitHub      | —       | Source code management and hosting                    |
| **Ports**                | Flask App         | 8080    | Access app at `http://localhost:8080`                 |
|                          | Django App        | 8081    | Access app at `http://localhost:8081`                 |

## 🚀 Run Locally with Docker

Use the appropriate command based on your operating system:

```bash
# On Ubuntu / Linux
docker-compose up -d

# On Windows
docker compose up -d

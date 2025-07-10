# 🌉 Project-Bridge

> A shared space built with Python for us to connect and learn to code together.

---

### The "Why"

This is our collaborative project to learn Python. We're building a simple client-server application from scratch that will serve as our own private, shared space on the internet. The goal is to learn by doing and to build something meaningful for us.

### Core Features (Our "Circles")

This is our roadmap. We'll check things off as we build them!

-   [x] **Foundation:** Basic Python, Git/GitHub, and environment setup.
-   [ ] **Center Circle (The API):** A central server that can send and receive messages.
-   [ ] **Notes System:** A feature to create, view, and share notes with each other.
    -   [ ] Private notes
    -   [ ] Shared notes
-   [ ] **To-Do List:** A shared checklist.
-   [ ] **Calendar:** A shared calendar for important dates.
-   [ ] _(More ideas to come!)_

---

### Tech Stack

*   **Language:** Python
*   **API Framework:** Flask (or FastAPI)
*   **Database:** SQLite (to start)
*   **Deployment:** PythonAnywhere (or Render)

---

### How to Set Up and Run This Project

This is a reminder for us on how to get the project running on a new computer.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Project-Bridge.git
    cd Project-Bridge
    ```

2.  **Create a Virtual Environment:**
    ```bash
    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # On Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Server:**
    ```bash
    cd server
    flask run
    ```
    The server should now be running at `http://127.0.0.1:5000`.

---

### API Endpoints

_(We will fill this out as we build the API. This will be our documentation!)_

*   `GET /`: Returns a simple "Hello" message.
*   `GET /notes`: Returns all shared notes and private notes for a user.
*   `POST /notes`: Creates a new note.

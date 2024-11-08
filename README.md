1. Install Node.js https://nodejs.org/en and Python 3.12 https://www.python.org/downloads/release/python-3127/ and git https://git-scm.com/downloads

2. Open a terminal and type the commands one by one

```bash
git clone https://github.com/GeneralMari0/COMP455---Final-Project
cd COMP455---Final-Project

cd backend
python -m pip install Flask Flask-Cors Flask-SQLAlchemy
python app.py
```

3. Open a new terminal **in the backend folder** and type the command

```bash
python populate_db.py
```

4. You should see "Database initialized successfully." Navigate to the frontend now using the following commands (or just open a new terminal in the frontend folder).

```bash
cd ..
cd frontend
```

5. Install the modules with the command:

```bash
npm i
```

5. Wait for all the modules to be installed. Then type the command:
```bash
npm start
```

6. That should open your browser to localhost:3000 or http://127.0.0.1:3000. Try out the search.

You can modify any code in the frontend folder and it should be updated without restarting the frontend terminal (you may have to refresh the page in chrome or whatever browser). For the backend, I think you have to restart the server every time you update the code. So in the terminal where you ran `python app.py` just stop the server with Ctrl+C and run the `python app.py` command again.
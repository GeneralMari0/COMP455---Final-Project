1. Install Elasticsearch 8.16 https://www.elastic.co/downloads/elasticsearch

2. Unzip the Elasticsearch archive
3. Run bin/elasticsearch (or bin\elasticsearch.bat on Windows)
4. Shutdown the server terminal
5. Edit config\elasticsearch.yml and set the following to false
```
xpack.security.enabled: false
xpack.security.transport.ssl.enabled: false
xpack.security.http.ssl.enabled: false
```
6. Start the server again. (bin\elasticsearch.bat) 
7. Open an terminal and type the following
```bash
curl http://localhost:9200/_cluster/health?pretty
```
8. If you see `status: "red"` then you either don't have enough disk space (you need minimum 50 GB) or something else went wrong, it needs to say yellow or green
9. Install Node.js https://nodejs.org/en and Python 3.12 https://www.python.org/downloads/release/python-3127/ and git https://git-scm.com/downloads

10. Open a terminal and type the commands one by one

```bash
git clone https://github.com/GeneralMari0/COMP455---Final-Project
cd COMP455---Final-Project

cd backend
python -m pip install Flask Flask-Cors elasticsearch-dsl
python app.py
```

11. Open a new terminal **in the backend folder** and type the command

```bash
python populate_db.py
```

12. You should see "Database initialized successfully." Navigate to the frontend now using the following commands (or just open a new terminal in the frontend folder).

```bash
cd ..
cd frontend
```

13. Install the modules with the command:

```bash
npm i
```

14. Wait for all the modules to be installed. Then type the command:
```bash
npm start
```

15. That should open your browser to localhost:3000 or http://127.0.0.1:3000. Try out the search.

You can modify any code in the frontend folder and it should be updated without restarting the frontend terminal (you may have to refresh the page in chrome or whatever browser). For the backend, I think you have to restart the server every time you update the code. So in the terminal where you ran `python app.py` just stop the server with Ctrl+C and run the `python app.py` command again.
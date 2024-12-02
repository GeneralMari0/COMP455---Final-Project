1. Download ElasticSearch 8.16.1 (https://www.elastic.co/downloads/elasticsearch), and extract the archive.
2. Enter the folder containing the contents of the archive and run bin\elasticsearch.bat. (bin/elasticsearch on Linux)

**NOTE**: Download the correct version of ElasticSearch for your operating system, otherwise the bundled Java JDK will not work. If Java is still not detected after verifying this, it may be easier to install Java system-wide. (https://www.java.com/en/download)

3. Shutdown the server (Ctrl+C).
4. Set the following from the default of `true` to `false` in config\elasticsearch.yml:
```
xpack.security.enabled: false
```

5. Start the server again. (bin\elasticsearch.bat) 
6. Open a terminal and query the health of the ElasticSearch server:
```bash
curl "http://localhost:9200/_cluster/health?pretty"
```

7. If you see `status: "red"` then something went wrong, such as not having enough disk space (minimum 50 GB). `status` must be `"yellow"` or `"green"` to function properly.
8. Install Node.js (https://nodejs.org/en/download), Python 3.12 (https://www.python.org/downloads/release/python-3127), and Git. (https://git-scm.com/downloads)
9. Open a terminal and run the following commands one by one to clone the repository, enter it, install the required python packages, and start the backend:
```bash
git clone https://github.com/GeneralMari0/COMP455---Final-Project
cd COMP455---Final-Project\backend
python -m pip install Flask Flask-Cors elasticsearch-dsl
python app.py
```

**NOTE**: After running the following command, the index will be saved to disk, and will persist across ElasticSearch restarts.
10. Open a new terminal **in the backend folder** and populate the database:
```bash
python populate_db.py
```

11. You should see "Database initialized successfully." Navigate to the frontend folder and install the required Node.js packages:
```bash
cd ..\frontend
npm i
```

12. After the modules are installed, start the frontend:
```bash
npm start
```

13. You browser should open to http://localhost:3000 (or http://127.0.0.1:3000), where you can try out the search.


Note: You can make changes to code in the frontend folder and it should be updated without having to restart (you may still have to refresh the page in your browser). For modifications to the backend, you may have to restart the server every time. To do this, stop the backend (Ctrl+C) in the terminal where it was started (`python app.py`), and then start it again.

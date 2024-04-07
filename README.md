## ML Fast API and Flask Web App deployment in Google Cloud GCPg

All the files outside the folder WebApp are mainly for API based deployment on GCP and common files. However, the ones inside the folder WebApp are for Web application based deployment on GCP and some common files share by both the applications are outside this folder. Though, GCP takes main.py as python file, I had to change the one inside WebApp folder to app.py as there was a conflict as both the applications had the same files name main.py and I wanted to store the code base in one location for both the applications.

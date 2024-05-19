## Educational web app

Small web-app for education and test purposes. Perfomed as microservice architecture app, therefore Very simple to readjust under your own needs.
You can run, test and wide this app for your purposes.

There are 3 branches:
- **develop**: where you can find the latest changes (as a rule it is not the working version)
- **pure_html**: where you can find version with pure html+css+js frontend
- **react**: where you can find version with react frontend.

Both **pure_html** and **react** versions are frames ready for use. You can readjust and wide them for your purposes.

**I would be very happy for your suggestions regarding to any essential remarks (vulnerabilities, runtime, clear arch, etc.)**

For testing service:
- switch to desired branch
- run **make up**
- run **make migratedb**
- run **make filldb**
- test on "https://localhost"


### ALEMBIC REMARKS:

if you want to change your content in database, do:
- readjust your models (models.py)
- readjust your data (db_data.py)
- run **make migratedb**
- run **make filldb** (while app is running!)

### HTTPS REMARKS

Now there are self-made SSL-certificates and apporpriate nginx-configuration. Due to this, the connection https://localhost will be insecure. Just go into advanced and follow the site. If you want to deploy app in production, change them with CA-certificates and readjust your nginx.conf.

### REACT REMARKS

There is React frame implemented. To start development using React **by yourself from scratch**  follow theese steps:
- Create folder for your service.
- Create Dockerfile inside this folder with content of react_service/Dockerfile
- Launch **docker run -it --rm -v "$PWD":/app:rw react_builder npx create-react-app my-react-app**
In appeared folder ***my-react-app*** create another Dockerfile with content of **my-react-app/Dockerfile**
Launch **docker build -t react_app_dev --target dev .**
Launch **docker run --rm -it -p 3000:3000 -v $PWD:/app react_app_dev**
Now you can access your react app from browser on **localhost:3000**

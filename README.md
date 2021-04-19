### Requirements:
- Docker installed

### Build Docker image:
- `docker build -t NicolasApp .`

### Run the Docker container:
- `docker run -d -p 5000:5000 NicolasApp:latest`

and then access the application at http://localhost:5000



### Local build environment:
- requires python3.6 or higher
- prefered virtual environment with the following requirement.txt

` python3 -m venv venv `

`source venv/bin/activate`

`python3 -m pip install -r requirements.txt`


### TESTS :
run python3 - m pytest

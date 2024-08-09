
Here's an updated README.md file based on the provided sources:
# People Museum

"I would trade all my technology for an afternoon with Socrates.” -- Steve Jobs

The People Museum app empowers ordinary people-- not just coders-- to create gen-AI powered conversations as Steve Jobs asked some years ago, and to build collections of interesting people. Teachers and historians can build educational experiences for their students, communities can build people collections that illustrate the greatness of the group.

## API documentation

[Check out](API-doc.md)

## Backend Setup

### Make a backend directory
```
mkdir peopleMuseum 
cd peopleMuseum
```

### Create conda environment
```
conda env list 
conda create -n pplmuseum python=3.11 
conda activate pplmuseum
```

### Clone the backend repo
```
git clone https://github.com/People-Museum-Project/people-museum-backend.git
```

### Install the requirements of the basic backend library
```
cd people-museum-backend 
pip3 install -r requirements.txt
```

### Install the GCP datastore library
```
pip install google-cloud-datastore
```

### Add environment variables
**Make sure to replace the placeholders with your actual GCP credential file path, project ID, and OpenAI API key.**
```
export PROJECT="your_gcp_project_id" export GOOGLE_APPLICATION_CREDENTIALS="/your_path_to_gcp_credential_file.json" export OPENAI_API_KEY="your_openai_api_key"
```

### Run the server
```
python server.py
```

## Docker Setup

### Build the Docker image
**Make sure to replace the placeholders in the Dockerfile with your actual GCP credential file path, project ID, and OpenAI API key before building.**
```
docker build -t people-museum-backend .
```

### Run the Docker container
```
docker run -p 8080:8080 people-museum-backend
```
This will start the People Museum backend server on port 8080.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
`
## License

[MIT](https://mit-license.org/)

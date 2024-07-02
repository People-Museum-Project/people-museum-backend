# People Museum
"I would trade all my technology for an afternoon with Socrates.” -- Steve Jobs

The People Museum app empowers ordinary people-- not just coders-- to create gen-AI powered conversations as Steve Jobs asked some years ago, and to build collections of interesting people. Teachers and historians can build educational experiences for their students, communities can build people collections that illustrate the greatness of the group.

## API documentation
[check out](API-doc.md)

##  Backend set up

### make a backend directory
```commandline
mkdir peopleClient
cd peopleClient
```

### create conda environment
```commandline
conda env list
conda create -n pplmuseum python=3.11
conda activate pplmuseum
```

### clone the backend repo
```commandline
git clone https://github.com/People-Museum-Project/people-museum-backend.git
```

### install the requirement of basic backend library
```commandline
cd people-museum-backend
pip3 install -r requirement.txt
```

### install the GCP datastore library
```commandline
pip install google-cloud-datastore
```

### Add enviroment variable
```commandline
export PROJECT="peoplemuseumyeah"
export GOOGLE_APPLICATION_CREDENTIALS=/your_path_to_GCP_credential_file/peoplemuseumyeah-18378c2ff07f.json
```

### Run the server
```commandline
python server.py
```
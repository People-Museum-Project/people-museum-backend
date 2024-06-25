# people-museum
"I would trade all my technology for an afternoon with Socrates.” -- Steve Jobs

The People Museum app empowers ordinary people-- not just coders-- to create gen-AI powered conversations as Steve Jobs asked some years ago, and to build collections of interesting people. Teachers and historians can build educational experiences for their students, communities can build people collections that illustrate the greatness of the group.

# Backend set up
```commandline
# make a backend directory
mkdir peopleClient
cd peopleClient

# create conda environment
conda env list
conda create -n pplmuseum python=3.11
conda activate pplmuseum

# clone the backend repo
git clone https://github.com/People-Museum-Project/people-museum-backend.git

# install the requirement of basic backend library
cd people-museum-backend
pip3 install -r requirement.txt

# install the GCP datastore library
pip install google-cloud-datastore

# Add enviroment variable
export PROJECT="peoplemuseumyeah"
export GOOGLE_APPLICATION_CREDENTIALS=/your_path_to_GCP_credential_file/peoplemuseumyeah-18378c2ff07f.json

python server.py
```
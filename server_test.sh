#!/bin/bash

# Base URL
BASE_URL="http://127.0.0.1:8080"

# Test addUser
echo "Testing addUser..."
curl -X POST "$BASE_URL/db/addUser" -H "Content-Type: application/json" -d '{
  "name": "Jordan Peterson",
  "imageLink": "http://example.com/jp_image.jpg",
  "description": "A new user"
}'
echo -e "\n"

# Test getUser
echo "Testing getUser..."
curl -X POST "$BASE_URL/db/getUser" -H "Content-Type: application/json" -d '{
  "userId": 5639601012080640
}'
echo -e "\n"

# Test listUsers
echo "Testing listUsers..."
curl -X GET "$BASE_URL/db/listUsers"
echo -e "\n"

# Test updateUser
echo "Testing updateUser..."
curl -X PUT "$BASE_URL/db/updateUser" -H "Content-Type: application/json" -d '{
  "userId": 5642061785071616,
  "name": "Foo Bar",
  "imageLink": "http://example.com/newimage.jpg",
  "description": "Updated description"
}'
echo -e "\n"

# Test deleteUser
echo "Testing deleteUser..."
curl -X DELETE "$BASE_URL/db/deleteUser" -H "Content-Type: application/json" -d '{
  "userId": 5644523313037312
}'
echo -e "\n"

# Test addPerson
echo "Testing addPerson..."
curl -X POST "$BASE_URL/db/addPerson" -H "Content-Type: application/json" -d '{
  "name": "Alice",
  "imageLink": "http://example.com/person.jpg",
  "description": "A foo person",
  "context": "Some context",
  "userId": 5642061785071616,
  "public": true
}'
echo -e "\n"

# Test getPersonList
echo "Testing getPersonList..."
curl -X POST "$BASE_URL/db/getPersonList" -H "Content-Type: application/json" -d '{
  "googleUserId": "7s6fzzlWcifsb7iS7Q8TdTOHoW72",
  "sortBy": "name",
  "limit": 10,
  "page": 1,
  "ascending": true
}'
echo -e "\n"

# Test getPersonListByCollection
echo "Testing getPersonListByCollection..."
curl -X POST "$BASE_URL/db/getPersonListByCollection" -H "Content-Type: application/json" -d '{
  "collectionId": 5715241090416640,
  "sortBy": "name",
  "limit": 10,
  "page": 1,
  "ascending": true
}'
echo -e "\n"

# Test getPerson
echo "Testing getPerson..."
curl -X POST "$BASE_URL/db/getPerson" -H "Content-Type: application/json" -d '{
  "personId": "5088723339313152"
}'
echo -e "\n"

# Test updatePerson
echo "Testing updatePerson..."
curl -X PUT "$BASE_URL/db/updatePerson" -H "Content-Type: application/json" -d '{
  "personId": 5723707007827968,
  "newName": "Foo Bar",
  "newImageLink": "http://example.com/newperson.jpg",
  "newDescription": "Updated person description",
  "newContext": "Updated context",
  "newPublic": false
}'
echo -e "\n"

# Test deletePerson
echo "Testing deletePerson..."
curl -X DELETE "$BASE_URL/db/deletePerson" -H "Content-Type: application/json" -d '{
  "personId": 5665673409724416
}'
echo -e "\n"

# Test addCollection
echo "Testing addCollection..."
curl -X POST "$BASE_URL/db/addCollection" -H "Content-Type: application/json" -d '{
  "userId": 5642061785071616,
  "name": "Foo Collection",
  "imageLink": "http://example.com/collection.jpg",
  "description": "A new collection",
  "isPublic": true
}'
echo -e "\n"

# Test getCollectionList
echo "Testing getCollectionList..."
curl -X POST "$BASE_URL/db/getCollectionList" -H "Content-Type: application/json" -d '{
  "googleUserId": "7s6fzzlWcifsb7iS7Q8TdTOHoW72",
  "page": 1,
  "limit": 10,
  "sortBy": "name",
  "ascending": false
}'
echo -e "\n"

# Test getCollection
echo "Testing getCollection..."
curl -X POST "$BASE_URL/db/getCollection" -H "Content-Type: application/json" -d '{
  "collectionId": 5675594515742720
}'
echo -e "\n"

# Test updateCollection
echo "Testing updateCollection..."
curl -X PUT "$BASE_URL/db/updateCollection" -H "Content-Type: application/json" -d '{
  "collectionId": 5680529164730368,
  "newName": "Updated Collection",
  "newImageLink": "http://example.com/newcollection.jpg",
  "newDescription": "Updated collection description",
  "newIsPublic": false
}'
echo -e "\n"

# Test deleteCollection
echo "Testing deleteCollection..."
curl -X DELETE "$BASE_URL/db/deleteCollection" -H "Content-Type: application/json" -d '{
  "collectionId": 5722267187150848
}'
echo -e "\n"

# Test getCollectionListByPerson
echo "Testing getCollectionListByPerson..."
curl -X POST "$BASE_URL/db/getCollectionListByPerson" -H "Content-Type: application/json" -d '{
  "personId": 5748214695198720,
  "sortBy": "name",
  "ascending": true,
  "limit": 10,
  "page": 1
}'
echo -e "\n"

# Test addPersonCollection
echo "Testing addPersonCollection..."
curl -X POST "$BASE_URL/db/addPersonCollection" -H "Content-Type: application/json" -d '{
  "personId": 5748214695198720,
  "collectionId": 5755374237908992
}'
echo -e "\n"

# Remove person from collection
curl -X DELETE "$BASE_URL/db/deletePersonFromCollection" -H "Content-Type: application/json" -d '{
    "personId": 5748214695198720,
    "collectionId": 5755374237908992
}'
echo -e "\n"

# AI part
# Test /generateText endpoint
curl -X POST "$BASE_URL/ai/generateText" -H "Content-Type: application/json" -d '{
  "prompt": "What is the capital of France?",
  "model": "gpt-3.5-turbo"
}'
echo -e "\n"


# Test /askQuestion endpoint
curl -X POST "$BASE_URL/ai/askQuestion" -H "Content-Type: application/json" -d '{
  "conversation": [],
  "question": "What is the weather usually like in San Francisco?",
  "instructions": "You are a helpful assistant.",
  "assistant_id": "asst_ubKwp4KW8cDePhDv7Gf6adf9"
}'
echo -e "\n"


# Test /generateSamplePrompts endpoint
curl -X POST "$BASE_URL/ai/generateSamplePrompts" -H "Content-Type: application/json" -d '{
  "context": "Discuss the impact of climate change.",
  "num_samples": 3,
  "max_words": 50,
  "assistant_id": "asst_ubKwp4KW8cDePhDv7Gf6adf9",
  "followups": true
}'
echo -e "\n"


# Test /generateFollowups endpoint
curl -X POST "$BASE_URL/ai/generateFollowups" -H "Content-Type: application/json" -d '{
  "question": "What are the causes of global warming?",
  "response": "Global warming is primarily caused by the increase in greenhouse gases in the atmosphere.",
  "num_samples": 2,
  "max_words": 50,
  "assistant_id": "asst_ubKwp4KW8cDePhDv7Gf6adf9"
}'

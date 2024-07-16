#!/bin/bash

# Base URL
BASE_URL="http://127.0.0.1:8080/db"

# Test addUser
echo "Testing addUser..."
curl -X POST "$BASE_URL/addUser" -H "Content-Type: application/json" -d '{
  "name": "Jordan Peterson",
  "imageLink": "http://example.com/jp_image.jpg",
  "description": "A new user"
}'
echo -e "\n"

# Test getUser
echo "Testing getUser..."
curl -X POST "$BASE_URL/getUser" -H "Content-Type: application/json" -d '{
  "userId": 5639601012080640
}'
echo -e "\n"

# Test listUsers
echo "Testing listUsers..."
curl -X GET "$BASE_URL/listUsers"
echo -e "\n"

# Test updateUser
echo "Testing updateUser..."
curl -X PUT "$BASE_URL/updateUser" -H "Content-Type: application/json" -d '{
  "userId": 5642061785071616,
  "name": "Foo Bar",
  "imageLink": "http://example.com/newimage.jpg",
  "description": "Updated description"
}'
echo -e "\n"

# Test deleteUser
echo "Testing deleteUser..."
curl -X DELETE "$BASE_URL/deleteUser" -H "Content-Type: application/json" -d '{
  "userId": 5644523313037312
}'
echo -e "\n"

# Test addPerson
echo "Testing addPerson..."
curl -X POST "$BASE_URL/addPerson" -H "Content-Type: application/json" -d '{
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
curl -X POST "$BASE_URL/getPersonList" -H "Content-Type: application/json" -d '{
  "userId": 5642061785071616,
  "sortBy": "name",
  "limit": 10,
  "page": 1,
  "order": "asc"
}'
echo -e "\n"

# Test getPersonListByCollection
echo "Testing getPersonListByCollection..."
curl -X POST "$BASE_URL/getPersonListByCollection" -H "Content-Type: application/json" -d '{
  "collectionId": 5675594515742720,
  "sortBy": "name",
  "limit": 10,
  "page": 1,
  "ascending": true
}'
echo -e "\n"

# Test getPerson
echo "Testing getPerson..."
curl -X POST "$BASE_URL/getPerson" -H "Content-Type: application/json" -d '{
  "personId": "5088723339313152"
}'
echo -e "\n"

# Test updatePerson
echo "Testing updatePerson..."
curl -X PUT "$BASE_URL/updatePerson" -H "Content-Type: application/json" -d '{
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
curl -X DELETE "$BASE_URL/deletePerson" -H "Content-Type: application/json" -d '{
  "personId": 5665673409724416
}'
echo -e "\n"

# Test addCollection
echo "Testing addCollection..."
curl -X POST "$BASE_URL/addCollection" -H "Content-Type: application/json" -d '{
  "userId": 5642061785071616,
  "name": "Foo Collection",
  "imageLink": "http://example.com/collection.jpg",
  "description": "A new collection",
  "isPublic": true
}'
echo -e "\n"

# Test getCollectionList
echo "Testing getCollectionList..."
curl -X POST "$BASE_URL/getCollectionList" -H "Content-Type: application/json" -d '{
  "userId": 5642061785071616,
  "page": 1,
  "limit": 10,
  "sortBy": "name",
  "order": "asc"
}'
echo -e "\n"

# Test getCollection
echo "Testing getCollection..."
curl -X POST "$BASE_URL/getCollection" -H "Content-Type: application/json" -d '{
  "collectionId": 5675594515742720
}'
echo -e "\n"

# Test updateCollection
echo "Testing updateCollection..."
curl -X PUT "$BASE_URL/updateCollection" -H "Content-Type: application/json" -d '{
  "collectionId": 5680529164730368,
  "newName": "Updated Collection",
  "newImageLink": "http://example.com/newcollection.jpg",
  "newDescription": "Updated collection description",
  "newIsPublic": false
}'
echo -e "\n"

# Test deleteCollection
echo "Testing deleteCollection..."
curl -X DELETE "$BASE_URL/deleteCollection" -H "Content-Type: application/json" -d '{
  "collectionId": 5722267187150848
}'
echo -e "\n"

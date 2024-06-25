#!/bin/bash

# Base URL
BASE_URL="http://127.0.0.1:8080"

## 1. Test index endpoint
#curl -X GET "${BASE_URL}/" -H "Content-Type: application/json"
#echo -e "\n"

# 2. Test addUser endpoint
curl -X POST "${BASE_URL}/addUser" -H "Content-Type: application/json" -d '{
  "name": "John Doe",
  "imageLink": "http://example.com/image.jpg",
  "description": "A new user"
}'
echo -e "\n"

## 3. Test getUser endpoint
#curl -X POST "${BASE_URL}/getUser" -H "Content-Type: application/json" -d '{
#  "userId": "1"
#}'
#echo -e "\n"
#
## 4. Test updateUser endpoint
#curl -X PUT "${BASE_URL}/updateUser" -H "Content-Type: application/json" -d '{
#  "userId": "1",
#  "name": "John Smith",
#  "imageLink": "http://example.com/newimage.jpg",
#  "description": "An updated user"
#}'
#echo -e "\n"
#
## 5. Test deleteUser endpoint
#curl -X DELETE "${BASE_URL}/deleteUser" -H "Content-Type: application/json" -d '{
#  "userId": "1"
#}'
#echo -e "\n"
#
## 6. Test addPerson endpoint
#curl -X POST "${BASE_URL}/addPerson" -H "Content-Type: application/json" -d '{
#  "name": "Jane Doe",
#  "imageLink": "http://example.com/person.jpg",
#  "description": "A new person",
#  "context": "Example context",
#  "public": true
#}'
#echo -e "\n"
#
## 7. Test getPersonList endpoint
#curl -X POST "${BASE_URL}/getPersonList" -H "Content-Type: application/json" -d '{
#  "userId": "1"
#}'
#echo -e "\n"
#
## 8. Test getPerson endpoint
#curl -X POST "${BASE_URL}/getPerson" -H "Content-Type: application/json" -d '{
#  "userId": "1",
#  "personId": "1"
#}'
#echo -e "\n"
#
## 9. Test updatePerson endpoint
#curl -X PUT "${BASE_URL}/updatePerson" -H "Content-Type: application/json" -d '{
#  "userId": "1",
#  "personId": "1",
#  "newName": "Jane Smith",
#  "newImageLink": "http://example.com/newperson.jpg",
#  "newDescription": "An updated person",
#  "newContext": "New context",
#  "newPublic": false
#}'
#echo -e "\n"
#
## 10. Test deletePerson endpoint
#curl -X DELETE "${BASE_URL}/deletePerson" -H "Content-Type: application/json" -d '{
#  "userId": "1",
#  "personId": "1"
#}'
#echo -e "\n"
#
## 11. Test addCollection endpoint
#curl -X POST "${BASE_URL}/addCollection" -H "Content-Type: application/json" -d '{
#  "userId": "1",
#  "name": "Collection 1",
#  "imageLink": "http://example.com/collection.jpg",
#  "description": "A new collection",
#  "isPublic": true
#}'
#echo -e "\n"
#
## 12. Test getCollectionList endpoint
#curl -X POST "${BASE_URL}/getCollectionList" -H "Content-Type: application/json" -d '{
#  "userId": "1"
#}'
#echo -e "\n"
#
## 13. Test getCollection endpoint
#curl -X POST "${BASE_URL}/getCollection" -H "Content-Type: application/json" -d '{
#  "userId": "1",
#  "collectionId": "1"
#}'
#echo -e "\n"
#
## 14. Test updateCollection endpoint
#curl -X PUT "${BASE_URL}/updateCollection" -H "Content-Type: application/json" -d '{
#  "userId": "1",
#  "collectionId": "1",
#  "newName": "Updated Collection",
#  "newImageLink": "http://example.com/updatedcollection.jpg",
#  "newDescription": "An updated collection",
#  "newIsPublic": false
#}'
#echo -e "\n"
#
## 15. Test deleteCollection endpoint
#curl -X DELETE "${BASE_URL}/deleteCollection" -H "Content-Type: application/json" -d '{
#  "userId": "1",
#  "collectionId": "1"
#}'
#echo -e "\n"

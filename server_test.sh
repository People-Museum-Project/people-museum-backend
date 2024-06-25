#!/bin/bash

# Base URL
BASE_URL="http://127.0.0.1:8080"

# 1. Test index endpoint
curl -X GET "http://127.0.0.1:8080/" -H "Content-Type: application/json"
echo -e "\n"

# 2. Test addUser endpoint
curl -X POST "http://127.0.0.1:8080/addUser" -H "Content-Type: application/json" -d '{
  "name": "John Doe",
  "imageLink": "http://example.com/image.jpg",
  "description": "A new user"
}'
echo -e "\n"

# 3. Test getUser endpoint
curl -X POST "http://127.0.0.1:8080/getUser" -H "Content-Type: application/json" -d '{
  "userId": "5653635052601344"
}'
echo -e "\n"

# 4. Test updateUser endpoint
curl -X PUT "http://127.0.0.1:8080/updateUser" -H "Content-Type: application/json" -d '{
  "userId": "5653635052601344",
  "name": "John Smith",
  "imageLink": "http://example.com/newimage.jpg",
  "description": "An updated user"
}'
echo -e "\n"

# 5. Test deleteUser endpoint
curl -X DELETE "http://127.0.0.1:8080/deleteUser" -H "Content-Type: application/json" -d '{
  "userId": "5653635052601344"
}'
echo -e "\n"

# 6. Test addPerson endpoint
curl -X POST "http://127.0.0.1:8080/addPerson" -H "Content-Type: application/json" -d '{
  "name": "Jane Doe",
  "imageLink": "http://example.com/person.jpg",
  "description": "A new person",
  "context": "Example context",
  "public": true
}'
echo -e "\n"

# 7. Test getPersonList endpoint
curl -X POST "http://127.0.0.1:8080/getPersonList" -H "Content-Type: application/json" -d '{
  "userId": "1"
}'
echo -e "\n"

# 8. Test getPerson endpoint
curl -X POST "http://127.0.0.1:8080/getPerson" -H "Content-Type: application/json" -d '{
  "personId": "5637476211228672"
}'
echo -e "\n"

# 9. Test updatePerson endpoint
curl -X PUT "http://127.0.0.1:8080/updatePerson" -H "Content-Type: application/json" -d '{
  "personId": "5637476211228672",
  "newName": "Jane Smith",
  "newImageLink": "http://example.com/newperson.jpg",
  "newDescription": "An updated person",
  "newContext": "New context",
  "newPublic": false
}'
echo -e "\n"

# 10. Test deletePerson endpoint
curl -X DELETE "http://127.0.0.1:8080/deletePerson" -H "Content-Type: application/json" -d '{
  "personId": "5637476211228672"
}'
echo -e "\n"

# 11. Test addCollection endpoint
curl -X POST "http://127.0.0.1:8080/addCollection" -H "Content-Type: application/json" -d '{
  "userId": "1",
  "name": "Collection 1",
  "imageLink": "http://example.com/collection.jpg",
  "description": "A new collection",
  "isPublic": true
}'
echo -e "\n"

# 12. Test getCollectionList endpoint
curl -X POST "http://127.0.0.1:8080/getCollectionList" -H "Content-Type: application/json" -d '{
  "userId": "1"
}'
echo -e "\n"

# 13. Test getCollection endpoint
curl -X POST "http://127.0.0.1:8080/getCollection" -H "Content-Type: application/json" -d '{
  "collectionId": "5629654941564928"
}'
echo -e "\n"

# 14. Test updateCollection endpoint
curl -X PUT "http://127.0.0.1:8080/updateCollection" -H "Content-Type: application/json" -d '{
  "collectionId": "5629654941564928",
  "newName": "Updated Collection",
  "newImageLink": "http://example.com/updatedcollection.jpg",
  "newDescription": "An updated collection",
  "newIsPublic": false
}'
echo -e "\n"

# 15. Test deleteCollection endpoint
curl -X DELETE "http://127.0.0.1:8080/deleteCollection" -H "Content-Type: application/json" -d '{
  "collectionId": "5629654941564928"
}'
echo -e "\n"

curl -X POST "http://127.0.0.1:8000/people_collection/" \
     -H "Content-Type: application/json" \
     -d '{
           "name": "Collection Name",
           "image": "http://example.com/collection_image.jpg",
           "description": "A sample collection",
           "bio_documents": ["Bio doc 1", "Bio doc 2"],
           "persons": ["person_id_1", "person_id_2"],
           "owner": "owner_user_id",
           "shareList": ["user1", "user2"],
           "is_public": true
         }'

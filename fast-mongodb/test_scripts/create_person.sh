curl -X POST "http://127.0.0.1:8000/person/" \
     -H "Content-Type: application/json" \
     -d '{
           "name": "John Doe",
           "image": "http://example.com/image.jpg",
           "description": "A sample person",
           "bio_documents": ["Bio document 1", "Bio document 2"],
           "authored_documents": ["Document 1", "Document 2"],
           "collections": [],
           "owner": "owner_user_id",
           "shareList": ["user1", "user2"],
           "is_public": true
         }'

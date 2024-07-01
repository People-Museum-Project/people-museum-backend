curl -X POST "http://127.0.0.1:8000/user/" \
     -H "Content-Type: application/json" \
     -d '{
           "username": "johndoe",
           "email": "johndoe@example.com",
           "password": "securepassword"
         }'

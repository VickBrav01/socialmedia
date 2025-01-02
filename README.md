<!-- Social Media API -->

This API enables users to perform various social media functions, including creating posts, following/unfollowing users, and viewing a feed of posts. The API uses JSON Web Tokens (JWT) for authentication.

<!-- Features -->

<!-- User Management: -->

   1.User registration and authentication using JWT.

   2.View user details, including followers and following.

<!-- Posts: -->

   CRUD operations for posts.

   Like and unlike posts.

   Follow System:

   Follow/unfollow users.

   View followers and following.

<!-- Feed: -->

   Display posts from followed users.

<!-- Authentication -->

   Authentication is handled using JWT. Users must include their token in the Authorization header as a Bearer token for all protected endpoints.

<!-- Example: -->



Endpoints

<!-- User Endpoints -->

   Register: /api/users/register/ (POST)

   Login: /api/users/login/ (POST)

   Profile: /api/users/<id>/ (GET)

<!-- Post Endpoints -->

   Create Post: /api/posts/ (POST)

   Get Posts: /api/posts/ (GET)

   Update Post: /api/posts/<id>/ (PUT)

   Delete Post: /api/posts/<id>/ (DELETE)

   Like Post: /api/posts/<id>/like/ (POST)

   Unlike Post: /api/posts/<id>/unlike/ (DELETE)

<!-- Follow Endpoints -->

   Follow User: /api/follow/<id>/ (POST)

   Unfollow User: /api/unfollow/<id>/ (DELETE)


<!-- Feed Endpoint -->

   Get Feed: /api/feed/ (GET)



<!-- Install dependencies: -->

pip install -r requirements.txt


<!-- Apply migrations: -->

<!-- python manage.py migrate -->

<!-- Run the server: -->

   python manage.py runserver


<!-- Example Request -->

Register User

POST /api/users/register/
<!-- JSON Data -->
   {
   "username": "Vick",
   "email": "vick@gmail.com",
   "password": "password123"
   }

Response

{
  "id": 1,
  "username": "Vick",
  "email": "vick@gmail.com"
}

<!-- Note -->

Ensure JWT token is included in the header for authenticated requests.

Replace <id> with the appropriate user or post ID in endpoints.


Dynamic Movie Management APP

Project Organization:

backend/: This folder contains the FastAPI project.

frontend/: This folder contains the React app.


Description:
The Simple Movie App is a full-stack web application that allows users to manage a collection of movies. The backend is powered by FastAPI, providing a RESTful API for CRUD (Create, Read, Update, Delete) operations on the movie data. The frontend is built with React, offering a user interface to interact with the API.

Backend (FastAPI):
The backend is implemented using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python. It manages movie data stored in a text file and provides endpoints to perform CRUD operations.

Endpoints:

GET /movie/{movie_id}: Retrieve details of a specific movie by its ID.
PUT /movie/{movie_id}: Update the details of a specific movie.
DELETE /movie/{movie_id}: Delete a movie by its ID.

POST /movie/{movie_id}: Add a new movie to the collection.
  
  
CORS Middleware:
CORS (Cross-Origin Resource Sharing) is enabled to allow requests from the frontend, which typically runs on a different domain or port.

Data Model:
Movie: A Pydantic model that includes the movie ID, name, and cast.
Movie2: A simplified Pydantic model used for updating or creating a movie (without the ID).
Movies: A class that handles loading and managing movie data from a text file.

Frontend (React)
The frontend is built with React, a popular JavaScript library for building user interfaces. It communicates with the FastAPI backend to display movie data and allow users to manage their movie collection.

Key Files:

App.js: The main component of the React application.
index.js: The entry point of the React app.
App.css: Contains the styling for the app, including animations and layout.
App.test.js: Test file for the App component.
reportWebVitals.js: Utility for measuring performance of the app.

Styling:
The app uses a simple CSS-based styling with some animations for the logo and a dark-themed header.
Setup Instructions

Backend
Install Dependencies:
Navigate to the backend/ directory.
Install the required Python packages:

pip install -r requirements.txt

Run the Backend Server:
Start the FastAPI server:
uvicorn main:app --reload
The server will be accessible at http://localhost:8000.

Frontend:
Install Dependencies:
- Navigate to the frontend/ directory.
- Install the required npm packages:

npm install

Run the Frontend:
Start the React development server:
npm start

The app will be accessible at http://localhost:3000.

How to Use:

View Movies: Access the list of movies by navigating to the appropriate endpoint or using the frontend interface.
Add a Movie: Use the POST method via the API or the frontend form to add a new movie.
Update a Movie: Modify movie details using the PUT method.
Delete a Movie: Remove a movie using the DELETE method.

ADDITIONAL INFORMATION
This project was developed as part of a class assignment. The backend manages movie data and serves it to the frontend, which provides an interface for users to interact with the movie collection.


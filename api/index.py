# Import the FastAPI class to create our application instance
from fastapi import FastAPI
# Import CORSMiddleware to allow frontend domains to access our backend
from fastapi.middleware.cors import CORSMiddleware

# Create the main FastAPI application object
app = FastAPI()

# Define a list of allowed origins (the URLs of your frontend)
# Using "*" allows any frontend to connect, which is great for learning/testing
origins = [
    "*"
]

# Add the CORS middleware to our application to intercept and check requests
app.add_middleware(
    # Specify the middleware class to use
    CORSMiddleware,
    # Pass the list of allowed frontend URLs (our origins list)
    allow_origins=origins,
    # Allow credentials like cookies or authorization headers (set to True if needed)
    allow_credentials=True,
    # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.) by using "*"
    allow_methods=["*"],
    # Allow all HTTP headers to be sent in the request by using "*"
    allow_headers=["*"],
)

# Define a route decorator for a GET request to the root URL ("/")
@app.get("/")
# Define the function that will run when a frontend visits the root URL
def read_root():
    # Return a JSON response with a success message
    return {"message": "Hello! Your FastAPI backend is working and CORS is enabled!"}


@app.get("/dragon")
def get_dragon():
    return {"message": "I am a Dragon!"}    
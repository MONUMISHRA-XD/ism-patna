from pymongo import MongoClient

# MongoDB Atlas connection URI
uri = "mongodb+srv://monumishra_xd:monumishra_xd@cluster0.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
client = MongoClient(uri)

# Choose database and collection
db = client["mydb"]  # database name
collection = db["users"]  # collection name

# Take input from user
name = input("Enter your name: ")
email = input("Enter your email: ")

# Create document
user_data = {
    "name": name,
    "email": email
}

# Insert into MongoDB
result = collection.insert_one(user_data)

print(f"✅ Data inserted with ID: {result.inserted_id}")

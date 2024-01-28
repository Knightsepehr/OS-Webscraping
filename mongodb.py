from pymongo import MongoClient

def connection(database_name):
    client = MongoClient("mongodb://localhost:27017/")
    db = client[database_name]
    return db

def close_connection(client):
    try:
        client.close()
    except Exception as e:
        print(f"Error occurred when closing connection: {e}")

def try_execute(db,collection_name,data):
    collection = db[collection_name]
    try:
        collection.insert_one(data)
    except Exception as e:
        print(f"Error occurred: {e}")

def create_database(database_name):
    client = MongoClient("mongodb://localhost:27017/")
    try:
        client.create_database(database_name)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        close_connection(client)

def try_sql_query(db, title, description, url, img_url, author, views, downloads, license, resolution, category, img_id):
    collection_name = "image2"
    collection = db[collection_name]
    data = {
        "image_title": title,
        "description": description,
        "url": url,
        "img_url": img_url,
        "author": author,
        "views": views,
        "downloads": downloads,
        "license": license,
        "resolution": resolution,
        "category": category,
        "img_id": img_id
    }
    try_execute(db, collection_name, data)

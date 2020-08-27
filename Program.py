import pymongo
import random


def create_database(db):
    user_collection = db['users']
    user_collection.drop()
    user_collection = db['users']

    post_collection = db['posts']
    post_collection.drop()
    post_collection = db['posts']

    comment_collection = db['comments']
    comment_collection.drop()
    comment_collection = db['comments']

    like_collection = db['likes']
    like_collection.drop()
    like_collection = db['likes']

    status_collection = db['status']
    status_collection.drop()
    status_collection = db['status']

    followers_collection = db['followers']
    followers_collection.drop()
    followers_collection = db['followers']

    user_data = [
        {
            "_id": 1,
            "name": "Aakash",
            "email": "aakash@gmail.com",
            "phone":"647632134",
            "friends": 456,
            "pictures": 34,
            "contacts": 90,
            "isVerified": True
        },
        {
            "_id": 2,
            "name": "Anmol Monga",
            "email": "anmol@gmail.com",
            "phone": "6476546784",
            "friends": 665,
            "pictures": 76,
            "contacts": 50,
            "isVerified": True
        },
        {
            "_id": 3,
            "name": "Harjant Singh",
            "email": "harjant@gmail.com",
            "phone": "6478765545",
            "friends": 987,
            "pictures": 64,
            "contacts": 75,
            "isVerified": False
        },
        {
            "_id": 4,
            "name": "Prabhjot Singh",
            "email": "prabh@gmail.com",
            "phone": "6478672134",
            "friends": 654,
            "pictures": 68,
            "contacts": 46,
            "isVerified": True
        },
        {
            "_id": 5,
            "name": "Harkaran",
            "email": "harkaran@gmail.com",
            "phone": "64768664335",
            "friends": 786,
            "pictures": 74,
            "contacts": 87,
            "isVerified": False
        },
        {
            "_id": 6,
            "name": "Dipanshu",
            "email": "deep@gmail.com",
            "phone": "416082134",
            "friends": 756,
            "pictures": 86,
            "contacts": 34,
            "isVerified": True
        },
        {
            "_id": 7,
            "name": "Hrsimran",
            "email": "harsimran@gmail.com",
            "phone": "643732939",
            "friends": 234,
            "pictures": 74,
            "contacts": 70,
            "isVerified": False
        },
        {
            "_id": 8,
            "name": "Harpreet ",
            "email": "harpreet@gmail.com",
            "phone": "324776566",
            "friends": 856,
            "pictures": 94,
            "contacts": 50,
            "isVerified": True
        },

    ]

    user_status = [
        {
            "status": "Having Dinner at Bahamas",
            "uploadTime": "20:44",
            "location": "indonesia",
            "likes": 46,
            "comments": 34,
            "user": "Anmol"
        },
        {
            "status": "Playing cricket at Key Land Field",
            "uploadTime": "10:44",
            "location": "india",
            "likes": 56,
            "comments": 14,
            "user": "Aakash"
        },
        {
            "status": "Watching Movie at Cineplex Theatre",
            "uploadTime": "16:44",
            "location": "Canada",
            "likes": 96,
            "comments": 66,
            "user": "Harjant"
        },

        {
            "status": "Reading novel at pearson library",
            "uploadTime": "19:34",
            "location": "Toronto",
            "likes": 51,
            "comments": 34,
            "user": "Prabhjot"
        },

        {
            "status": "Playing Golf at Wee Golf Course",
            "uploadTime": "11:22",
            "location": "USA",
            "likes": 12,
            "comments": 3,
            "user": "Harkaran"
        },
    ]

    followers = [
        {
            "name": "Ali",
            "active": False,
            "lastSeen": "20-8-2020",
            "followers": 943,
            "username": "ali_zumair"
        },
        {
            "name": "Alex",
            "active": True,
            "lastSeen": "10-8-2020",
            "followers": 443,
            "username": "alex_scott"
        },
        {
            "name": "Lee",
            "active": False,
            "lastSeen": "10-3-2020",
            "followers": 333,
            "username": "lee_you"
        },
        {
            "name": "joe",
            "active": True,
            "lastSeen": "09-1-2020",
            "followers": 567,
            "username": "joe_Tribiani"
        },
        {
            "name": "Ross",
            "active": False,
            "lastSeen": "05-7-2020",
            "followers": 133,
            "username": "ross_geller"
        }
    ]

    #ADD DATA INTO COLLECTION

    user_ids = user_collection.insert_many(user_data)
    status_collection.insert_many(user_status)
    followers_collection.insert_many(followers)

    user_id_list = user_ids.inserted_ids

    like_id = 1
    post_id = 1
    comment_id = 1

    #ADD DUMMY POSTS
    for user_id in user_ids.inserted_ids:
        post_data = [{"_id": post_id,
                      "user_id": user_id,
                      "content": 'Dummy post', "view_count": 10,
                      "likes": [{"like_id": like_id}],
                      "comments": [{"comment_id": comment_id}]}]
        like_id += 1
        comment_id += 1
        post_id += 1
        post_collection.insert_many(post_data)

    comment_id = 1
    comment_all = []
    for p_id in range(1, post_id):
        comment_data = [{"_id": comment_id, "post_id": p_id,
                         "user_id": random.choice(user_id_list),
                         "comment": "Looks good"}]
        comment_collection.insert_many(comment_data)
        comment_all.append(comment_id)
        comment_id += 1

    like_id = 1
    for p_id in range(1, post_id):
        like_data = [{"_id": like_id, "post_id": p_id,
                      "user_id": random.choice(user_id_list),
                      "comment_id": random.choice(comment_all)}]
        like_collection.insert_many(like_data)
        like_id += 1

 #PRINT ALL USERS
def read_all_users(db):
    user_collection = db['users']
    for user in user_collection.find():
        print(user)

#PRINT SINGLE USER
def read_single_users(db):
    user_id = int(input("Enter user id: "))
    user_collection = db['users']
    for user in user_collection.find({"_id": user_id}):
        print(user)

#READ ALL POSTS
def read_all_post(db):
    post_collection = db['posts']
    for post in post_collection.find():
        print(post)

#PRINT SINGLE POST
def read_single_post(db):
    user_id = int(input("Enter user id: "))
    post_collection = db['posts']
    for post in post_collection.find({"user_id": user_id}):
        print(post)

#PRINT ALL COMMENTS
def read_all_comments(db):
    comment_collection = db['comments']
    for comment in comment_collection.find():
        print(comment)

#PRINT SINGLE COMMENTS
def read_single_comment(db):
    user_id = int(input("Enter user id: "))
    comment_collection = db['comments']
    for comment in comment_collection.find({"user_id": user_id}):
        print(comment)

#READ POST DATA
def read_post_comment(db):
    post_id = int(input("Enter post id: "))
    comment_collection = db['comments']
    for comment in comment_collection.find({"post_id": post_id}):
        print(comment)

#INSERT NEW USER INTO COLLECTION
def insert_user(db):
    users = db["users"]
    name = input("User name: ")
    email = input("User Email: ")
    ids = users.insert_many([{"name": name, "email": email}])
    print(ids.inserted_ids)

#DELETE COMMENT
def delete_comment(db):
    comment_id = int(input("Enter comment Id: "))

    comment_collection = db['comments']

    comment = comment_collection.find_one({"_id": comment_id})

    db.post.update(
        {"_id": comment["post_id"]},
        {"$pull": {"comments": {"comment_id": comment["_id"]}}}
    )

    comment_collection.delete_one({"_id": comment_id})

#UPDATE POST CONTENT
def update_post_content(db):
    post_id = int(input("Enter post Id: "))
    post_content = input("Enter post content: ")
    post_query = {"_id": post_id}
    update_data = {"$set": {"content": post_content}}
    db.posts.update_one(post_query, update_data)


if __name__ == '__main__': #CONNECT TO MONGO ATLAS
    client = pymongo.MongoClient("mongodb+srv://akash:lambton123@db.di1ed.mongodb.net/db?retryWrites=true&w=majority")
    database = client["feeddb"]
    create_database(database)

    print("Reading all users")
    read_all_users(database)
    print("Reading single user")
    read_single_users(database)

    print("Reading all posts")
    read_all_post(database)
    print("Reading single post")
    read_single_post(database)

    print("Reading all comments")
    read_all_comments(database)

    print("Reading single comment")
    read_single_comment(database)

    print("Reading all comments of a post")
    read_post_comment(database)

    print("Inserting new user")
    insert_user(database)

    print("Deleting comment")
    delete_comment(database)

    print("Reading all comments")
    read_all_comments(database)

    print("Updating the post")
    update_post_content(database)

    print("Reading all posts")
    read_all_post(database)

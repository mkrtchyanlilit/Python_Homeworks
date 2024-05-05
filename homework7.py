import requests

base_url = "https://jsonplaceholder.typicode.com"
# GET
response = requests.get(f"{base_url}/posts")

if response.status_code == 200:
    posts = response.json()

    filtered_posts = [post for post in posts if len(post['title'].split()) < 4]

    print("Filtered Posts:")
    for post in filtered_posts:
        print(post)

    # POST
    post_response = requests.post(f"{base_url}/posts", json={'title': 'New Post', 'body': 'New Body', 'userId': 1})
    print("POST Response:", post_response.status_code, post_response.json())

    # PUT
    put_response = requests.put(f"{base_url}/posts/1", json={'title': 'Updated Title', 'body': 'Updated Body'})
    print("PUT Response:", put_response.status_code)

    # GET updated post
    updated_post_response = requests.get(f"{base_url}/posts/1")
    updated_post = updated_post_response.json()
    print("Updated Post:", updated_post)

    # DELETE
    delete_response = requests.delete(f"{base_url}/posts/2")
    print("DELETE Response:", delete_response.status_code)

else:
    print("Failed to fetch posts:", response.status_code)



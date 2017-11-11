"""."""
import os
import requests


def main():
    """Run the start of the whole thing."""
    try:
        print_intro()
        send_post_request(user_input())
    except KeyboardInterrupt:
        print()
        print("Closing out!")


def user_input():
    """Get the user input."""
    title = input("Enter your post title: ")
    body = input("Share your thoughts: ")
    post = {'title': title, 'body': body}
    return post


def send_post_request(post):
    """Send the post to the learning journal."""
    url = os.environ.get("URL")
    response = requests.post(url + 'login',
                             data={'username': os.environ.get("AUTH_USERNAME"),
                                   'password': os.environ.get("AUTH_PASSWORD")})
    if response.status_code != 200:
        print("Login failed.")
    else:
        header = response.request.headers
        response = requests.post(url + 'journal/new-entry',
                                 data=post, headers=header)
        if response.status_code != 200:
            print("Posting failed.")
        else:
            print("Post was succesful!")


def print_intro():
    """Print the intro header when app is first run."""
    intro = """
    +-----------------------------------+
    |                                   |
    |                                   |
    |              POSTER               |
    |                                   |
    |                                   |
    +-----------------------------------+
    """
    print(intro)

if __name__ == "__main__":
    main()

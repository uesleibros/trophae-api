import requests

PAYLOAD: dict = {
	"email": "uesleibros@gmail.com",
	"username": "UesleiDev",
	"password": "abc123abc123"
}
session: requests.Session = requests.Session()
print(session.post("http://localhost:4000/auth/user/connect", json=PAYLOAD).json())
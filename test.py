import requests

BASE_URL = "http://localhost:3000/dev/send-email"

def print_result(test_name, response):
    print(f"\n🧪 {test_name}")
    print(f"Status Code: {response.status_code}")
    try:
        print("Response:", response.json())
    except:
        print("Response:", response.text)

# Test 1: Valid request
def test_success():
    data = {
        "receiver_email": "valid@test.com",
        "subject": "Test Email",
        "body_text": "Hello! This is a test email."  
    }
    headers = {"body_text-Type": "application/json"}
    response = requests.post(BASE_URL, json=data, headers=headers)
    print_result("Test Success", response)



# Test 2: Missing email (400)
def test_400_bad_request():
    data = {
        "subject": "No Email",
        "body_text": "Oops"
    }
    response = requests.post(BASE_URL, json=data)
    print_result("Test 400 Bad Request", response)

# Test 3: Unauthorized (401)
def test_401_unauthorized():
    data = {
        "receiver_email": "unauth@test.com",
        "subject": "Unauthorized",
        "body_text": "Failing test"
    }
    response = requests.post(BASE_URL, json=data)
    print_result("Test 401 Unauthorized", response)

# Test 4: Forbidden (403)
def test_403_forbidden():
    data = {
        "receiver_email": "forbidden@test.com",
        "subject": "Forbidden",
        "body_text": "Access denied"
    }
    response = requests.post(BASE_URL, json=data)
    print_result("Test 403 Forbidden", response)

# Test 5: Not found (404)
def test_404_not_found():
    response = requests.post(BASE_URL + "/xyz", json={})
    print_result("Test 404 Not Found", response)

# Test 6: Internal server error (500)
def test_500_server_error():
    data = {
        "receiver_email": "crash@test.com",
        "subject": "Crash",
        "body_text": "Break server"
    }
    response = requests.post(BASE_URL, json=data)
    print_result("Test 500 Server Error", response)

# Main menu
def main():
    print("\nChoose a test to run:")
    print("1. Test Success")
    print("2. Test 400 Bad Request")
    print("3. Test 401 Unauthorized")
    print("4. Test 403 Forbidden")
    print("5. Test 404 Not Found")
    print("6. Test 500 Server Error")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        test_success()
    elif choice == "2":
        test_400_bad_request()
    elif choice == "3":
        test_401_unauthorized()
    elif choice == "4":
        test_403_forbidden()
    elif choice == "5":
        test_404_not_found()
    elif choice == "6":
        test_500_server_error()
    else:
        print("Invalid choice. Please run the script again and select a valid option.")

if __name__ == "__main__":
    main()

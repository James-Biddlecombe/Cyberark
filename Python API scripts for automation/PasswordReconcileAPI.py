import requests

# set the PVWA URL as a variable
PVWA = "https://x.x.x.pvwaURL/PasswordVault"
LogonUser = "api_user"
LogonPass = "Cyberark1"

# these are the env details used to access the API
LogonURL = str(PVWA) + "/API/Auth/Cyberark/Logon"
payload = {"username":str(LogonUser),"password":str(LogonPass)}
headers = {"Content-Type":"application/json"}

# this is used to get the auth token from the API POST
response = requests.post(LogonURL, data=payload, json=headers, verify=False)

# save authToken to authKey variable
authKey = response.text.strip('\"')

# set the account ID of the account to Reconcile password for (can be obtained with POSTMAN)
accID = "21_5"

# set the PasswordReconcile URL
PassReconcileURL = str(PVWA) + "/API/Accounts/" + accID + "/Reconcile"
headers = {'Authorization': str(authKey),'Content-Type': "application/json"}
response = requests.request("POST", PassReconcileURL, headers=headers, verify=False)

print(response.text)

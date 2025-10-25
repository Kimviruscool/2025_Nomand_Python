from requests import get

website = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
)

result = {}

for website in website:
    if not website.startswith("https://") :
        website = f"https://{website}"
    response = get(website);
    if response.status_code == 200:
        result[website] = "OK"
    else :
        result[website] = "FAILED"

print(result)
    # .status_code : 통신상태만 확인

#1XX : Information responses
# 2XX : Successful responses
# 3XX : Redirection messages
# 4XX : Client error responses
# 5XX : Server error reponses
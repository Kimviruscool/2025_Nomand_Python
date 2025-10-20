#반복문

website = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
)

print(website[1]);

for website in website:
    if not website.startswith("https://") :
        website = f"https://{website}"
    print(website);
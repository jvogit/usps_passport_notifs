# USPS Passport Checker
Check for available appointment by USPS post office. If available, then send an email.

# Requirements
.env 
```
OUTLOOK_USERNAME=outlook email address to send from
OUTLOOK_PASSWORD=outlook email password
FDB_ID=post office id. Found by inspecting network requests in the USPS passport site for desired passport processing office.
RECIPIENT_EMAIL=where to send the notification email to
```

json_payload - currently set to find appointment for 1 minor. Change for desired settings.

# Docker
1. Set .env/environment variables
2. `docker build .`
3. `docker run`

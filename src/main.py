import smtplib
import email.message
import requests
import dotenv
import os

def main():
    dotenv.load_dotenv()
    outlook_email = os.environ.get("OUTLOOK_USERNAME")
    outlook_password = os.environ.get("OUTLOOK_PASSWORD")
    fdbId = os.environ.get("FDB_ID")
    recipient_email = os.environ.get("RECIPIENT_EMAIL")

    json_payload = {
        "numberOfAdults": "0",
        "numberOfMinors": "1",
        "fdbId": f"{fdbId}",
        "productType": "PASSPORT",
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    req = requests.post(
        "https://tools.usps.com/UspsToolsRestServices/rest/v2/appointmentDateSearch",
        json=json_payload,
        headers=headers,
    )

    response = req.json()

    if not response['dates']:
        exit()

    with smtplib.SMTP(host="smtp-mail.outlook.com", port=587) as outlook:
        outlook.ehlo('mylowercasehost')
        outlook.starttls()
        outlook.ehlo('mylowercasehost')
        outlook.login(outlook_email, outlook_password)
        
        m = email.message.Message()
        m['From'] = outlook_email
        m['To'] = recipient_email
        m['Subject'] = "USPS Passport Available"
        m.set_payload("\n".join((str(response), "https://tools.usps.com/rcas.htm")))

        outlook.sendmail(outlook_email, recipient_email, m.as_string())
        outlook.quit()


if __name__ == "__main__":
    main()

import requests

url = "https://microsoft-translator-text.p.rapidapi.com/translate"

languages = {"Spanish": "es", "German": "de", "French": "fr", "English": "en"}

text = input("\nEnter the text to be translated : ")

lan2 = input("Enter the conversion language : ").capitalize()

querystring = {"to[0]": languages[lan2], "api-version": "3.0", "profanityAction": "NoAction", "textType": "plain"}

payload = [{"Text": text}]

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com",
    "X-RapidAPI-Key": "e228ed9bcdmsha1fc0c3f1222c75p1d3eafjsn15f97a40c083"
}

response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

print(f"\nDetected Language : {list(languages.keys())[list(languages.values()).index(response.json()[0]['detectedLanguage']['language'])]}")
print(f"Translated Text : {response.json()[0]['translations'][0]['text']}")
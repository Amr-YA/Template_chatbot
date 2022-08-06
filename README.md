# Template Chatbot
A sample project using Rasa framework to build a chatbot with interactive elements.
If bot is deployed to a FB page or Whatsapp, the Bot can respond in 3 ways
- Text message only
- Text message with buttons
- Text message with quick replies
# Running the service:
## Building
You can build the dockerfile in the repo with the following commands:
```
docker build -t temp_bot .
```

## Running
Start the service frjom the build docker image:
```
docker run --rm -p 5005:5005 -t temp_bot
```

# APIs to interact with the Bot:
## Send
To send any message to the bot you can use the example request below:
```
response = requests.post("http://localhost:5005/webhooks/rest/webhook", json={"sender": "as0123",
 										                                      "message": "text"})
```

## Replies
response is expected to be like:
```
[
    {
        "recipient_id": "as0123",
        "text": "message",

        "buttons": [
            {
                "payload": "button_1",
                "title": "one"
            },
            {
                "payload": "button_2",
                "title": "two"
            },
            {
                "payload": "button_3",
                "title": "three"
            }
        ],

        "buttons": [
            {
                "content_type": "text",
                "payload": "qr_1",
                "title": "one"
            },
            {
                "content_type": "text",
                "payload": "qr_2",
                "title": "two"
            },
            {
                "content_type": "text",
                "payload": "qr_3",
                "title": "three"
            },
            {
                "content_type": "text",
                "payload": "qr_4",
                "title": "four"
            },
            {
                "content_type": "text",
                "payload": "qr_5",
                "title": "five"
            },
            {
                "content_type": "text",
                "payload": "qr_6",
                "title": "six"
            }
        ]

    }
]
```

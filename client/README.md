# RatingApp

RatingApp is an application used by raters to rate ads.
A task is an object containting an ad, a description of this ad and what we want to rate (quality of the ad, relevance of the description, how interesting is the ad to the user...).
This app fetches a task, displays it so the user can rate it and sends back the results. 

It is compatible with Windows, Linux, MacOS, and smartphones as well (Android, iOS).

## Requirements
Python 3.7

### Server

uvicorn 0.13.4

```bash
pip install uvicorn
```

### Client
Kivy 2.0.0 

```bash
pip install kivy
```

## Usage

To run the server, run the following command from the server folder on your terminal.

```
unicorn server_api:app --reload
```

To run the client, run the following command from the client folder on your termnal:

```
python controller.py 
```


2 simple tests are also included in test folder.

To run the test, run the following command from the client folder on your teminal:

```
pytest test/test_cases.py

```

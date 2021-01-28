# RatingApp

RatingApp is an application used by raters to rate ads.
A task is an object containting an ad, a description of this ad and what we want to rate (quality of the ad, relevance of the description, how interesting is the ad to the user...).
This app fetches a task, displays it so the user can rate it and sends back the results. 

It is compatible with Windows, Linux, MacOS, and smartphones as well (Android, iOS).

## Requirements
Kivy 2.0.0 

To install Kivy visit the installation [page](https://kivy.org/doc/stable/gettingstarted/installation.html#installation-canonical) or use the following command.

```bash
pip install kivy
```

## Usage

To run the app, simply run the following command on your terminal.

```
python controller.py
```

2 simple tests are also included in test folder. 
To run the test, run the following command on your teminal in the current directory.

```
pytest test/test.py
```
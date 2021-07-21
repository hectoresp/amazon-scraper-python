## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info

This program scrapes anything from Amazon. You can specify the type of article you want and it will scrape it for you.

Note: This program only works with Amazon ES and EURO. Please do not change the Amazon URL to another country because it won't work.

## Technologies

To execute the code you'll need the following packages:

- Selenium 3.141.0

```
$ pip install selenium
```
Selenium is used in this program to go to the URL and scrape the information.

- Argparse 1.4.0

```
$ pip install argparser
```
Argparser is used to parse the search you want to make.

- Plyer 2.0.0

```
$ pip install plyer
```
Plyer is used to show notifications.

- Xlsxwriter 1.4.4

```
$ pip install Xlsxwriter
```

## Setup

To execute this program go to your console and type the following line:
```
$ python main.py -s your_search
```


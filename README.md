## Table of contents
* [Simple Watermark App (Project title)](#watermark-app)
* [App info](#app-info)
* [Usage Example](#usage-example)
* [Technologies](#technologies-requirements)
* [Pending changes](#pending-changes)
* [Setup](#setup)

# Watermark App
Simple GUI application,using Tkinter and Pillow,where a user can place a watermark on his favourite photo

## App info
Some useful information about the application:
* The user can upload his desired photo in various formats
* The original photo is resized to fit the dimensions of the GUI App Frame
* The user can either place a Logo watermark or Text watermark or both on the selected image
* The user can download the edited photo on the Frame

## Usage Example
A brief example of the GUI App is demonstrated below:
![Alt text](/images/original_photo.png "Before watermark")
![Alt text](/images/original_photo.png "After watermark")


## Technologies - Reqirements
Project is created with:
* Python version: 3.10.2
* PyCharm version: 2021.3.2 (Community Edition)
* Runtime version: 11.0.13+7-b1751.25 amd64
* Pillow==9.5.0

## Pending changes
Some of major changes to be done:
* The App is over simple and doesn't allow watermark customizations (e.g. colors, directions,angles etc)
* Save Photo operation saves the photo at the current resized dimensions
* Undo Operations and exception handling need to be done 

## Setup
To run this project,you must have installed python version 3.6+.You can run the project from simple python console or import it in PyCharm.
To run the project from the cmd console,first download the project, extract it to your desired directory and follow the commands:

```
$ cd ../path-to-main-py-file
```
```
$ python main.py
```
Hope you enjoy it 🧡

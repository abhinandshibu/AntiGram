# AntiGram
A simple web application designed as a CTF (capture the flag) to increase awareness about security vulnerabilities.

## Contents
* [Purpose](#purpose)
* [Setup](#setup)
* [Purpose](#purpose)
* [Vulnerabilities (answers)](#vulerabilities-(answers))
* [License](#license)

## Purpose

Capture the flag is a game where the objective is to find and exploit vulnerabilities to get to an end goal. AntiGram is a CTF and a simple web application that has multiple vulnerabilities (the answers can be found below). The purpose of this game is to increase awareness about specific vulnerabilities in order to prevent developers making these errors, which increases the security of software in general.

## Setup

### Mac OS example
#### Clone the repository
```
git clone https://github.com/abhinandshibu/AntiGram.git
```

#### Navigate into the directory of the repository
```
cd AntiGram
```

#### Create a virtual environment and install the requirements
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

#### Run it
```
FLASK_APP=antigram.py
flask run
```

## Vulnerabilities (answers)

Below are the answers to the CTF, please try to find these vulnerabilities yourself first.


## License

Copyright © 2020 Abhinand Shibu

This project is licensed under the [MIT License](/LICENSE).

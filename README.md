# Genetic Algorithm Based Pattern Matcher

A Simple (Flask app) demonstration of Genetic Algorithm

## Pre-requisites
- Python - https://www.python.org/downloads
- Pip - https://pip.pypa.io/en/stable/installing
- Flask - http://flask.pocoo.org/docs/1.0/installation

## Install necessary packages

`pip install -r requirements.txt`

## Run Flask's Development server

`python app.py`

## Overview

- The application takes an `input_string` as 
input in HTTP request. 

- The input string is given as an input to
a custom implementation of Genetic Algorithm.

- The resultant HTML output shows the steps and generations
tried by the Genetic Algorithm along with a
line chart.

- We can infer from the line chart that
as the **generation** keeps increasing, 
the **Fitness Score** also increases

## Available endpoints:
`GET /?input_string='example_string'`

## Resources

For a more detailed explanation
on Genetic Algorithm and it's working,
have a look at [our powerpoint presentation](https://docs.google.com/presentation/d/1JWc_9xtpcCP1g5bY2LBn3wZ3UQSYo1NirBEJID0wxSA/edit?usp=sharing).

# App Engine Starter

A template for App Engine projects. [Demo](https://united-tempest-196023.appspot.com/) (not much to see).

**Uses**: [webapp2](https://webapp2.readthedocs.io/en/latest/), [Python 2.7](https://docs.python.org/2/), [Bootstrap v4.0.0-alpha.6](https://v4-alpha.getbootstrap.com/getting-started/introduction/).

Hosted on [Google App Engine](https://cloud.google.com/appengine/).

# Usage

## How to start the dev server

**Google Cloud SDK must be installed.**

1. Open shell in the directory containing "app.yaml"

2. Run `dev_appserver.py app.yaml`

3. Go to [http://localhost:8080](http://localhost:8080). The admin console can be accessed at [http://localhost:8000/](http://localhost:8000/).

## How to push changes to App Engine

If Google Cloud SDK is configured to this project:

1. Open shell in the directory containing "app.yaml"

2. Run `gcloud app deploy`

If Google Cloud SDK is not configured to this project you can switch to it with

    `gcloud config set project PROJECT_ID`

### References

This template was developed during Udacity's [Intro to Programming nanodegree](https://www.udacity.com/course/intro-to-programming-nanodegree--nd000). Some of the code was given, some of it I added later on. My [website](https://www.wsundine.com/) was built off a template like this.

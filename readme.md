# App Engine Starter

A template for App Engine projects. [Demo](https://united-tempest-196023.appspot.com/) (not much to see).

**Built with**:
- [Bootstrap v4.0.0-alpha.6](https://v4-alpha.getbootstrap.com/getting-started/introduction/)
- [Jinja2](http://jinja.pocoo.org/docs/2.10/)
- [Python 2.7](https://docs.python.org/2/)
- [webapp2](https://webapp2.readthedocs.io/en/latest/)

Hosted on [Google App Engine](https://cloud.google.com/appengine/).

# Usage

First off, go to [Google Cloud Console](https://console.cloud.google.com/) and create a new project. Then install the [Google Cloud SDK](https://cloud.google.com/sdk/).

## How to start the dev server

1. Open shell in the directory containing "app.yaml"

2. Run `dev_appserver.py app.yaml`

3. Go to [http://localhost:8080](http://localhost:8080).

The admin console can be accessed at [http://localhost:8000/](http://localhost:8000/).

## How to push changes to App Engine

If Google Cloud SDK is set to this project:

1. Open shell in the directory containing "app.yaml"

2. Run `gcloud app deploy`

If Google Cloud SDK is not set to this project you can switch to it with

```bash
    gcloud config set project PROJECT_ID
```

# Misc

### Why Python 2?

Because Python 3 is not supported by the [App Engine Standard Environment](https://cloud.google.com/appengine/docs/standard/). The standard environment is cheaper than the flexible environment (standard is free within limits). However, it's been a few years since I last checked App Engine's pricing so this might have changed.

### References

This template was developed during Udacity's [Intro to Programming nanodegree](https://www.udacity.com/course/intro-to-programming-nanodegree--nd000). Some of the code was given, some of it I added later on. My [website](https://www.wsundine.com/) was built off a template like this.

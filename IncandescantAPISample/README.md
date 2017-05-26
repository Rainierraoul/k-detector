# Incandescant API Sample

## Goals
This goal of this small Node app was to try out the Incandescant Reverse Image Search API. The IncandescantAPI performs image lookups on ppopular services and returns the websites using that image.
The purpose of finding those websites was to see if its possible to know who the person is in the photo.
IncandescantAPI does not do any facial recognition, just an image lookup comparison against sites, but it may yield some results.

## Technologies used
* Node
* [node-incandescent-client](https://github.com/AaronHammond/node-incandescent-client)
* AWS S3

## Tasks undertaken
* Created a IncandescantAPI account to get the API key.
* Created a new node app importing the necessary node modules.
* Upload the profile image to AWS S3 to get a public URL to be used by the app.
* Run the app and evaluate the returned data.

# What was found out
IncandescantAPI does a lookup against a number of popular websites to get some data, providing URLs, source locations, and the image compared against.

JSON object returned from API;
```
instagom.com:
  pages:
    2:
      page:         http://instagom.com/explore/tags/letsgosomewhere
      base64_page:  aHR0cCUzQSUyRiUyRmluc3RhZ29tLmNvbSUyRmV4cGxvcmUlMkZ0YWdzJTJGbGV0c2dvc29tZXdoZXJl
      source:       google
      date:         1495763084
      usage-image:  http://scontent-amt2-1.cdninstagram.com/t51.2885-19/s150x150/13285521_651817998299645_1265590597_a.jpg
      usage-height: 150
      usage-width:  150
      image:        https://s3-us-west-2.amazonaws.com/incandescantapisample/andy.jpg
      iid:          407173
```

The data returned does not reveal much about the profile, and can be very hit and miss. For example, the profile image for Joost returned his github account, whereas the profile of Andy returned a lot of account that he publicly follows on social media sites. Making it hard to know if its him or someone else.

## Recommendations
The reverse image lookup is not proving us with a result to fill the unknown identified person. We may want to look elsewhere, such as Facebook API's to get a persons profile from image tagging capabilities.

# Getting up and running
To get this little app up and running make sure you have Node and NPM installed.

1. Make an account on [IncandescantAPI](http://incandescent.xyz/)
2. Clone this repo
3. `$ touch .env`
4. Copy your `uid=` and `api_key=` to the `.env` file
5. `$ npm install` to install the node modules
3. `$ npm start` to start the app

To search for a different image just replace the URL of the image on line 11.

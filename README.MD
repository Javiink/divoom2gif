# Divoom2gif

This utility will download the latest animations from Divoom and save them as gif files!

## Setup

You should copy the `docker-compose.example.yml` file to `docker-compose.yml` and fill your account details and download preferences. There's not much to do.
Then, just launch the container with `docker-compose up`. This should build the image, start the container and start downloading the animations!

## Todo

- [ ] Ability to download a particular animation

## Credits

This is a very basic usage of the [@redphx's APIxoo](https://github.com/redphx/apixoo/) Divoom library for python.

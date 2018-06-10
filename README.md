# Auto-Screenshots

Generates perceptual diff of a git repository as you make pull requests.

## Installation

### Manual Installation

**System Requirements**<br />

Download and install the following:<br />
[Python 2](https://www.python.org/downloads/) w/ pip installed<br />
[Node](https://nodejs.org/en/) w/ yarn installed<br />
[Redis](https://redis.io/)<br />
[PostgreSQL](https://www.postgresql.org/)<br />
  ```postgres
  CREATE DATABASE garnish_db
  CREATE USER garnish_user WITH LOGIN PASSWORD 'garnish'
  ```
[PhantomJS](http://phantomjs.org/)<br />

**Python and NodeJs Packages**<br />
```
$ pip install -r requirements.txt
$ yarn install
```

### Docker Installation
Make sure to set up PostgreSQL:
```postgres
CREATE DATABASE garnish_db
CREATE USER garnish_user WITH LOGIN PASSWORD 'garnish'
```

Run Docker:
```
docker run build .
docker run -it <JUST_GENERATED_DOCKER_BUILD_HASH> bash
```

## Setup

### Environment Variables
*All manage.py commands will need the proper environment variables set to run properly*

The Github Repository that you are testing for:
```
GIT_REPO='YOUR_GITHUB_USERNAME/YOUR_GITHUB_REPO'
```

Your Github [personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/):
```
GIT_OAUTH='YOU_AUTH_ID_HERE'
```

The name of the directory in the Git Repository that stores the state representation JSON files. See [this folder](https://github.com/MingDai/kolibri/tree/test-master/states) for example:
```
STATES_FOLDER='NAME_OF_YOUR_STATES_FOLDER'
```

Set what screen capture tools and resolutions you want. Add the screenshot configuration file to root of this directory. See [this file](https://github.com/MingDai/HookCatcher/blob/develop/HookCatcher/config.json) for example:
```
SCREENSHOT_CONFIG='PATH_TO_YOUR_CONFIG_FILE'
```

Specify the port that is running Redis (defaults to 6379):
```
REDIS_PORT='REDIS_PORT_NUMBER'
```

Specify the port that is running PostgreSQL (defaults to 5432):
```
POSTGRES_PORT='POSTGRES_PORT_NUMBER'
```


**Optional:**<br />
If you are planning to use BrowserStack API, specify your username:
```
BROWSERSTACK_USERNAME='YOUR_BROWSERSTACK_USERNAME'
```

Also specify your BrowserStack OAUTH [access key](https://www.browserstack.com/accounts/settings):
```
BROWSERSTACK_OAUTH='YOUR_BROWSERSTACK_ACCESS_KEY'
```



**Production:**<br />
Provide a Django Secret Key environment variable:
```
DJANGO_SECRET_KEY='YOUR_PRODUCTION_KEY'
```

### Start the server
1. Open a new window and start Redis by running the command `$ redis-server`

2. From the root, navigate into the *HookCatcher* directory `$ cd Hookcatcher/`

3. Open how ever many more windows and start a Redis Queue worker on each `$  python manage.py rqworker default`

4. To start the server, run
`$ python manage.py runserver (port)`
NOTE: port defaults to 8000

To view site enter the following website url into your browser:
http://127.0.0.1:8000/


## Command Line Tools
In the root of this directory utilize the following Django commands.

#### Generate screenshots and take Image Diffs of a Github Pull Request
NOTE: you must run redis-server before you run the auto-screenshot command
```
$ python manage.py auto-screenshot <Github Pull Request Number>
```

#### Generate a full-page screenshot of a url using PhantomJS
```
$ python manage.py simpleGetScreenshot <URL> <Image Name>
```

#### Generate a perceptual diff between two images using ImageMagick
```
$ python manage.py simpleGetDiff <Image Name 1> <Image Name 2> <Resulting Diff Name>
```

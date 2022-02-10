# Stryktipset


## Setup
*Make sure you have at least python 3.6.0 installed*<br>
*Make sure you have chrome installed*<br>
*Make sure you have a g++ (and/or make) installed<br>

Navigate into to project, create an environment, activate it, and install the required packages
<pre>
python3 -m venv env
</pre>
<br></br>
<b>Activate environment:</b> <br>
Windows:
<pre>source env/Scripts/activate </pre>
<b><i>Or</i></b><br>
Unix/MacOS:
<pre>source env/bin/activate </pre>
<br></br>
<b>Install packages</b>
<pre>python3 -m pip install -r requirements.txt</pre>
<br></br>
Create a file named "config.cfg" and fill in the following (example can be found at "config.cfg.example"):
```
{
    "headless" : true,
    "login_op" : {
        "username" : "YOU'R USERNAME TO ODDS PORTAL",
        "password" : "YOU'R PASSWORD TO ODDS PORTAL"
    },
    "login_stl" : {
        "email" : "YOU'R EMAIL TO STRYKTIPSETETLEAGUE",
        "password" : "YOU'R PASSWORD TO STRYKTIPSETETLEAGUE"
    },
    "sleep_time" : 60,
    "output-email": {
        "from": "DESIRED OUTPUT EMAIL ADDRESS",
        "server": "EMAIL SERVER,
        "port": FORT TO EMAIL SERVER,
        "password": "EMAIL SERVER PASSWORD",
        "to": ["EMAIL ADDRESS TO SEND TO"]
    }
}
```
<br>

## Run
From the top folder simply run:
```
make
python3 ./main.py
```

## Notes
* When compiling dijkstras remember to compile for 64 but systems in order to not run out of memory at runtime. (see make-file)

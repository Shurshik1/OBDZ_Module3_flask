from flask import Flask, render_template, g
import random
from datetime import datetime
import pytz

### Make the flask app
app = Flask(__name__)

### Routes
@app.route("/time")
def get_time():
    now = datetime.now().astimezone(pytz.timezone("US/Central"))
    timestring = now.strftime("%Y-%m-%d %H:%M:%S")  # format the time as a easy-to-read string
    beginning = "<html><body><h1>The time is: "
    ending = "</h1></body></html>"
    return render_template("time.html", timestring=timestring)

@app.route("/random")
def pick_number():
    n = random.choices(['Name - Serhiy', 'Surname - Vasyliev', 'Group and ID - KID-21'], [1, 1, 1], k=1)
    return render_template("random.html", number=n)

@app.route("/")
def hello_world():
    return "Hello, world!"  # Whatever is returned from the function is sent to the browser and displayed.
  
@app.cli.command("initdb")
def init_db():
    """Clear existing data and create new tables."""
    conn = get_db()
    cur = conn.cursor()
    with current_app.open_resource("schema.sql") as file: # open the file
        alltext = file.read() # read all the text
        cur.execute(alltext) # execute all the SQL in the file
    conn.commit()
    print("Initialized the database.")

@app.cli.command('populate')
def populate_db():
    conn = get_db()
    cur = conn.cursor()
    with current_app.open_resource("populate.sql") as file: # open the file
        alltext = file.read() # read all the text
        cur.execute(alltext) # execute all the SQL in the file
    conn.commit()
    print("Populated DB with sample data.")

@app.route("/dump")
def dump_entries():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('select id, date, title, content from entries order by date')
    rows = cursor.fetchall()
    output = ""
    for r in rows:
        debug(str(dict(r)))
        output += str(dict(r))
        output += "\n"
    return "<pre>" + output + "</pre>"

### Start flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

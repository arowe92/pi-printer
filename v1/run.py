from datetime import datetime, timedelta
import time
from escpos.printer import Usb
import subprocess
from weather import Weather, Unit
import todoist
import pystache
import pprint
print = pprint.PrettyPrinter(indent=1).pprint

api = todoist.TodoistAPI('a8d1ca7cac05c34bd77d38787d0b402eed3ba9a2')
api.sync()

# Get all Items overdue or due today
cal_items = []
todo_items = []
todo_week = []

now = datetime.now().date()

# Iterate through all items
for item in api.items.all():
    due_date = item.data['due_date_utc']
    if due_date is None:
        continue

    # Format the date
    date = datetime.strptime(due_date, '%a %d %b %Y %H:%M:%S %z')

    # Get Those labels
    # add to calendar if necessary
    if 'GCal' in [
        label for label in map(
            lambda l: api.labels.get(l)['label']['name'],
            item.data['labels']
        )]:
        if now == date.date():
            cal_items += [item.data]
            string = date.strftime("%I:%M %p").lower()
            if string[0] == '0':
                string = string[1:]

            item.data['due_date'] = string

        continue

    # Project Name
    project = api.projects.get(item.data['project_id'])['project']['name']
    if project == 'Inbox':
        project = ''

    item.data['project_name'] = project

    if now >= date.date():
        todo_items += [item.data]

    elif now + timedelta(days=27) >= date.date():
        item.data['due_date'] = date.strftime('%a')
        todo_week += [item.data]

# get weather
weather = Weather(unit=Unit.FAHRENHEIT)
location = weather.lookup_by_location('austin')
weather = {
    'high': location.forecast[0].high,
    'low': location.forecast[0].low,
    'text': location.forecast[0].text,
    'status':location.forecast[0].text.lower().replace(' ', '-')
}
# Read in template
with open('template.ms', 'r') as f:
    template = f.read()

# Write output
with open('output.html', 'w') as f:
    f.write(pystache.render(template, {
        'cal_items': cal_items,
        'todo_items':todo_items,
        'todo_week': todo_week,
        'weather': weather,
        'day': now.strftime("%A"),
        'date': now.strftime("%B %d, %Y")
    }))

#  Start web server cap
url = 'http://localhost:9000/output'
# url = 'file:///home/alexrowe/Projects/escpos/output.html'
output = 'output.png'
proc = subprocess.Popen(['harp', 'server'])

# Screen cap
time.sleep(2)
subprocess.call(['phantomjs', 'cap.js', url, output])

# Kill Process
proc.terminate()
proc.wait()

p = Usb(0x0416, 0x5011)
p.image('output.png')
p.text('\n')
p.cut()

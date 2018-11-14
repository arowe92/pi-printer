from datetime import datetime, timedelta
import pytz
import todoist

from . util import Provider


class TodoProvider(Provider):

    template = 'todo'

    def __init__(self, key='a8d1ca7cac05c34bd77d38787d0b402eed3ba9a2'):
        self.api = todoist.TodoistAPI(key)
        self.api.sync()

    def get_data(self):
        # Get all Items overdue or due today
        cal_items = []
        todo_items = []

        now = datetime.now().astimezone(tz=None)

        # Iterate through all items
        for item in self.api.items.all():
            project = self.api.projects.get(item.data['project_id'])['project']['name']
            due_date = item.data['due_date_utc']

            # let inbox entries continue through
            if project == 'Inbox' and due_date is None:
                due_date = datetime.now()

            # We only want ones with due dates
            if due_date is None or item.data['date_completed'] is not None:
                continue

            # Format the datetime if needed
            if type(due_date) is str:
                due_date = datetime.strptime(due_date, '%a %d %b %Y %H:%M:%S %z')

            due_date = due_date.astimezone(tz=None)
            item.data['date_obj'] = due_date

            if now.date() + timedelta(days=5) <= due_date.date():
                continue

            # Get Those labels
            # add to calendar if necessary
            labels = list(map(
                lambda l: self.api.labels.get(l)['label']['name'],
                item.data['labels']
            ))
            # Get Calendar items that are TODAY
            if 'GCal' in labels:
                if now.date() != due_date.date():
                    continue

                # Add to list
                cal_items += [item.data]

                # Get the time
                string = due_date.strftime("%I:%M %p").lower()

                # Remove leading 0
                if string[0] == '0':
                    string = string[1:]

                item.data['due_date'] = string

                continue

            # Project Name
            if project == 'Inbox':
                project = ''

            # Add properties
            if due_date.date() < now.date():
                string = 'overdue'
            elif due_date.date() == now.date():
                string = ''
            else:
                string = due_date.strftime('%a')

            item.data['due_date'] = string
            item.data['project_name'] = project
            todo_items += [item.data]

        todo_items.sort(key=lambda x: x['date_obj'])
        cal_items.sort(key=lambda x: x['date_obj'])

        return {
            'cal_items': cal_items,
            'cal_items_length': len(cal_items),
            'todo_items': todo_items,
        }

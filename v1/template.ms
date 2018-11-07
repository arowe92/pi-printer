<head>
    <link rel='stylesheet' href='main.css' />
    <link rel='stylesheet' href='weather-icons.css' />
</head>
<body>

<h1>
    <span id='day'>{{day}}</span>
    <span id='date'>{{date}}</span>
</h1>

{{#weather}}
    <div id='weather'>
        <span id='status'>
            {{text}},
        </span>
        <span id='temp'>{{low}}°↓ {{high}}↑°</span>
        <!-- <i class='wi wi-day-{{status}}'></i> -->
    </div>
{{/weather}}

<h2> Todo </h2>
<ul>
{{#todo_items}}
<li>
    <span>{{content}}</span>
    {{^all_day}}
        <span id='due-date'>{{due_date}}</span>
    {{/all_day}}
</li>
{{/todo_items}}
</ul>

<h3> This Week </h3>
<ul>
{{#todo_week}}
<li>
    <span>{{content}}</span>
    <span id='due-date'>{{due_date}}</span>
</li>
{{/todo_week}}
</ul>

<h2>Calendar</h2>
<ul>
{{#cal_items}}
<li>
    <span>{{content}}</span>
    {{^all_day}}
        <span id='due-date'>{{due_date}}</span>
    {{/all_day}}
</li>
{{/cal_items}}
</ul>

</body>

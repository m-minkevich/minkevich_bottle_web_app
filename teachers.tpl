<html>

<style>
    #navbar a {
        color: white;
        text-decoration: none;
        margin-right: 16px;
        font-weight: bold;
    }
</style>

<div id="navbar" style="background-color: black; margin: 0px; padding: 16px; display: flex;">
    <a href="/">Students</a>
    <a href="/teachers">Teachers</a>
    <a href="/workload.png">Workload</a>
    <div style="flex: 1;"></div>
    <a href="/new-teacher">Create New Teacher</a>
</div>

<head>

</head>
<body style="margin: 0px; font-family: Arial, Helvetica, sans-serif;">
 
%for row in rows:
<div style="background-color: lightgray; margin: 8px; padding: 16px;">
    <p>First Name: <b>{{row[1]}}</b></p>
    <p>Last Name: <b>{{row[2]}}</b></p>
    <p>Id: {{row[0]}}</p>
    <div style="display: flex;">
        <form action="/delete-teacher-{{row[0]}}" method="get">
         <input type="submit", name="delete", value="Delete", style="background-color: red; border-radius: 4px">
        </form>
    </div>
</div>
%end
    
</body>

</html>
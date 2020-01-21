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
    <div style="flex: 1;"></div>
    <a href="/new-teacher">Create New Teacher</a>
</div>

<head>

</head>
<body style="margin: 0px; font-family: Arial, Helvetica, sans-serif;">
 
%for row in rows:
<div style="background-color: wheat;">

    <div style="background-color: chartreuse;">
        <p>First Name: {{row[1]}}</p>
    </div>
    <div style="background-color: coral;">
        <p>Last Name: {{row[2]}}</p>
    </div>
    <div>
        <p>Id: {{row[0]}}</p>
    </div>
    <form action="/{{row[0]}}" method="get">
        <input type="submit", name="select", value="Select">  
    </form>
    <form action="/delete-teacher-{{row[0]}}" method="get">
        <input type="submit", name="delete", value="Delete">
    </form>
    
</div>
%end
    
</body>

</html>
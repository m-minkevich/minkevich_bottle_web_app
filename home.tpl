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
        <div style="flex: 1;"></div>
        <a href="/new-student">Create New Student</a>
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
        <input type="submit", name="update", value="Update">
        <input type="submit", name="delete", value="Delete">
      </form>
</div>
%end
    
%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>The open items are as follows:</p>
<table border="1">
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  </tr>
%end
</table>


</body>
</html>
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
        <a href="/new-project">Create New Project</a>
    </div>

<head>

</head>
<body style="margin: 0px; font-family: Arial, Helvetica, sans-serif;">
    





    %for row in rows:
      <div style="background-color: wheat; padding: 24px;">
      
        <form action="/{{row[0]}}" method="get">
          <button type="submit">Select</button>
          <a>{{row[1]}} created by {{row[2]}}</a>
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
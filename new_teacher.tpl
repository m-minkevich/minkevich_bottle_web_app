% rebase('base_home_navbar.tpl')

<form action="/teachers" method="GET">
    <fieldset>
        <legend>New Teacher Creation Form</legend>
        <p><label class="field" for="name"></label>First Name: <input type="text", placeholder="Enter first name", maxlength="100", name="first_name",></p>
        <p><label class="field" for="name"></label>Last Name: <input type="text", placeholder="Enter last name", maxlength="100", name="last_name",></p>
        <input type="submit", name="save", value="save">
    </fieldset>
</form>

<body style="margin: 0px; font-family: Arial, Helvetica, sans-serif;">
    
</body>
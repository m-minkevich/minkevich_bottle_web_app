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
    </div>

<form action="/" method="GET">
    <fieldset style="margin: 24px;">
        <legend>New Student Creation Form</legend>
        <p><label class="field" for="name"></label>First Name: <input type="text", placeholder="Enter first name", maxlength="100", name="first_name",></p>
        <p><label class="field" for="name"></label>Last Name: <input type="text", placeholder="Enter last name", maxlength="100", name="last_name",></p>
        <!-- <p><label class="field" for="name"></label>Age group
            <select id="age-select">
            <option value="">--Please choose an option--</option>
            <option value="small">Small</option>
            <option value="medium">Medium</option>
            <option value="big">Big</option>
            </select>
        </p> -->
        <input type="submit", name="save", value="save">
    </fieldset>
</form>

<body style="margin: 0px; font-family: Arial, Helvetica, sans-serif;">
    
</body>
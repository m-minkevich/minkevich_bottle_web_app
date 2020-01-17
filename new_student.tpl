% rebase('base_home_navbar.tpl')

<div style="background-color: wheat; padding: 24px;">
    Here is my project overview

</div>

<form action="/" method="GET">
    <fieldset>
        <legend>New Student Creation Form</legend>
        <p><label class="field" for="name"></label>First Name: <input type="text", placeholder="Enter first name", maxlength="100", name="first_name",></p>
        <p><label class="field" for="name"></label>Last Name: <input type="text", placeholder="Enter last name", maxlength="100", name="last_name",></p>
        <p><label class="field" for="name"></label>Date of Birth: <input type="text", placeholder="Enter the date of birth", maxlength="100", name="birth",></p>
        <p><label class="field" for="name"></label>Age group
            <select id="age-select">
                <option value="">--Please choose an option--</option>
                <option value="small">Small</option>
                <option value="medium">Medium</option>
                <option value="big">Big</option>
            </select>
        </p>
        <input type="submit", name="save", value="save">
    </fieldset>
</form>

<body style="margin: 0px; font-family: Arial, Helvetica, sans-serif;">
    
</body>
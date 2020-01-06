% rebase('base.tpl', title='Page Title')

<div style="background-color: wheat; padding: 24px;">
    Here is my creation form

    <form action="/create-subject" method="GET">
        <input type="text" placeholder="Enter name" style="height: 30px;" name="subject">
        <button type="submit" style="height: 30px;" name="save" value="save">Create Subject</button>
    </form>

</div>
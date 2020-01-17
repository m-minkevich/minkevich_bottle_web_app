% rebase('base.tpl', title='Page Title')

<div style="background-color: wheat; padding: 24px;">
    Here is my creation form

    <form action="/{{no}}/subjects" method="GET">
        <input type="text" placeholder="Enter the name of the subject" style="height: 30px;" name="subject">
        <input type="text" placeholder="Number of places" style="height: 30px;" name="places">
        <button type="submit" style="height: 30px;" name="save" value="save">Create Subject</button>
    </form>

</div>

%for row in rows:
    <div style="background-color: burlywood;">
         <div style="background-color: cadetblue; padding: 12px;">
            {{row[0]}}
        </div>
        <div style="background-color: chartreuse; padding-left: 12px; padding-right: 12px">
        Number of available places: {{row[1]}}
        </div>
    </div>
%end




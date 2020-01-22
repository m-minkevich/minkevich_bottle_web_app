% rebase('base.tpl', title='Page Title')

<div style="padding: 24px;">
    <p>You have selected <b>{{result[0][0]}} {{result[0][1]}}</b></p>
</div>

%for row in rows:
<div style="display: flex; padding: 12px; align-items: center; margin: 8px;">
  <form action="/save-lesson-for-{{row[0]}}-{{student_id}}" method="GET">
    <fieldset>
        <legend>{{row[1]}} {{row[2]}}</legend>
        <p><label class="field" for="name"></label>Number of lessons: <input type="text", placeholder="hours", maxlength="100", name="hours", value={{row[3]}}></p>
        <input type="submit", name="save", value="save">
    </fieldset>
  </form>
</div>
%end



{% extends 'index.pat' %}

{% block css %}
{{ super() }}
<link href="/css/froala_editor.min.css" rel="stylesheet" type="text/css" />
<link href="/css/froala_style.min.css" rel="stylesheet" type="text/css" />
{% endblock css %}


{% block content %}
<form action="/do_newpost" method="post">
    <input type="text" class="form-control" placeholder="Title" name="title">
    <textarea id="edit" name="article"></textarea>
    <input type="submit" value="Save Post">
</form>
{% endblock content %}


{% block js %}
{{ super() }}
<!-- Include JS files. -->
<script src="js/froala_editor.min.js"></script>

<!--[if lt IE 9]>
    <!-- Include IE8 JS. -->
    <script src="js/froala_editor_ie8.min.js"></script>
<![endif]-->

<!-- Initialize the editor. -->
<script>
    $(function() {
        $('#edit').editable({inlineMode: false})
    });
</script>
{% endblock js %}

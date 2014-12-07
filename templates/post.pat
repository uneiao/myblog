{% extends 'index.pat' %}

{% block header %}
    <!-- Page Header -->
    <!-- Set your background image for this header on the line below. -->
    <header class="intro-header" style="background-image: url('/img/lx4.jpg')">
        <div class="container">
            <div class="row">
                <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
                    <div class="post-heading">
                        <h1>{{ post.title }}</h1>
                        <h2 class="subheading">{{ post.subtitle }}</h2>
                        <span class="meta">Posted by <a href="#">{{ post.owner }}</a> on {{ post.upload_time | string }}</span>
                    </div>
                </div>
            </div>
        </div>
    </header>
{% endblock header %}

{% block content %}
    <!-- Post Content -->
    <article>
        <div class="container">
            <div class="row">
                <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
                    {{ post.article }}
                </div>
            </div>
        </div>
    </article>

    <hr>
{% endblock content %}

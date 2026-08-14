{% extends "mail_templated/base.tpl" %}

{% block subject %}
Email Verification
{% endblock %}

{% block html %}
<h1>Hello {{ user.email }}</h1>

<p>Your verification token:</p>

<p>http://localhost:8000/api/v1/activation/confirm/{{ token }}</p>
{% endblock %}
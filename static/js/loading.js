document.write('\
<ul id="dropdown1" class="dropdown-content">\
    <form method="POST" action="{{ url_for("/edit/1") }}"> \
        <li><a href="/edit/1">Champion 1</a></li>\
    <form>\
    <form method="POST" action="{{ url_for("/edit/2") }}"> \
        <li><a href="/edit/2">Champion 2</a></li>\
    </form>\
</ul>\
<nav>\
    <div class="nav-wrapper">\
        <a href="/" class="brand-logo" style="padding-left: 10px;">LOLStats - Data Structures Final Project</a>\
        <ul class="right hide-on-med-and-down">\
            <!-- Dropdown Trigger -->\
            <li><a class="dropdown-trigger" href="/edit/1" data-target="dropdown1">Champion and Itemization<i class="material-icons right">arrow_drop_down</i></a></li>\
            <li><a href="/stats">Stats</a></li>\
            <li><a href="/info">About Us</a></li>\
\
        </ul>\
    </div>\
</nav>\
');

document.write('\
<ul id="dropdown1" class="dropdown-content">\
  <form method="POST" action="{{ url_for("champ/edit/1") }}"> \
    <div name="Champ1">\
    <li name="Champ1"><a href="/edit/1" name="Champ1">Champion 1</a></li>\
    </div>\
    <form>\
    <form method="POST" action="{{ url_for("champ/edit/2") }}"> \
    <div name="Champ2">\
    <li name="Champ2"><a href="/edit/2" name="Champ2">Champion 2</a></li>\
    </div>\
  </form>\
</ul>\
<nav>\
  <div class="nav-wrapper">\
    <a href="/" class="brand-logo">Derp.gg</a>\
    <ul class="right hide-on-med-and-down">\
      <!-- Dropdown Trigger -->\
      <li><a class="dropdown-trigger" href="/champ" data-target="dropdown1">Champion and Itemization<i class="material-icons right">arrow_drop_down</i></a></li>\
      <li><a href="/stats">Stats</a></li>\
      <li><a href="/info">About Us</a></li>\
\
    </ul>\
  </div>\
</nav>\
');

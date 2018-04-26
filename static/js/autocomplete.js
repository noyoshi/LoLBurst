$(document).ready(function(){
    $(".dropdown-trigger").dropdown();
});

$(document).ready(function(){
    $('.scrollspy').scrollSpy();
});


function add_options_list(type) {
    var id = "autocomplete-options-"+type;
    $input = $("#autocomplete-input-"+type);
    $input.after(`
    <ul id=${id} class="autocomplete-dropdown dropdown-content" tabindex="-1"></ul>
    `);
    var backends = {
        'unsorted':'Unsorted List',
        'sorted':  'Sorted List',
        'trie':    'Trie!'
    };

    var radioname = `autocomplete-radio-${type}`
    $.each(backends, function(k, v) { 
        $input.parent().next().append(`<div><label><input type="radio" name=${radioname} value=${k} /><span>${v}</span></label></div>`);
    });
    $(`input[name=${radioname}][value='trie']`).prop('checked', true);
}

function add_option(type, data, key, index) {
    var baseurl;
    var url = `/static/${type}_icons/${data.image}`;
    var textstart = data.name.substring(0, key.length);
    var textend = data.name.substring(key.length);
    $li = $(`
        <li class="autocomplete-option" tabindex="0"><div>
        <strong class="autocomplete-match">${textstart}</strong><span>${textend}</span>
        <img src=${url} />
        </div></li>
    `);
    $li.addClass(type);
    $li.keydown(function(e) {
        if (e.which == 13) {
            var champ;
            if ($(this).hasClass('champ'))
                type = 'champ';
            else
                type = 'item';

            var text = $(this).text().trim();
            console.log("Entered on " + text + " of type " + type);
            search(type, text);
        }
    });
    $li.click(function(e) {
        var type;
        if ($(this).hasClass('champ'))
            type = 'champ';
        else
            type = 'item';

        var text = $(this).text().trim();
        console.log("Clicked on " + text + " of type " + type);
        search(type, text);
    });
    $(`#autocomplete-options-${type}`).append($li);

}

function search(type, text) {
    $input = $(`#autocomplete-input-${type}`);
    $input.val(text.trim());
    $input.focus();
}

function load_autocomplete(type, text) {
    var backend = $("input[name=autocomplete-radio-"+type+"]:checked").val();
    $.getJSON(`/backend?key=${text}&backend=${backend}&datatype=${type}`, function(result) {
        console.log("Inputting "+type+": " + text + "...");
        console.log(result);
        $(`#autocomplete-options-${type}`).empty();
        $.each(result, function(i, v) {
            add_option(type, v, text, i + 2);
        })
    });
}

$(document).ready(function() {
    var types = ["champ", "item"];
    $.each(types, function(key, type) {
        add_options_list(type);
        $('#autocomplete-input-'+type).on("input", function(e){
            var text = $(e.target).val();
            load_autocomplete(type, text);
        });

        $(`#${type}search`).focusout(function(e) {
            if (!this.contains(e.relatedTarget)) {
                $(`#autocomplete-options-${type}`).empty();
            }
        });

        $(`#autocomplete-input-${type}`).focus(function(e) {
            var text = $(this).val();
            console.log(text);
            load_autocomplete(type, text);
        });

    });
});

/*
$(document).ready(function(){

    $('#autocomplete-input-item').autocomplete({
        },
        limit: 10,
        minLength: 1
    });
});
*/

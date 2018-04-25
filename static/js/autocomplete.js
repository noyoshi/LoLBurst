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
    <ul id=${id} class="dropdown-content" tabindex="0"
        style="display: block; opacity: 1; transform: scaleX(1) scaleY(1); width: 100%; left: 10.5px; top: 43px; height 50px; transform-origin: 0px 0px 0px;">
    </ul>
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

function add_option(type, data) {
    $(`#autocomplete-options-${type}`).append(`<li>${data}</li>`);
}

function load_autocomplete(type, text) {
    var backend = $("input[name=autocomplete-radio-"+type+"]:checked").val();
    $.getJSON(`/backend?key=${text}&backend=${backend}&datatype=${type}`, function(result) {
        console.log("Inputting "+type+": " + text + "...");
        console.log(result);
        $(`#autocomplete-options-${type}`).empty();
        $.each(result, function(k, v) {
            add_option(type, v);
        })
    });
}

$(document).ready(function() {

    var types = ["champ", "item"];
    $.each(types, function(key, type) {
        console.log(type);
        add_options_list(type);
        $('#autocomplete-input-'+type).on("input", function(e){
            var text = $(e.target).val();
            load_autocomplete(type, text);
        });

        $(`#autocomplete-input-${type}`).focusout(function(e) {
            $(`#autocomplete-options-${type}`).empty();
        });

        $(`#autocomplete-input-${type}`).focus(function(e) {
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

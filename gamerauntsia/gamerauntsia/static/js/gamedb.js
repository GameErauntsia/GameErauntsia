$(function() {
	console.log("HAHA");
    $("#id_froga").autocomplete({
        source: "/ajax/get_jokoak/",
        minLength: 2,
        select: function(event, ui) {
            // $('#balioa').val( $(ui).val());
            $('<input type="hidden" value="'+ui.item.id+'" name="top_jokoak" id="id_top_jokoak_{{jokoak}}">').insertAfter('#id_top_jokoak_{{jokoak|add:-1}}');
        }
    });
});

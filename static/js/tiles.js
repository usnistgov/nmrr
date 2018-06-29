/*
 Create refinement fields dynamically and submit the form.
 Add an input field for each category given in the categories array in parameter.
*/
submitRefinement = function (categories, refinement_form_id) {
    categories.forEach(function(category_id) {
        $('<input/>').attr({type:'text',
                            name:refinement_form_id,
                            value:category_id}).appendTo('#form');
    });

    // Submit the form
    $('#form').submit();
}
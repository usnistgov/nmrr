/*
 Create refinement fields dynamically and submit the form.
 Add an input field for each category given in the categories array in parameter.
*/
submitRefinement = function (categories) {
    categories.forEach(function(category_id) {
        $('<input/>').attr({type:'text',
                            name:'refinement-type',
                            value:category_id}).appendTo('#form');
    });

    // Submit the form
    $('#form').submit();
}
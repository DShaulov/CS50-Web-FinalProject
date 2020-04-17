/**
 * checks if enter was pressed while focused on input, if yes, press submit form button
 */

$(document).ready( () => {
    $('input').on('keypress', function(event) {
        // if enter was pressed while focused on input, click the form button
        if (event.which == 13) {
            $('.form-button').click();
        }
    });
});
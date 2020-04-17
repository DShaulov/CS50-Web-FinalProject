/**
 * contains functions that check if the user input meets the restriction requirements
 */

function checkRegisterRestrictions(){
    // check that password is longer than 8 characters
    var password_length = $('input[name="password"]').val().length;
    if (password_length < 8){
        // remove previous error messages
        $('.error-message').remove();
        // insert new error message
        $('<br class="error-message"> <p class="my-text error-message" style="color: red" >* Password is less than 8 characters</p>').insertAfter($("input[name='password_again']"));
        return;
    }

    // check that email doesnt already exist
    $.ajax({
        method: "POST",
        url: "check_if_user_exists",
        data: {
            "csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val(),
            "email": $('input[name="email"]').val()
        },
        success: (data) => {
            if (data == "No existing user"){
                $("form").submit()
            }
            else {
                // remove previous error messages
                $('.error-message').remove();
                // insert new error message
                $('<br class="error-message"> <p class="my-text error-message" style="color: red" >* Email already taken</p>').insertAfter($("input[name='password_again']"));
            }
        }

        
    })
}
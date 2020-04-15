/** 
 * contains a function that checks if a user left an input field blank and that passwords match eachother
 */

 function checkInputs(){
    // get all of the inputs in the current page
    var all_inputs = $("input");
    var empty_input = false;
    all_inputs.each( (index) => {
        // if any are empty, set empty_input to true and change placeholder
        if ($(all_inputs[index]).val() == "") {
            $(all_inputs[index]).attr('placeholder', '* Cannot be empty');
            empty_input = true;
            return false;
        }
    });

    // check that passwords match
    if ($("input[name='password']").val() != $("input[name='password_again']").val()){

        // if they dont match display an error message and clear the password fields
        $("input[name='password']").val('');
        $("input[name='password_again']").val('');
        $('<br> <p class="my-text" style="color: red">* Passwords dont match</p>').insertAfter($("input[name='password_again']"));
        return false;
    }

    if (empty_input == true) {
        return false;
    }
    else {
        return true;
    }
 }
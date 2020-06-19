/**
 * contains instructions for calculating total cart items price
 */

$(document).ready(() => {
    // calculate total price
    var all_prices = $('.price');
    var total_price = 0
    $(all_prices).each( (index) => {
        console.log(total_price);
        var item_price = $(all_prices[index]).html().replace('$', '')
        var item_amount = $(all_prices[index]).siblings('.amount').html();
        var add_to_total = item_price * item_amount;
        total_price = total_price + add_to_total;
    })
    var conc_total_amount = '$'.concat(total_price);
    // add the total price to the cart table
    $('.total-amount').html("Total: ".concat(conc_total_amount));
})
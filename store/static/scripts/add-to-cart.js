/**
 * contains instructions for adding items to the users cart
 */

function add_to_cart(){
    product_name = $('.product-name').html();
    product_type = $('.product-type').html();

    console.log('ey im in')
    $.ajax({
        method: "POST",
        url: '/add-to-cart',
        data: {
            "csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val(),
            product_name: product_name,
            product_type: product_type
        }
    })
}
/**
 * contains instructions for redirecting users to a laptop product page onclick
 */

function redirect_to_product_page_laptop(laptop_name) {
 $.ajax({
     method: "POST",
     url: "redirect-to-product-page-laptop",
     data: {
        "csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val(),
        "laptop_name": laptop_name
     }
 })
}
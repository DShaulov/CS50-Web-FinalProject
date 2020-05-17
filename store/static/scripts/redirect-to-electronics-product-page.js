/**
 * contains instructions for redirecting users to a laptop product page onclick
 */

function redirect_to_electronics_product_page() {
    // get the correct div from the click event
    find_item_div = $(event.target)
    while ($(find_item_div).hasClass('item-card') == false) {
        find_item_div = $(find_item_div).parent()
    }
    product_type = $(find_item_div).children(".product-type").html();
    product_name = $(find_item_div).children(".product-name").html();

    $.ajax({
        method: "POST",
        url: "electronics-product-page",
        data: {
            "csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val(),
            "product_name": product_name,
            "product_type" : product_type
        },
        success: (data) => {
            // rememeber the electronics section page
            console.log($(location).attr("href"));
            window.history.pushState($(location).attr("href"), "Electronics Section");
            var new_document = document.open();
            new_document.write(data);
            new_document.close();
        }
    })
}
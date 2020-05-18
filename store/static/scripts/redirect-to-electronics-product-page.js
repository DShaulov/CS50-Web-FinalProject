/**
 * contains instructions for redirecting users to a laptop product page onclick
 */

function redirect_to_electronics_product_page() {
    // get the correct div from the click event
    find_item_div = $(event.target)
    while ($(find_item_div).hasClass('item-card') == false) {
        find_item_div = $(find_item_div).parent()
    }
    // submit the form in order to redirect to the product page
    $(find_item_div).children(".electronics-product-form").submit();
}
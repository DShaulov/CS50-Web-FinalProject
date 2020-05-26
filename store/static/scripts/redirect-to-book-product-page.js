/**
 * contains instructions for redirecting a user to a book product page upon clicking the item div
 */

function redirect_to_book_product_page() {
    // get the correct div from the click event
    find_item_div = $(event.target)
    while ($(find_item_div).hasClass('item-card') == false) {
        find_item_div = $(find_item_div).parent()
    }
    // submit the form in order to redirect to the product page
    $(find_item_div).children(".book-product-form").submit();
}
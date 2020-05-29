/**
 * contains function that on clic, scroll of product divs
 */

function scroll_right() {
    current_position = $(event.target).siblings("div").scrollLeft();
    $(event.target).siblings("div").animate({scrollLeft: current_position + 500}, 500);
}

function scroll_left() {
    current_position = $(event.target).siblings("div").scrollLeft();
    $(event.target).siblings("div").animate({scrollLeft: current_position - 500}, 500);
}
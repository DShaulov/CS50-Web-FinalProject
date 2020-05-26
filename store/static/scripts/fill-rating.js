/**
 * contains instructions for filling out the rating stars on the item card
 */

$(document).ready( () => {
    // get each of the rating bar
    $(".rating-stars").each( (element) => {
        // for each rating bar, check whats the databse rating
        database_rating = $('.rating-stars')[element].previousElementSibling.innerHTML;

        // according to the database rating, fill out the stars
        all_stars = $('.rating-stars')[element].children
        $(all_stars).each( (index) => {
            if (database_rating >= 1) {
                $(all_stars[index]).removeClass('fa-star-o');
                $(all_stars[index]).addClass('fa-star checked');
                database_rating = database_rating - 1;
                return;
            }
            
            if (database_rating == 0.5) {
                $(all_stars[index]).removeClass('fa-star-o');
                $(all_stars[index]).addClass('fa-star-half-o checked');
                database_rating = database_rating - 0.5;
            }
        });
    })
})
/**
 * contains a function that opens the sidebar
 */

 function open_desktop_sidebar(){
   $('.desktop-sidebar').slideToggle();

   //TODO Dim input fields
   //! Cant dim input fields
   // dim and brighten the body-block when the sidebar is opened/closed
   /* var background_color = $('.body-block').css('background-color');
   if (background_color == 'rgba(0, 0, 0, 0.5)') {
      $('.body-block').css('background-color', 'white');
      $('.body-block').attr('data-toggle', 'closed');
   }

   else {
      $('.body-block').css('background-color', 'rgba(0, 0, 0, 0.5)');
      $('.body-block').attr('data-toggle', 'open');
   } */
 }

// listen for clicks on the body, and close the sidebar
/* $(document).ready( function () {
   $('.body-block').on('click', function () {
      debugger;
      if ($('.body-block').attr('data-toggle') == "open") {
         $('#sidebar_opener_icon').click();
      }
   })
}) */

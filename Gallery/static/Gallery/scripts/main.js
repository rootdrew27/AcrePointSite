let categoryButtons,
    allCategoriesButton;

$(function() {
    console.log("Document is Ready");


    //Event listeners

    //Change button appearance
    //Update the 'visible' categories (and thus the images)
    //If button has class all-categories -> remove 'activated' from all other buttons
    //If button does NOT have class all-categories -> remove 'activated' from 'All' button

    //list of buttons
    categoryButtons = $('.btn.category');
    //ALL button
    allCategoriesButton = $('.btn.category.allcategories');


    categoryButtons.on('click', function () {

        var thisButton = $(this);

        if (thisButton.attr('activated') === undefined) {

            thisButton.attr('activated', true);

            if(thisButton.hasClass('allcategories') != false) {
                categoryButtons.each( function(i, e) {
                    if(i === 0){ return; } //ie. continue
                    $(e).removeAttr('activated');
                })
            }
            else {
                allCategoriesButton.removeAttr('activated');
            }
        }
        else {
            thisButton.removeAttr('activated');
        }

    });
    
});


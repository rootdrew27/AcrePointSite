// const { event } = require("jquery");

$(function() {
    console.log("Document is Ready");

    $('.categories-owl-carousel').owlCarousel({
        pagination: false,
        itemsMobile: [479, 3]
    });

    //All image cards
    let dg_img_cards = $('.dg-img_card');

    //Array used for Event logic 
    let dg_activeCategories = []; //this is used in the 'otherCategoryButtons' event to determine what images to show, the 'All' button event emptys this array because the event also deactivates the other buttons (this prevents multpile of the same category from being added)

    //Buttons
    let dg_allCategoriesButton = $('.dg-allcategories'); // the 'All' category button
    let dg_otherCategoryButtons = $('.dg-category'); //the other category buttons 

    //Event handler for allCategories Button (ie 'All' button)
    //Shows or hides all images (potentially deactivaes other buttons)
        // dg_allCategoriesButton.on('click', function(jqEvent) {
        //     var button = $(this);
        //     //if thisButton is not activated...
        //     //activate it
        //     //display all images
        //     //reset the array of categories to display (this is used in the other event to determine what images to show, but it is not necessarily representative of what categories are being shown)

        //     //else...
        //     //deactivate it
        //     //hide all images

        //     if (button.attr('dg-activated') === undefined) {
        //         button.attr('dg-activated', true);// activate it
        //         dg_img_cards.parent().css('display', 'block');

        //         dg_otherCategoryButtons.each(function(index, button) { // deactivate other buttons
        //             $(button).removeAttr('dg-activated');
        //         });
        //         dg_activeCategories = []; //reset 
        //     }
        //     else {
        //         button.removeAttr('dg-activated'); //deactivate it
        //         dg_img_cards.parent().hide();
        //     }

        // });

        var touchmoved;

        dg_allCategoriesButton.on('touchend', function(jqEvent) {
            jqEvent.preventDefault();
            if(touchmoved != true){

                var button = $(this);
                //if thisButton is not activated...
                //activate it
                //display all images
                //reset the array of categories to display (this is used in the other event to determine what images to show, but it is not necessarily representative of what categories are being shown)

                //else...
                //deactivate it
                //hide all images

                if (button.attr('dg-activated') === undefined) {
                    button.attr('dg-activated', true);// activate it
                    dg_img_cards.parent().css('display', 'block');

                    dg_otherCategoryButtons.each(function(index, button) { // deactivate other buttons
                        $(button).removeAttr('dg-activated');
                    });
                    dg_activeCategories = []; //reset 
                }
                else {
                    button.removeAttr('dg-activated');
                    dg_img_cards.parent().hide();
                }
            }

        }).on('touchmove', function(e){
            touchmoved = true;
        }).on('touchstart', function(){
            touchmoved = false;
        });


    

    //Event handler for all other buttons
    //Shows or hides image cards based on selected categories
    dg_otherCategoryButtons.each(function(jqEvent) {

        var button = $(this);
        button.on('click', function() {

            var button = $(this);
            //IF this button is not activated...
            //activate it
            //deactivate 'All' button
            //add this category to the activeCategory Dict

            //ELSE the button is activated...
            //deactivate it
            //remove this category from the active category arr
            
            //FINALLY..
            //loop through all images
                //IF the image has a category in activeCategories...
                //display image
                //ELSE hide image

            if (button.attr('dg-activated') === undefined) {

                button.attr('dg-activated', true);// activate the button 
                dg_allCategoriesButton.removeAttr('dg-activated'); //deactivate 'All' button
                dg_activeCategories.push(button.attr('dg-category')); //add the button to activeCategories
            }
            else {
                button.removeAttr('dg-activated');// deactivate button

                dg_activeCategories = dg_activeCategories.filter(function(arrElement){ //remove category from activeCategory array
                    return arrElement !== button.attr('dg-category');
                });
            }

            dg_img_cards.each(function() {
                var img_card = $(this);
                var img_categories = img_card.attr('dg-categories').split(',')//get img categories

                //loop through images
                //loop through image's categories and look for a match in the activeCategories array
                //IF there is match
                    //set the flag
                    //exit the loop
                //ELSE 
                //continue

                var inTheActiveArrayFlag = 0;
                img_categories.forEach( (img_category) => {

                    dg_activeCategories.forEach( (activeCategory) => {
                        if (activeCategory === img_category){ 
                            inTheActiveArrayFlag = 1;
                            return false; //exit loop
                        }
                    });
                });
                if (inTheActiveArrayFlag === 1){
                    img_card.parent().show();
                }
                else {
                    img_card.parent().hide();
                }
            });
        });


        button.on('touchend', function(jqEvent) {
            jqEvent.preventDefault();
            if (touchmoved != true){
            var button = $(this);
            //IF this button is not activated...
            //activate it
            //deactivate 'All' button
            //add this category to the activeCategory Dict

            //ELSE the button is activated...
            //deactivate it
            //remove this category from the active category arr
            
            //FINALLY..
            //loop through all images
                //IF the image has a category in activeCategories...
                //display image
                //ELSE hide image

            if (button.attr('dg-activated') === undefined) {

                button.attr('dg-activated', true);// activate the button 
                dg_allCategoriesButton.removeAttr('dg-activated'); //deactivate 'All' button
                dg_activeCategories.push(button.attr('dg-category')); //add the button to activeCategories
            }
            else {
                button.removeAttr('dg-activated');// deactivate button

                dg_activeCategories = dg_activeCategories.filter(function(arrElement){ //remove category from activeCategory array
                    return arrElement !== button.attr('dg-category');
                });
            }

            dg_img_cards.each(function() {
                var img_card = $(this);
                var img_categories = img_card.attr('dg-categories').split(',')//get img categories

                //loop through images
                //loop through image's categories and look for a match in the activeCategories array
                //IF there is match
                    //set the flag
                    //exit the loop
                //ELSE 
                //continue

                var inTheActiveArrayFlag = 0;
                img_categories.forEach( (img_category) => {

                    dg_activeCategories.forEach( (activeCategory) => {
                        if (activeCategory === img_category){ 
                            inTheActiveArrayFlag = 1;
                            return false; //exit loop
                        }
                    });
                });
                if (inTheActiveArrayFlag === 1){
                    img_card.parent().show();
                }
                else {
                    img_card.parent().hide();
                }
            });

        }
        }).on('touchmove', function(e){
            touchmoved = true;
        }).on('touchstart', function(){
            touchmoved = false;
        });

    });
});
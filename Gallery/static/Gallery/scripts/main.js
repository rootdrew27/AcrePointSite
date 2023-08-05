$(function() {
    console.log("Document is Ready");

    let dg_img_cards = $('.dg-img_card');

    //Arrays used for Event logic 
    let dg_imgsToDisplay = []; 
    let dg_activeCategories = []; //this is used in the 'otherCategoryButtons' event to determine what images to show, but it is not necessarily representative of what images/categories are being shown

    //Buttons
    let dg_allCategoriesButton = $('.dg-allcategories'); // the 'All' category button
    let dg_otherCategoryButtons = $('.dg-category'); //the other category buttons 

    //Event handler for allCategories Button (ie 'All' button)
    //Shows or hides all images (potentially deactivaes other buttons)
    dg_allCategoriesButton.on('click', function(jqEvent) {
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
            dg_img_cards.removeAttr('hidden');

            dg_otherCategoryButtons.each(function(index, button) { // deactivate other buttons
                $(button).removeAttr('dg-activated');
            });
            dg_activeCategories = []; //reset 
        }
        else {
            button.removeAttr('dg-activated'); //deactivate it
            dg_img_cards.attr('hidden', true);
        }

    });



    //Event handler for all other buttons
    dg_otherCategoryButtons.each(function() {

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
                $()
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
                    img_card.removeAttr('hidden');
                }
                else {
                    img_card.attr('hidden', true);
                }
            });

        });
    })
});
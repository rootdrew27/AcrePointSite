

$(function() {
    console.log("Document is Ready");

    let dg_categoryButtons,
    dg_allCategoriesButton,
    dg_categoiresToDisplay,
    dg_imgsToDisplay, //(when this array is empty, all images are shown)
    dg_imgs;

    //Event listeners

    //Change button appearance
    //Update the 'visible' categories (and thus the images)
    //If button has class all-categories -> remove 'activated' from all other buttons
    //If button does NOT have class all-categories -> remove 'activated' from 'All' button

    dg_imgs = $('.dg-img');

    //list of buttons
    dg_categoryButtons = $('.btn.dg-category');
    //ALL button
    dg_allCategoriesButton = $('.btn.dg-allcategories');

    //ToDo: break into multiple events 
    //One for the 'All' button, and events for each other button (these would be the same event) 
    dg_categoryButtons.on('click', function () {

        var thisButton = $(this);

        //if thisButton is not activated...
        if (thisButton.attr('dg-activated') === undefined) {

            thisButton.attr('dg-activated', true);// activate it 

            
            if(thisButton.hasClass('dg-allcategories') === true) { //if this is the 'All' button..
                dg_categoryButtons.each(function(i, e) { // deactivate other buttons
                    if(i === 0){ return; } //ie. continue
                    $(e).removeAttr('dg-activated');
                })
                //show all images
                dg_imgs.each(function(i, e){
                    $(this).removeAttr('hidden');
                });
                dg_categoiresToDisplay = []; //reset
                dg_imgsToDisplay = []; //reset (when this array is empty, all images are shown)
            }
            else { //thisButton is not the 'All' button
                dg_allCategoriesButton.removeAttr('dg-activated'); //deactivate 'All' button

                var thisCateogry = $(this).attr('dg-category');

                dg_categoiresToDisplay.append(thisCateogry); //add category to display list

                dg_imgs.each(function(index, thisImage){
                                        
                    var img_categories = $(thisImage).attr('dg-categories').split(','); //current image's categories

                    img_categories.forEach(function(i, img_category){
                        if(img_category === thisCateogry){
                            dg_imgsToDisplay.append(thisImage);
                        }
                    })
                })
                if (dg_categoiresToDisplay.length === 1){
                    dg_imgs.attr('hidden','true');
                    $(dg_imgsToDisplay).removeAttr('hidden');
                }
                else { // dg_categoriesToDisplay.length > 1
                    $(dg_imgsToDisplay).removeAttr('hidden');
                }
                // dg_imgsToDisplay = []; //reset 
            }
        }
        else { //this button is activated
            thisButton.removeAttr('dg-activated'); //deactivate it
        }

    });

    //Add images to array
    //Keep track of 'activated' categories
    //Display images which match any category in the category array




    
});


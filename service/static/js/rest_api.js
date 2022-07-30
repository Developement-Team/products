$(function () {

    // ****************************************
    //  U T I L I T Y   F U N C T I O N S
    // ****************************************

    // Updates the form with data from the response
    function update_form_data(res) {
        $("#product_id").val(res.id);
        $("#product_name").val(res.name);
        $("#product_category").val(res.category);
        $("#product_description").val(res.description);
        $("#product_available").val(res.available);
        $("#product_price").val(res.price);
        $("#product_rating").val(res.rating);
        $("#product_num_rating").val(res.no_of_users_rated);
    }

    /// Clears all form fields
    function clear_form_data() {
        $("#product_name").val("");
        $("#product_category").val("");
        $("#product_description").val("");
        $("#product_available").val("");
        $("#product_price").val("");
        $("#product_rating").val("");
        $("#product_num_rating").val("");
    }

    // Updates the flash message area
    function flash_message(message) {
        $("#flash_message").empty();
        $("#flash_message").append(message);
    }

    // ****************************************
    // Create a Product
    // ****************************************

    $("#create-btn").click(function () {

    });


    // ****************************************
    // Update a Product
    // ****************************************

    $("#update-btn").click(function () {

    });

    // ****************************************
    // Retrieve a Product
    // ****************************************

    $("#retrieve-btn").click(function () {

    });

    // ****************************************
    // Delete a Product
    // ****************************************

    $("#delete-btn").click(function () {

    });

    // ****************************************
    // Clear the form
    // ****************************************

    $("#clear-btn").click(function () {
        $("#product_id").val("");
        $("#flash_message").empty();
        clear_form_data()
    });

    // ****************************************
    // Search for a Product
    // ****************************************

    $("#search-btn").click(function () {

    });

    // ****************************************
    // Add a rating to Product
    // ****************************************

    $("#add-rating-btn").click(function () {

    });

})

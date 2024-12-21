$(function() {
    $('#customer-form-link').click(function(e) {
        // When customer register is clicked
        $("#customer-form").delay(100).fadeIn(100); // Show customer form
        $("#seller-form").fadeOut(100); // Hide seller form
        $('#seller-form-link').removeClass('active'); // Remove active class from seller link
        $(this).addClass('active'); // Add active class to customer link
        e.preventDefault();
    });

    $('#seller-form-link').click(function(e) {
        // When seller register is clicked
        $("#seller-form").delay(100).fadeIn(100); // Show seller form
        $("#customer-form").fadeOut(100); // Hide customer form
        $('#customer-form-link').removeClass('active'); // Remove active class from customer link
        $(this).addClass('active'); // Add active class to seller link
        e.preventDefault();
    });
});
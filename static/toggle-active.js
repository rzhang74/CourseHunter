$('#activeToggle > li').click(function () {

    //Check for active class
    if (!$(this).hasClass("active")) {

        // Remove the active class
        $("li.active").removeClass("active");

        // active current/clicked li
        $(this).addClass("active");
    }
});
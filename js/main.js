$(window).load(function () {
    
 
    $('.grid').masonry({
        columnWidth: '.grid-sizer',
        gutter: '.gutter-sizer',
        itemSelector: '.grid-item',
        percentPosition: true
    });
    $('.show-sub-bar').click(function () {
        $('.sub-bar').slideToggle();
        $('.show-sub-bar').toggleClass('nav-active');
    });
    $('#toggle').click(function () {
        $(this).toggleClass('show-nav-bar');
        $('.nav-bar-menu').slideToggle();
    });

    if ($('#news1').length >= 1) {
        $('#next').click(function () {
            $('#news1').vTicker('next', {animate: true});
        });
        $('#news1').vTicker('pause', true);
    }

    if ($('#news2').length >= 1) {
        $('#nextb').click(function () {
            $('#news2').vTicker('next', {animate: true});
        });
        $('#news2').vTicker('pause', true);
    }

    if ($('#datepicker').length >= 1) {
        $(function () {
            $("#datepicker").datepicker();
        });
    }
});
$(document).ready(function () {
    if ($('#news1').length >= 1) {
        $(function (s) {
            $('#news1').vTicker('init',
                    {speed: 400,
                        showItems: 3,
                        height: 194});
        });
        setInitialOpacities();
        $('#news1').on('vticker.afterTick', function () {
            setInitialOpacities2();
        });
    }
    if ($('#news2').length >= 1) {
        $(function (e) {
            $('#news2').vTicker('init',
                    {speed: 400,
                        showItems: 4,
                        height: 469});
        });
    }
    $('#next').click(function (i) {
        i.preventDefault();
    });
    $('#nextb').click(function (u) {
        u.preventDefault();
    });
    $('#toggle').click(function (p) {
        p.preventDefault();
    });
});
function setInitialOpacities() {
    var ul = jQuery('#news1 ul');
    ul.children('li:nth-child(1)').css("color", '#78909c').addClass('active');
    ul.children('li:nth-child(2)').css("color", 'white').removeClass('active');
    ul.children('li:nth-child(3)').css("color", 'white').removeClass('active');
    ul.children('li:nth-child(4)').css("color", 'white').removeClass('active');
}
function setInitialOpacities2() {
    var ul = jQuery('#news1 ul');
    ul.children('li:nth-child(1)').css("color", 'white').removeClass('active');
    ul.children('li:nth-child(2)').css("color", '#78909c').addClass('active');
    ul.children('li:nth-child(3)').css("color", 'white').removeClass('active');
    ul.children('li:nth-child(4)').css("color", 'white').removeClass('active');
}

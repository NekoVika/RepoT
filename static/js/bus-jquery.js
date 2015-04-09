$(document).ready( function() {
    $.each(NameCal, function( index, value ) {
        $(function () {
            $(value).datetimepicker({
            format: "YYYY/MM/DD",
            minDate: moment()
            });
        });
    });
    $('#ACh').on('click', function () {
        $(this).button('toggle') // button text will be "finished!"
    });
});


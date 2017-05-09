function toggleIcon(e) {
    $(e.target)
        .prev('.panel-heading')
        .find(".more-less")
        .toggleClass('glyphicon-plus glyphicon-minus');
}
$('.panel-group').on('hidden.bs.collapse', toggleIcon);
$('.panel-group').on('shown.bs.collapse', toggleIcon);

$(document).ready(function() {

    $.support.placeholder = (function(){
        var i = document.createElement('input');
        return 'placeholder' in i;
    })();

    if($.support.placeholder) {
        $('.form-label').each(function(){
            $(this).addClass('js-hide-label');
        });

        $('.form-group').find('input, textarea').on('keyup blur focus', function(e){

            // Cache our selectors
            var $this = $(this),
                $parent = $this.parent().find("label");

            if (e.type == 'keyup') {
                if( $this.val() == '' ) {
                    $parent.addClass('js-hide-label');
                } else {
                    $parent.removeClass('js-hide-label');
                }
            }
            else if (e.type == 'blur') {
                if( $this.val() == '' ) {
                    $parent.addClass('js-hide-label');
                }
                else {
                    $parent.removeClass('js-hide-label').addClass('js-unhighlight-label');
                }
            }
            else if (e.type == 'focus') {
                if( $this.val() !== '' ) {
                    $parent.removeClass('js-unhighlight-label');
                }
            }
        });
    }
});
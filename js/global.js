$(document).ready(function(e) {
    $('img[usemap]').rwdImageMaps();
    $('area').click(function() {
        console.log("clicou");
        $('#entrada').modal();
    });
});

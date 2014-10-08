/*globals jQuery, document */
/*jslint sloppy: true, vars: true, white: true, maxerr: 50, indent: 4 */
(function (jQuery) {
    /*
     * docs ...
     */
    function prepOverlay() {
        return jQuery('[data-rg-infocard-overlay]').prepOverlay({
            subtype: 'ajax',
        });
    }
    jQuery(document).ready(prepOverlay);
}(jQuery));

/*globals jQuery, document, portal_url */
/*jslint sloppy: true, vars: true, white: true, maxerr: 50, indent: 4 */
(function (jQuery) {
    /*
     * Add tinymce when needed
     */
    function textareas() {
        function init_textarea(idx, element) {
            var edit, show_box;
            element = jQuery(element);
            edit = jQuery('<img>').attr({src: portal_url+"/edit.png"}).css({float: 'left'});
            show_box = jQuery('<div>').html(element.text());
            element.after(show_box);
            element.after(edit);
            if (element.html()) {
                element.addClass('hiddenStructure');
            };
            edit.click(
                function(evt) {
                    jQuery.ajax({
                        url: portal_url + '/@@tinymce-jsonconfiguration?field=',
                        success: function(data) {
                            element.removeClass('hiddenStructure');
                            element.attr({
                                'data-mce-config': data
                            });
                            element.addClass('mce_editable');
                            element.addClass('pat-tinymce');
                            window.initTinyMCE(document);
                            edit.remove();
                            show_box.remove();
                        }
                    })
                }
            );
        }
        return jQuery('[data-rg-infocard-richtext]').each(init_textarea);
    }
    jQuery(document).ready(textareas);
}(jQuery));

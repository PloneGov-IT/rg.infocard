/*globals jQuery, document, portal_url */
/*jslint sloppy: true, vars: true, white: true, maxerr: 50, indent: 4 */
require(['jquery', 'mockup-patterns-modal'], function(jQuery, Modal) {
    function textareas() {
      
        function init_modal(self, a, idx){
          modal = new Modal(a, {
            position: 'center top',
            content: jQuery(self),
            templateOptions: {
              classBodyName: 'plone-modal-body',
              template: '' +
                '<div class="<%= options.className %>">' +
                '  <div class="<%= options.classDialog %>">' +
                '    <div class="<%= options.classModal %>">' +
                '      <div class="<%= options.classHeaderName %>">' +
                '        <a class="plone-modal-close">&times;</a>' +
                '        <% if (title) { %><h2 class="plone-modal-title"><%= title %></h2><% } %>' +
                '      </div>' +
                '      <div class="<%= options.classBodyName %>">' +
                '        <div class="<%= options.classPrependName %>"><%= prepend %></div> ' +
                '        <textarea class="textarea-wrapper pat-tinymce">' +
                '          <div class="<%= options.classContentName %>"><%= content %></div>' +
                '        </textarea>' +
                '      </div>' +
                '      <div class="<%= options.classFooterName %>"> ' +
                '        <% if (buttons) { %><%= buttons %><% } %>' +
                '        <button class="textarea-button" data-index='+ idx +' type="button">OK</button>' +
                '      </div>' +
                '    </div>' +
                '  </div>' +
                '</div>'
            }
          });
          modal.on('shown', function(e){  
            jQuery('.textarea-button').on('click', function(e){                
              var value = tinymce.activeEditor.getContent();
                                                                                
              // set new value
              var textarea = jQuery('#form-widgets-informations-'+ jQuery(e.target).data('index') +'-widgets-arg_value');
              textarea.val(value);
              textarea.text(value);
              var div = textarea.siblings('div:not(.label)');
              div.empty();
              div.append(jQuery(value));
              
              jQuery('.plone-modal-close').click();
            });
          });
                    
          return modal;
        }
      
        function init_textarea(idx, element) {
            var a, edit, show_box;
            
            if (jQuery(element).siblings('a.edit-textarea').length === 0){
              element = jQuery(element);  
              a = jQuery('<a>').attr({
                'href': "",
                'class': "edit-textarea"
              });         
              edit = 'Modifica';
              show_box = jQuery('<div>').html(element.text());
              element.after(show_box);
              element.after(a.append(edit));
              element.addClass('hiddenStructure');
            }else{
              a = jQuery(element).siblings('a.edit-textarea')
            }
                  
            modal = init_modal(this, a, idx);
        }
        jQuery('[data-rg-infocard-richtext]').each(init_textarea);

        function handle_new_row(evt, dgf, row) {
            jQuery('tbody.datagridwidget-body').find('textarea.richTextWidget').each(init_textarea)
        }
        jQuery(document.body).on(
            "afteraddrow afteraddrowauto aftermoverow",
            ".datagridwidget-table-view",
            handle_new_row
        );
    }
    jQuery(document).ready(textareas);
});

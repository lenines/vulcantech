/**
 * Created by lenin on 12/3/13.
 */
$(document).ready(function() {
    $.extend($.validationEngineLanguage.allRules, {
        number2: {
            alertText: '* Invalid floating decimal number',
            regex: /^[\-\+]?((([0-9]{1,3})([,][0-9]{3})*)|([0-9]+))?([,]([0-9]+))?$/
        }
    });
    jQuery("#formMobile").validationEngine();

});
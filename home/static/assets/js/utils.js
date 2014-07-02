/**
 * Created by lenin on 11/18/13.
 */
$(document).ready(function() {
 var fechaACtual=function(){
            var fullDate = new Date();console.log(fullDate);
            var twoDigitMonth = fullDate.getMonth()+"";if(twoDigitMonth.length==1)  twoDigitMonth="0" +twoDigitMonth;
            var twoDigitDate = fullDate.getDate()+"";if(twoDigitDate.length==1) twoDigitDate="0" +twoDigitDate;
            var currentDate = twoDigitDate + "-" + twoDigitMonth + "-" + fullDate.getFullYear();console.log(currentDate);
            return currentDate
       };
});
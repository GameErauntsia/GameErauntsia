$(document).ready(function() {
         $('.auto-submit-star').rating({
		  callback: function(value, link){
		   var slug = window.location.pathname;
                   slug = slug.replace('/tutorialak/','').replace('/','');
		   // To submit the form via ajax:
		   ajaxSubmit(value,slug);
		  }
 	});
    });

    function AjaxSucceeded(result) {
        if (result == 'True'){
            alert('Mila esker zure bozkagatik!')
        }
        else{
            alert('Ezin izan dugu zure bozka erregistratu...')
        }
        
    }
   
    function AjaxFailed(result) {
         alert(result.status + ' ' + result.statusText);
    }
    
    function ajaxSubmit(value,slug){
        $.ajax({
                type: "GET",
                url: "/rating",
                data: "value=" + value +"&slug="+ slug,
                success: function(msg) {                    
                    var delay = function() {
                        AjaxSucceeded(msg);
                    };
                    setTimeout(delay, 150);
                },
                error: AjaxFailed
        });       
    }
$(function(){
	$('.hamburger').click(function(e){
		$("#wrapper").toggleClass("toggled");
		if($('.hamburger').attr('class') == "hamburger is-closed"){
			$('.hamburger').attr('class','hamburger is-open')
		} else {
			$('.hamburger').attr('class','hamburger is-closed')
		}
	})
})


$("#menu-arrow-div").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
    $("#menu-arrow-div").toggleClass("toggled");
});

// $("#page-content-wrapper").click(function(e) {
//    	if($('#wrapper').attr('class') == "" && e.pageX > 75){
//    		$("#wrapper").attr('class',"toggled");
//    		$("#menu-arrow-div").attr('class',"");
//    	}    
// });

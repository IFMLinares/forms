$(document).ready(function() {
	$('#click1').click(function() {
	  if ($('#hidden1').is(':hidden')) {
		$('#hidden1').show(500);
	  } else {
		$('#hidden1').hide(500);
	  }
	});
  });

  $(".submenu").click(function(){
	$(this).children("ul").slideToggle();
  })
  
  $("ul").click(function(ev){
	ev.stopPropagation();
  })

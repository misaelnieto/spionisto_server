// execute your scripts when the DOM is ready. this is mostly a good habit
$(function() {
    //Load system_information
    $.ajax({
      url: '/@@system_status',
      dataType: 'json',
      success: function(data){
          $('p#time_update span').html(data.last_update);
          $('li#registered_cameras a').html(data.registered_cameras);
          $('li#online_cameras a').html(data.online_cameras);
          $('li#cameras_recording a').html(data.cameras_recording);
      }
    });

    
	// initialize scrollable
	$(".scrollable").scrollable();

	$(".items img").click(function() {
	
		// see if same thumb is being clicked
		if ($(this).hasClass("active")) { return; }
	
		// calclulate large image's URL based on the thumbnail URL (flickr specific)
		var url = $(this).attr("src").replace("_t", "");
	
		// get handle to element that wraps the image and make it semi-transparent
		var wrap = $("#image_wrap").fadeTo("medium", 0.5);
	
		// the large image from www.flickr.com
		var img = new Image();
	
	
		// call this function after it's loaded
		img.onload = function() {
	
			// make wrapper fully visible
			wrap.fadeTo("fast", 1);
	
			// change the image
			wrap.find("img").attr("src", url);
	
		};
	
		// begin loading the image from www.flickr.com
		img.src = url;
	
		// activate item
		$(".items img").removeClass("active");
		$(this).addClass("active");
	
	// when page loads simulate a "click" on the first image
	}).filter(":first").click();
});

var APP = (function(){
	var self = {
			rsvp: {
				init: function(){
					self.rsvp.bind();
				},

				bind: function(){
					$('.attending-yn').on('click', 'input', function(){
						var el = $(this);
						if(el.val() == 'True'){
							$('#attending-yes').slideDown();
							$('#attending-no').slideUp();
						} else {
							$('#attending-no').slideDown();
							$('#attending-yes').slideUp();
						}
					});
				}
			}

	};

	return self;
})();
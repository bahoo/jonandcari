var APP = (function(){
	var self = {
			rsvp: {
				init: function(){
					self.rsvp.bind();
					self.rsvp.geolocate();
				},

				geolocate: function(){
					$.get('http://freegeoip.net/json/' + APP.rsvp.ip, function(data){
						$('#id_location').val(data.city + ', ' + data.region_code);
					});
				},

				bind: function(){
					$('.attending-yn').on('click', 'a', function(){
						var el = $(this);
						el.addClass('clicked').siblings('.big-button').removeClass('clicked');
						var target = $('#attending-' + el.attr('href').substr(1));
						target.slideDown();
						$('body').animate({scrollTop: el.offset().top - 60}, 400);
						target.siblings('[id*="attending-"]').slideUp();
					});

					if(typeof self.rsvp.is_attending !== 'undefined'){
						$('a[href="#' + self.rsvp.is_attending + '"]').click();
					}
				}
			}

	};

	$(function(){
	});

	return self;
})();
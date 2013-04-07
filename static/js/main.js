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

					$('#id_count').on('blur', function(){
						var el = $(this);
						if(el.val() > 1){
							$('.attendees').slideDown(200, function(){
								var el = $(this).find('#id_attendees');
								el.focus();
								// set cursor to be at the end of the text already entered.
								// http://stackoverflow.com/a/10576409/412290
								var textarea = el.get(0);
								textarea.selectionStart = textarea.selectionEnd = textarea.value.length;
							});
						} else {
							$('.attendees').slideUp();
						}
					});
				}
			}

	};

	$(function(){
	});

	return self;
})();
$(document).ready(function(){

  $(".b-slider-nav a:first").addClass("active");

        var imageWidth = $(".b-slider").width();
        var imageSum = $(".b-slider-item").size();
        var imageReelWidth = imageWidth * imageSum;

        $(".b-slider-inner").css({'width' : imageReelWidth});

        rotate = function(){
            var triggerID = $active.attr("rel") - 1;
            var image_reelPosition = triggerID * imageWidth;

            $(".b-slider-nav a").removeClass('active');
            $active.addClass('active');

            $(".b-slider-inner").animate({
                left: -image_reelPosition
            }, 500 );

        };

        rotateSwitch = function(){
            play = setInterval(function(){
                $active = $('.b-slider-nav a.active').next();
                if ( $active.length === 0) {
                    $active = $('.b-slider-nav a:first');
                }
                rotate();
            }, 5000);
        };

        rotateSwitch();

        $(".b-slider-nav a").click(function() {
            if(!$(".b-slider-inner").is(':animated')) {
                $active = $(this);
                clearInterval(play);
                rotate();
                rotateSwitch(); }
            return false;
        });




})
(function($, window) {
      $("body").swipe( {
        swipe:function(event, direction, distance, duration, fingerCount, fingerData) {
          if(direction == 'left'){
            window.location.href = './' + left_page;
          }else if(direction == 'right'){
            window.location.href = './' + right_page;
          }
        },
         threshold:0
      });

}).call(this, jQuery, window);

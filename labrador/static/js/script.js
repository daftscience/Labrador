(function($, window) {
      $("body").swipe( {
        swipe:function(event, direction, distance, duration, fingerCount, fingerData) {
          $("#test").text("You swiped " + direction );
        },
         threshold:0
      });

      Materialize.updateTextFields();

}).call(this, jQuery, window);

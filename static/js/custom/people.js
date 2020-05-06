$(function(){
  
    var flag = 0;
    show_peoples()
    
    $(window).scroll(function() {
      if ($(window).scrollTop() >= $(document).height()-$(window).height()) {
        formdata = new FormData();
        formdata.append('offset',flag);
        formdata.append('limit','10');
        $.ajax({
          headers: { "X-CSRFToken": $.cookie("csrftoken") },
          processData: false,
          contentType: false,
          type: "post",
          url: "/peoples/show",
          data:formdata,
          success: function(data) {
            $("#show-peoples").html(data)
            flag += 5;
          }
        })
      }
    })
}); // ajax function

function show_peoples() {
      var flag = 0;
      formdata = new FormData();
      formdata.append('offset',0);
      formdata.append('limit','10');
      $.ajax({
        headers: { "X-CSRFToken": $.cookie("csrftoken") },
        processData: false,
        contentType: false,
        type: "post",
        url: "/peoples/show",
        data:formdata,
        success: function(data) {
          $("#show-peoples").html(data)
          flag += 5;
        }
      })
}


function follow(id) {
  formdata = new FormData();
  formdata.append('id',id);
  $.ajax({
    headers: { "X-CSRFToken": $.cookie("csrftoken") },
    processData: false,
    contentType: false,
    type: "post",
    url: "/follow/add",
    data:formdata,
    success: function(data) {
      $("#alert").html(data)
      show_peoples()
    }
  })
}
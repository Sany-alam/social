$(document).ready(function(){
  

  posts()

    var flag = 0;

  $(window).scroll(function() {
    if ($(window).scrollTop() >= $(document).height()-$(window).height()) {
      formdata = new FormData();
      formdata.append('offset',flag);
      formdata.append('limit',2);
        $.ajax({
          headers: { "X-CSRFToken": $.cookie("csrftoken") },
          processData: false,
          contentType: false,
          type: "post",
          url: "/posts/",
          data:formdata,
          success: function(data) {
                $("#posts").append(data);
              flag += 2;
          }
        });
    }
  })

  
  $("#post").click(function() {
    formdata = new FormData();
    formdata.append('title',$("#title").val());
    formdata.append('reference',$("#reference").val());
    formdata.append('content',$("#content").val());
    $.ajax({
      headers: { "X-CSRFToken": $.cookie("csrftoken") },
      processData: false,
      contentType: false,
      type: "post",
      url: "posts/create",
      data:formdata,
      success: function(data) {
        posts()
      }
    });
  })

}); // ajax function


function posts() {
  var flag = 0;
  formdata = new FormData();
  formdata.append('offset',0);
  formdata.append('limit',2);
  $.ajax({
    headers: { "X-CSRFToken": $.cookie("csrftoken") },
    processData: false,
    contentType: false,
    type: "post",
    url: "/posts/",
    data:formdata,
    success: function(data) {
        a = $.trim(data)
        if (a.length != 0) {
          $("#posts").html(data);
        }
        else{
          $("#posts").append("<h3 class='text-center text-primary'>No post available. Post only valid information!</h3>");
        }
        flag += 2;
    }
  });
 }
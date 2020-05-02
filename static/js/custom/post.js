$(function(){
  //  logout

  
  posts()
  
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
  formdata = new FormData();
    $.ajax({
      headers: { "X-CSRFToken": $.cookie("csrftoken") },
      processData: false,
      contentType: false,
      type: "get",
      url: "posts",
      data:formdata,
      success: function(data) {
          a = $.trim(data)
          if (a.length != 0) {
            $("#posts").html(data);
          }
          else{
            $("#posts").html("<h3 class='text-center text-primary'>No post available. Post only valid information!</h3>");
          }
      }
    });
 }
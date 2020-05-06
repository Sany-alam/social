$(function() {
    following()
    follower()
})

function removefollower(id) {
    formdata = new FormData();
    formdata.append('id',id);
    $.ajax({
      headers: { "X-CSRFToken": $.cookie("csrftoken") },
      processData: false,
      contentType: false,
      type: "post",
      url: "/follow/follower/remove",
      data:formdata,
      success: function(data) {
        $("#alert").html(data)
        following()
        follower()
      }
    })
}

function removefollowing(id) {
    formdata = new FormData();
    formdata.append('id',id);
    $.ajax({
      headers: { "X-CSRFToken": $.cookie("csrftoken") },
      processData: false,
      contentType: false,
      type: "post",
      url: "/follow/following/remove",
      data:formdata,
      success: function(data) {
        $("#alert").html(data)
        following()
        follower()
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
        following()
        follower()
      }
    })
  }


function following() {
    formdata = new FormData();
    $.ajax({
        headers: { "X-CSRFToken": $.cookie("csrftoken") },
        processData: false,
        contentType: false,
        type: "get",
        url: "/follow/following",
        data:formdata,
        success: function(data) {
            // console.log(data);
            $("#following").html(data);
        }
    })
  }

function follower() {
    formdata = new FormData();
    $.ajax({
        headers: { "X-CSRFToken": $.cookie("csrftoken") },
        processData: false,
        contentType: false,
        type: "get",
        url: "/follow/follower",
        data:formdata,
        success: function(data) {
            // console.log(data);
            $("#follower").html(data);
        }
    })
}
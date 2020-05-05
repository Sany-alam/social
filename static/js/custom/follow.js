$(function() {
    following()
    follower()
})

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
            console.log(data);
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
            console.log(data);
            $("#follower").html(data);
        }
    })
}

  function unfollow(id) {
      alert(id)
  }
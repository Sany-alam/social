$(function() {
    ShowChatList()
})

function chat(id) {
  alert(id)
}

function ShowChatList() {
    formdata = new FormData();
    $.ajax({
      headers: { "X-CSRFToken": $.cookie("csrftoken") },
      processData: false,
      contentType: false,
      type: "post",
      url: "/chat/chatlist",
      data:formdata,
      success: function(data) {
        $(".chat-user-list").html(data)
      }
    })
}
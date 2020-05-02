   // alert("heello")
   $(function() {
    show_comment($("#hidden_post_id").val());
    
    $("#addComment").click(function() {
        formdata = new FormData();
        formdata.append('hidden_post_id',$("#hidden_post_id").val());
        formdata.append('comment',$("#comment").val());
        $.ajax({
            headers: { "X-CSRFToken": $.cookie("csrftoken") },
            processData: false,
            contentType: false,
            type: "post",
            url: "/posts/comment/add",
            data:formdata,
            success: function(data) {
            show_comment($("#hidden_post_id").val())
            }
        });
    })
})

function show_comment(id){
    formdata = new FormData();
    $.ajax({
        headers: { "X-CSRFToken": $.cookie("csrftoken") },
        processData: false,
        contentType: false,
        type: "post",
        url: "/posts/comment/"+id,
        data:formdata,
        success: function(a) {
            console.log(a);
            // a = $.JSON.parse(data)
            data = jQuery.parseJSON(a);
            $("#show_comment").html(data.loop);
            $("#total-comment").html("Comments ("+data.total+")");
        }
    });
}
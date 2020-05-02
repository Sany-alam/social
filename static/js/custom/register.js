$(function() {
    
    $('.datepicker-input').datepicker();
    $('.select2').select2();
    // $.datepicker.parseDate( "yy-mm-dd" );
    $( ".selector" ).datepicker({
        altFormat: "yy-mm-dd"
      });


    $("#username").focusout(function() {
            formdata = new FormData();
        formdata.append('uname',$("#username").val());
        $.ajax({
            headers: { "X-CSRFToken": $.cookie("csrftoken") },
            processData:false,
            contentType:false,
            data:formdata,
            url:"/ValidUsername/",
            type:"post",
            success:function(data) {
                i = $.trim(data)
                if (i == "positive") {
                    $("#alertusername").show()
                    $("#alertusername").html("Invalid Username")
                }
                else{
                    $("#alertusername").hide()
                }
            }
        })
    })


    $("#email").focusout(function() {
        formdata = new FormData();
        formdata.append('email',$("#email").val());
        $.ajax({
            headers: { "X-CSRFToken": $.cookie("csrftoken") },
            processData:false,
            contentType:false,
            data:formdata,
            url:"/Validemail/",
            type:"post",
            success:function(data) {
                i = $.trim(data)
                if (i == "positive") {
                    $("#alertusername").show()
                    $("#alertusername").html("Invalid email")
                }
                else{
                    $("#alertusername").hide()
                }
            }
        })
    })


})
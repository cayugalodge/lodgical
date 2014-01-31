function add_alum(csrf_token) {
    $.ajax({
        type: "POST",
        url:"/alumni/add/",
        data: {
            name: $("#id_name").val(),
            email: $("#id_email").val(),
            csrfmiddlewaretoken:csrf_token
        },
        success: function(response) {
            if (response == 'success') {
                $( "#success_msg" ).show();
                $("#alum_form")[0].reset();
            } else {
                $( "#error_msg" ).show();
            }},
        error: function(){
            $( "#problem_msg" ).show();
        }
    });
}
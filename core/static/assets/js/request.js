$(document).ready(function(){
    $(document).on("click","#editsupplier", function(e){
        var supplier_id = $(this).data("supplier")

        $.ajax({
            method: "POST",
            url: "{% url 'supplier_edit' %}",
            data:{
                'supplier_id': supplier_id
            },
            success: function(data){
                console.log(data)
            },
            error: function(data){
                console.log(data)
            },
        })
    });
});
$(function() {
    $('a#calculate').bind('click', function() {
        $.getJSON('_addNumbers', {
            a : $('input[name="a"]').val(),
            b : $('input[name="b"]').val()
        }, function(data) {
            $("#result").text(data.result);
        });
        return false;
    })
    $("p#calculate2").click(function() {
        $.getJSON('_mulNumbers', {
            a : $('input[name="a2"]').val(),
            b : $('input[name="b2"]').val()
        }, function(data) {
            $("#result2").text(data.result);
        });
        return false;
    })
    $("p#action").click(function() {
        $.ajax({url:"/static/txt.txt", async:true, success:function(result) {
            $("#text").html(result);
        }})
    })
    $("p#action2").click(function() {
        $.post("/static/txt.txt", {name:"loading"}, function(data,status){
            $('#text2').html(data);
        })
    })
})
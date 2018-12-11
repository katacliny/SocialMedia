$( document ).ready(function() {
    $("#start-stop-listen-button").click(function () {

        if($(this).hasClass( "start-listen-button" )){
            $(this).removeClass("start-listen-button");
            $(this).addClass("stop-listen-button");
            $(this).html("Stoped");
            $.ajax({
                    url: '/StopSearch/',
                    data: {},
                    dataType: 'json',
                    success: function (data) {
                    }
                  });

        } else{
            $(this).removeClass("stop-listen-button");
            $(this).addClass("start-listen-button");
            $(this).html("Listen");
            $.ajax({
                    url: '/StartSearch/',
                    data: {},
                    dataType: 'json',
                    success: function (data) {
                    }
                  });
        }

    })
});
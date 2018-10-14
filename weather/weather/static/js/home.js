$(document).ready(function() {
    getLocation();

    var lat;
    var lon;

    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition);
        
    }};

    function showPosition(position) {
        var lat = position.coords.latitude;
        var lon = position.coords.longitude;

        $.ajax({
            url: "/senddata/",
            type: "GET",
            dataType: "json",
            data: {
                "Latitude": lat,
                "Longitude": lon
            },
            success: function(response) {
                console.log(response);
                $(".cityname").html(response['city'] + ", " + response['country']);
                $(".temp").html(response['temperature']+"°");
                $(".description").html(response['description']);
                $(".sunrise").html("sunrise at: " + response['sunrise']);
                $(".sunset").html("sunset at: " + response['sunset']);
                $(".humidity").html("Humidty: " + response['humidity']+"%");
                $(".pressure").html("Pressure:" + response['pressure']+" hPa");
                $(".windspeed").html("Wind Speed: " + response['wind_speed']+" m/s");
                $("img").attr('src', "https://openweathermap.org/img/w/" + response['icon'] + ".png");
                $(".tmax").html("Max temperature: " + response['temp_max']+"°");
                $(".tmin").html("Min temperature: " + response['temp_min']+"°");
                $(".main").html(response['main']);
            }
        });
    }

});
function loadActionTiles() {
    $.ajax({
        url: tilesGetUrl,
        method: "GET",
        success: function(data) {
            $("#tiles").html(data);
        },
        error: function(data) {

        }
    });
}


loadActionTiles();
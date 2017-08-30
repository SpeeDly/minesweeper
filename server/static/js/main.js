$( document ).ready(function() {
    var game_id = $('#game').data('game');
    var status;

    setInterval(function() {
        $.ajax({
            type: "GET",
            url: "/state/" + game_id,
            dataType: 'json',
            data: {'game_id': game_id},
            success: render
        });
    }, 1000);

    function render(data) {
        var board = data['board']

        html = ''
        for (var i = 0; i < board.length; i++) {
            html += '<tr>';
            for (var j = 0; j < board[i].length; j++) {
                html += '<td class="block">';
                html += board[i][j];
                html += '</td>';
            }
            html += '</tr>';
        }
        $('#game').html(html);
        if (status !== undefined && status !== data['status']) {
            if (data['status'] == -1) {
                alert("The player lost the game!");
            }
            else {
                alert("The player won the game!");
            }
            window.location.href = "/";
        }
        status = data['status'];
    }
});
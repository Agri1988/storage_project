$(document).ready(function () {
    var table = $('#table').find('tbody').find('th');
    var rows_length = document.getElementById('table').rows.length;
    console.log(table);
    function filter_data(index, sample) {
            var table = document.getElementById('table');
            for (var i = 2; i < rows_length; i++) {
                if ((table.rows[i].cells[index].innerText.toLowerCase()).indexOf(sample.toLowerCase()) == -1) {
                    table.rows[i].setAttribute("style", "display:none")
                }
                else if(sample != ''){table.rows[i].setAttribute("style", "display:")}
                else {
                    table.rows[i].setAttribute("style", "display:")
                }
            }
        }
    table.each(function (index) {
        var input = $(this).find('input');
            input.on('input keyup', function (e) {
                filter_data(index, String(input.val()))
            })
    });
    console.log(table)
});





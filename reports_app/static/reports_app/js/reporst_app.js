/**
 * Created by Ar on 26.11.2017.
 */
$(document).ready(function () {
    var table = $('#table').find('tbody').find('th');
    var rows_length = document.getElementById('table').rows.length;

    function filter_data(index, sample) {

            var table = document.getElementById('table');
            for (var i = 2; i < rows_length; i++) {
                if ((table.rows[i].cells[index].innerText).indexOf(sample) == -1) {
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
                console.log(input.val());
                filter_data(index, String(input.val()))
            })
    });
    table = $('#table').find('tbody');
    table.find('tr').each(function (index) {
        var csrf = $(this).find("[name='csrfmiddlewaretoken']").val();
        var input_document_id = $(this).find('#document_id');
        var input_document_date = $(this).find('#document_date');
        var input_product_id = $(this).find('#product_id');
        var product_count = $(this).find('#product_count');
        var input_btn = $(this).find('#add_btn');
        var url_redirect = '/documents/'+input_document_id.val();
        var url_action = '/reports/add_product_to_outgoing_document';
        input_btn.on("click", function (e) {
            $.ajax({
                url: url_action,
                type: 'POST',
                data: {
                    input_document_id: input_document_id.val(), input_document_date: input_document_date.val(),
                    csrfmiddlewaretoken: csrf, input_product_id: input_product_id.val(), product_count:product_count.val()},
                cache: true,
                success: function () {
                    console.log('OK')
                    document.location.href = url_redirect
                },
                error: function () {
                    console.log('error')
                }
            });
        });
    });
});
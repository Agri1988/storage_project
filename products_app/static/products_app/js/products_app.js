$(document).ready(function () {
    var margin_percentage = $('#id_margin_percentage');
    var provider_price = $('#id_provider_price');
    var vat = $('#id_vat');
    var product_price = $('#id_product_price');
    
    function calculate_vat() {
        return parseFloat(provider_price.val())*(parseFloat(vat.val())/100);
    }

    function calculate_price_with_vat() {
        return parseFloat(provider_price.val())+calculate_vat()
    }

    function calculate_product_price() {
        var summ;
        var function_vat = calculate_vat();
        var function_margin_percentage = (function_vat+ parseFloat(provider_price.val()))*(parseFloat(margin_percentage.val())/100);
        summ = calculate_price_with_vat()+function_margin_percentage;
        summ =summ.toFixed(2);
        console.log(summ);
        return summ;
    }

    function calculate_margin_percentage() {
        var function_product_price = parseFloat(product_price.val());
        var function_margin = function_product_price-calculate_price_with_vat();
        console.log(function_product_price);
        console.log(calculate_price_with_vat());
        console.log(function_margin);
        return (function_margin*100/calculate_price_with_vat()).toFixed(2)
    }

    margin_percentage.blur(function() {
        margin_percentage.val() > 0? product_price.val(calculate_product_price()):product_price.val(product_price.val());
    });

    provider_price.blur(function () {
        product_price.val(calculate_product_price())
    });

    vat.blur(function () {
        product_price.val(calculate_product_price())
    });

    product_price.blur(function () {
        margin_percentage.val(calculate_margin_percentage())
    });
        console.log(calculate_margin_percentage())

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
                console.log(input.val())
                filter_data(index, String(input.val()))
            })
    })
    console.log(table)
});





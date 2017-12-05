$(document).ready(function () {
    var category = $('#id_category');
    category.after('<div id="modal_form">' +
        '<span id="modal_close">X</span>' +
        '</div>' +
        '<div id="overlay"></div>' +
        '<button value="'+url_add_category+'" id="add_category">добавить</button>');
    var add_btn = $('#add_category');
    add_btn.click( function (e) {
        e.preventDefault();
        var data_dict= {};
        $('#add_new_product p').each(function (index) {
            data_dict[index] = $(this).find('input').val()
        });
        $('#overlay').fadeIn(400, // снaчaлa плaвнo пoкaзывaем темную пoдлoжку
		 	function() { // пoсле выпoлнения предъидущей aнимaции
                $('#modal_form')
                    .css('display', 'block') // убирaем у мoдaльнoгo oкнa display: none;
                    .animate({opacity: 1, top: '50%'}, 200); // плaвнo прибaвляем прoзрaчнoсть oднoвременнo сo съезжaнием вниз
            });
        var csrf = $('#add_new_product').find("[name='csrfmiddlewaretoken']").val();
        $.ajax({
                url:add_btn.val(),
                type:'GET',
                data:data_dict,
                cache:true,
                success:function (data){
                    console.log('OK');
                    $('#modal_form').append(data)
                },
                error:function () {
                    console.log('error')
                }
            });

    });

    	/* Зaкрытие мoдaльнoгo oкнa, тут делaем тo же сaмoе нo в oбрaтнoм пoрядке */
    function close_modal_window () {
        $('#modal_form')
        .animate({opacity: 0, top: '45%'}, 200,  // плaвнo меняем прoзрaчнoсть нa 0 и oднoвременнo двигaем oкнo вверх
            function(){ // пoсле aнимaции
                $(this).css('display', 'none'); // делaем ему display: none;
                $('#overlay').fadeOut(400); // скрывaем пoдлoжку
            }
        );
    $('#modal_form').find('div').remove()
    }

	$('#modal_close, #overlay').click( function(){ // лoвим клик пo крестику или пoдлoжке
        close_modal_window()
	});


    // $('a#go').click( function(event){ // лoвим клик пo ссылки с id="go"
		// event.preventDefault(); // выключaем стaндaртную рoль элементa
		//
    //             var csrf = $(document).find("[name='csrfmiddlewaretoken']").val();
		// });

    //отправка формы и подстановка нового значения в select
    //     var save_form_btn = $(document).find('#category_form').find('submit');
    // $('body').on('click', ".find('#category_form').find('submit')",function (event) {
    //     event.preventDefault();
    //         console.log('dasfghjgsdfadfghj')
    $('#modal_form').on('submit',function (event) {
        event.preventDefault();
        var csrf = $('#add_new_product').find("[name='csrfmiddlewaretoken']").val();
        var data_dict= {};
        $('#modal_form').find('#category_form p').each(function (index) {
            data_dict[$(this).find('input').attr('name')] = $(this).find('input').val()
        });
        data_dict['csrfmiddlewaretoken']=csrf;
        var url = $('#modal_form').find('#category_form').attr('action');
        console.log(data_dict);
        $.ajax({
                url:url,
                type:'POST',
                data:data_dict,
                cache:true,
                success:function (data){
                    console.log('OK');
                    console.log(data);
                    category.append("<option value="+data['new_category_id']+">"+data['new_category_name']+"</option>");
                    category.val(data['new_category_id']);
                    close_modal_window()
                },
                error:function () {
                    console.log('error')
                }
            });
    });

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
        return summ;
    }

    function calculate_margin_percentage() {
        var function_product_price = parseFloat(product_price.val());
        var function_margin = function_product_price-calculate_price_with_vat();
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





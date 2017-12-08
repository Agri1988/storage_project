$(document).ready(function () {
    var add_product_btn = $('#add_product_btn');
    var document_id = $('#document_id').val();
    var storage_id = $('#id_storage').val();
    var document_date = $('#id_date').val();
    console.log(a+'/'+document_id+'/'+storage_id);

    var price_tickiet_list_btn = $('#price_tickiet_list');
    var price_ticket_list_url = price_tickiet_list_btn.data('url');
    price_tickiet_list_btn.on('click', function (event) {
        event.preventDefault();
        document.location.href = price_ticket_list_url
    });

    if ($('#id_document_type').val().indexOf('remove', '') != -1){
        price_tickiet_list_btn.attr('style', 'display:none')
    }

    add_product_btn.on('submit', function (e) {
        e.preventDefault();
        var document_type = $('#id_document_type').val();
        if (document_type == 'add'){
            document.location.href = a+'/'+document_id+'/'+storage_id;
        }
        else if (document_type == 'remove'){
            document.location.href = '/reports/'+document_date+'/'+document_id+'/'+storage_id
        }
        else if (document_type == 'move'){

            document.location.href = '/reports/'+document_date+'/'+document_id+'/'+storage_id
        }


         });

    var document_type = $('#id_document_type');
    var to_storage = $('#id_to_storage');
    to_storage.attr('style', 'display:none');
    var label = $('label')[7];
    label.setAttribute('style', 'display:none');
    console.log(label);
    document_type.change(function () {
        if (document_type.val() == 'move') {
            to_storage.attr('style', 'display:');
            label.setAttribute('style', 'display:')
        }
        else {
            to_storage.attr('style', 'display:none');
            label.setAttribute('style', 'display:none')
        }

    });

    //update data in table products_in_dokuments from editing page input document
    $('#products_in_dokument li').each(function (index) {
        var button = $(this).find('button');
        var products_in_document_id = $(this).find('#products_in_document_id').val();
        var count = $(this).find('#id_count');
        var url = $(this).find('form').attr('action');
        var csrf = $(this).find("[name='csrfmiddlewaretoken']").val();
        button.on('click',function(e){
        e.preventDefault();
            $.ajax({
                url:url,
                type:'POST',
                data:{products_in_document_id : products_in_document_id, count : count.val(), csrfmiddlewaretoken : csrf},
                cache:true,
                success:function (){
                    console.log('OK')
                },
                error:function () {
                    console.log('error')
                }
            });
        });
    });


    var provider = $('#id_provider');
    provider.after('<div id="modal_form">' +
        '<span id="modal_close">X</span>' +
        '</div>' +
        '<div id="overlay"></div>' +
        '<button value="'+url_add_partner+'" id="add_partner">добавить</button>');
    var add_btn = $('#add_partner');
    add_btn.click( function (e) {
        e.preventDefault();
        var data_dict= {};
        $('#document_form p').each(function (index) {
            data_dict[index] = $(this).find('input').val()
        });
        $('#overlay').fadeIn(400, // снaчaлa плaвнo пoкaзывaем темную пoдлoжку
		 	function() { // пoсле выпoлнения предъидущей aнимaции
                $('#modal_form')
                    .css('display', 'block') // убирaем у мoдaльнoгo oкнa display: none;
                    .animate({opacity: 1, top: '50%'}, 200); // плaвнo прибaвляем прoзрaчнoсть oднoвременнo сo съезжaнием вниз
            });
        var csrf = $('#document_form').find("[name='csrfmiddlewaretoken']").val();
        $.ajax({
                url:add_btn.val(),
                type:'GET',
                data:data_dict,
                cache:true,
                success:function (data){
                    console.log('OK');
                    console.log(data);
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

    $('#modal_form').on('submit',function (event) {
        event.preventDefault();
        var csrf = $('#document_form').find("[name='csrfmiddlewaretoken']").val();
        var data_dict= {};
        $('#modal_form').find('#partner_form p').each(function (index) {
            data_dict[$(this).find('input').attr('name')] = $(this).find('input').val()
        });
        data_dict['csrfmiddlewaretoken']=csrf;
        var url = $('#modal_form').find('#partner_form').attr('action');
        console.log(data_dict);
        $.ajax({
                url:url,
                type:'POST',
                data:data_dict,
                cache:true,
                success:function (data){
                    console.log('OK');
                    var provider = $('#id_provider');
                    provider.append("<option value="+data['new_partner_id']+">"+data['new_partner_name']+"</option>");
                    provider.val(data['new_partner_id']);
                    close_modal_window()
                },
                error:function () {
                    console.log('error')
                }
            });
    });
});







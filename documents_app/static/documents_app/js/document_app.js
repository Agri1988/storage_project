$(document).ready(function () {
    var add_product_btn = $('#add_product_btn');
    var document_id = $('#document_id').val();
    var storage_id = $('#id_storage').val();
    var document_date = $('#id_date').val();
    console.log(a+'/'+document_id+'/'+storage_id);

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
    var label = $('label')[7]
    label.setAttribute('style', 'display:none')
    console.log(label)
    document_type.change(function () {
        if (document_type.val() == 'move') {
            to_storage.attr('style', 'display:')
            label.setAttribute('style', 'display:')
        }
        else {
            to_storage.attr('style', 'display:none')
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
});







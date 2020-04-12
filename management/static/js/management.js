$("#report-button").on('click', function(){
    var content = [{
                'staff': $('#staff_member')[0].value,
                'amount': $('#cashless')[0].value,
                'cost': '2',
                'day': $('#day')[0].value,
                'shop': $('#shop_id')[0].value
            },
            {
                'staff': $('#staff_member')[0].value,
                'amount': $('#cash')[0].value,
                'cost': '1',
                'day': $('#day')[0].value,
                'shop': $('#shop_id')[0].value
            },
            {
                'staff': $('#staff_member')[0].value,
                'amount': $('#finish_cash')[0].value,
                'cost': '6',
                'day': $('#day')[0].value,
                'shop': $('#shop_id')[0].value
            }];
    var data = {
            'content': JSON.stringify(content),
            'csrfmiddlewaretoken': $('#csrf_token')[0].value
        };
    $.ajax({
            data: data,
            type: "POST",
            dataType: 'json',
            url: "/management/api/",
            success: function(result){
                $("#report-form").html('<h1>Data entered successfully</h1>');
            }
        })
});

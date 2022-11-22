$(document).ready(function(){
    if( $('#flexSwitchCheckDefault').is(':checked') ){
        $('#check_checkbox').text('');
        $('#id_button').prop('disabled', false);
    }else{
            $('#check_checkbox').text('Debe aceptar los términos y condiciones para poder continuar');
            $('#id_button').prop('disabled', true);
    }
    $('#flexSwitchCheckDefault').change(function(){
        if($(this).prop('checked') === true){
           $('#check_checkbox').text('');
           $('#id_button').prop('disabled', false);
        }else{
             $('#check_checkbox').text('Debe aceptar los términos y condiciones para poder continuar');
             $('#id_button').prop('disabled', true);
        }
    });
});

function consultar_saldo(rut){
  $.ajax({
    method: "POST",
    url: "/bank/consultar_saldo_pro/",
    data: {
        'rut': rut,
        'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
    },
    success: function(data){
        $('#resultado_consulta').html(data);
       },
    dataType: 'html',
    async: true
  });
}

function realizar_transferencia(cue_o, cue_d, mon_t){
    $.ajax({
      method: "POST",
      url: "/bank/transferencia_pro/",
      data: {
          'cue_o': cue_o,
          'cue_d': cue_d,
          'mon_t': mon_t,
          'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
      },
      success: function(data){
          $('#resultado_consulta').html(data);
         },
      dataType: 'html',
      async: true
    });
  }

$('#update_url_button').click(function() {
  $('#update_url_modal').modal();
});
$('#update_url_form').submit(function(e) {
  e.preventDefault();

  // indicate loading data
  var btn = $(this).find('button[type=submit]');
  btn.attr('disabled', true);

  // load data from URL
  $.post("/workshops/events/import/", $(this).find(":input"), function(data) {
    var action = $('#update_url_form input[type=radio]:checked').val();

    $("#event_update_url").parent().removeClass('has-error');
    $('#update_url_modal').modal('hide');

    switch (action) {
      case 'overwrite':
        console.log('overwrite');
        $("#id_event-slug").val(data.slug);
        $("#id_event-start").val(data.start);
        $("#id_event-end").val(data.end);
        $("#id_event-reg_key").val(data.reg_key);
        $("#id_event-url").val(data.url);
        $("#id_event-contact").val(data.contact);
        $("#id_event-notes").val(data.notes);
        $('#id_event-venue').val(data.venue);
        $('#id_event-address').val(data.address);
        $('#id_event-country').val(data.country);
        $('#id_event-latitude').val(data.latitude);
        $('#id_event-longitude').val(data.longitude);
        break;

      case 'skip':
      default:
        console.log('skip');
        if ($("#id_event-slug").val() == "") {
          $("#id_event-slug").val(data.slug);
        }
        if ($("#id_event-start").val() == "") {
          $("#id_event-start").val(data.start);
        }
        if ($("#id_event-end").val() == "") {
          $("#id_event-end").val(data.end);
        }
        if ($("#id_event-reg_key").val() == "") {
          $("#id_event-reg_key").val(data.reg_key);
        }
        if ($("#id_event-url").val() == "") {
          $("#id_event-url").val(data.url);
        }
        if ($("#id_event-contact").val() == "") {
          $("#id_event-contact").val(data.contact);
        }
        // append notes
        var today = new Date();
        var today_str = "\nUPDATE " + today.getFullYear() + "-" + today.getMonth() + "-" + today.getDay() + ":\n";
        $("#id_event-notes").val($("#id_event-notes").val() + today_str + data.notes);
        if ($("#id_event-venue").val() == "") {
          $("#id_event-venue").val(data.venue);
        }
        if ($("#id_event-address").val() == "") {
          $("#id_event-address").val(data.address);
        }
        if ($("#id_event-country").val() == "") {
          $("#id_event-country").val(data.country);
        }
        if ($("#id_event-latitude").val() == "") {
          $("#id_event-latitude").val(data.latitude);
        }
        if ($("#id_event-longitude").val() == "") {
          $("#id_event-longitude").val(data.longitude);
        }

        break;
    }
  })
  .fail(function(data) {
    // something went wrong, let's indicate it
    $("#event_update_url").parent().addClass('has-error');
  })
  .always(function(data) {
    // let's always reenable the form's submit when the request finishes
    btn.attr('disabled', false);
  });
});

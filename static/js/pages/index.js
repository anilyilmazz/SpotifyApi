﻿var datatable;

$( document ).ready(function() {
    $.ajax({
        type: 'GET',
        url: '/getgenres',
        contentType: "application/json",
        success: function (response, status, xhr, $form) {
            response.forEach(genre =>{
                $('#selectGenre').append($('<option/>', {
                    value: genre,
                    text : genre
                }));
            })
        }
    });
});

function submitClick(){
     event.preventDefault();
     let genreName = $( "#selectGenre option:selected" ).text();
     $('#tracksTable').show();
     if (datatable) {
      $('#tracksTable').empty();
      datatable.destroy();
     }
    datatable = $('#tracksTable').DataTable( {
           "order": [[ 1, "asc" ]],
           "paging": false,
           "destroy": true,
           "serverSide": false,
           "ajax": {
               "type": "GET",
               "url": `/tracks/${genreName}`,
                "contentType": 'application/json;',
               "dataSrc": function (data){
                   $('#artistName').html(`<strong>${data.artistname.charAt(0).toUpperCase() + data.artistname.slice(1)}</strong> Top 10 Tracks`);
                   return data.tracklist;
               },
               "error": function (xhr, error, code)
               {
                   console.log(xhr);
                   console.log(code);
               }
           },
           "columns": [
               { "data": "name" },
               { "data": "popularity" },
               { "data": "album.name" },
               {
                   "defaultContent": `<button class ="btn btn-secondary preview">Preview</button>`
               }
           ]
     } );

     $('#tracksTable tbody').on('click', 'button', function () {
     var data = datatable.row($(this).parents('tr')).data();
        if(data.preview_url){
             window.open(data.preview_url, '_blank');
        }else{
           alert('Preview url not found.')
        }
    });
}
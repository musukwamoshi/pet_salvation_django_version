
    $(document).ready(function(){


            "use strict";


            /*
            $.ajax({

                     url: "./index",
                     type: "GET",
                     dataType: "JSON",
                     success: function(data){

                              console.log(data);
                              show(data)

                     }

            });

            */
    
        
            $('a[href="#ClientDetails"]').addClass('active');
            //$("#ServiceDetails").removeClass('active');
            //$("#GPSCoordinates").removeClass('active');

            $('ul.dropdown-menu [data-toggle=dropdown]').on('click', function (event){

                    event.preventDefault();
                    event.stopPropagation();
                    $(this).parent().siblings().removeClass('open');
                    $(this).parent().toggleClass('open');

            });


            $(".pagination a").click(function(){
                         
                var theUrl = $(this).attr('href');
                $("#the-container").load(theUrl);

            });


            $("#search").keyup(function(){

                var theUrl = $(this).attr('href');
                $("#the-container").load(theUrl);
                $('#searchbar').css('display', 'block');

            });

            $('form').on('submit',function(e){

                    
                  showSecurityInput();


            });

            

            $('#category').on('focusout',function(event){


                 if(this.options[this.selectedIndex].value=="For Rent"){
                         
                        $('.for_rent').css('display','block');

                 }


                 if(this.options[this.selectedIndex].value=="For Sale"){
                         
                        $('.for_sale').css('display','block');

                 }

            });



            $('#securityyes').on('focusout',function(event){


                 if(this.options[this.selectedIndex].value=="Yes"){
                         
                        $('.securitydeposit').css('display', 'block');

                 }

            });
            


            function addFileInput() {
  
                    var html='';
                    html+='<div class="alert alert-success">';
                    html+='<button type="button"  class="close" data-dismiss="alert" arai-hidden="true">&times;</button>';
                    html+='<strong>Attach Image</strong>';
                    html+='<div class=form-group>';
                    html+='<input class="form-control" type="file" name="multipleFiles[]">';
                    html+='</div>';
                    html+='</div>';

                    $('div#uploadContainer').append(html); 


            }


            $('#addfile').on('click',function(event){

                            event.preventDefault;
                            addFileInput();

                    }
            );


            
            

            $('a[href="#search"]').click(function(){

                       $('#envelope1').css('display', 'block');
                       $('#envelope2').css('display', 'block');

            });


            function show(data) {
                    // Loop through passed data
                    var html='';
                    
                    data.ads.forEach(function(current,index,array){
                        //console.log(array);
                        html += '<div class="panel panel-default">';
                        html += '<div class="panel-body">';
                        html += '<table>';
                        html += '<tr><td style="width:50%"><strong>Date Posted:</strong>'+current.date_posted+'</td><td style=width:50%><strong>Town:</strong>'+current.town+'</td>'+'</tr>';
                        html += '<tr><td><strong>Description:</strong></td>'+'</tr>';
                        html += '<tr><td>'+current.description+'</td></tr>';
                        html += '</table>';
                        html += '</div>';
                        html += '</div>';
                    // Add the DOM to the page
                        $('#the-container').html(html);
                    });
                        html += data.links;
                        $('#the-container').html(html);


            }


            /*
            function success(position) {

                var latitude = position.coords.latitude.toFixed(7);             // set latitude variable
                var longitude = position.coords.longitude.toFixed(7);            // set longitude variable
            
                var mapcanvas = document.createElement('div');        // create div to hold map
                mapcanvas.id = 'map';                                       // give this div an id of 'map'
                mapcanvas.style.height = '400px';                           // set map height
                mapcanvas.style.width = '100%';                             // set map width
            
                document.querySelector('#map-container').appendChild(mapcanvas);    // place new div within the 'map-container' div
            
                var coords = new google.maps.LatLng(latitude,longitude);    // set lat/long object for new map
  
                var options = {                                             // set options for map
                    zoom: 20,
                    center: coords,
                    mapTypeControl: false,
                    navigationControlOptions: {
                    style: google.maps.NavigationControlStyle.SMALL
                    },
                    mapTypeId: 'satellite'
                };
            
                var map = new google.maps.Map(document.getElementById("map"), options); // create new map using settings above

                var marker = new google.maps.Marker({                       // place a marker at our lat/long
                    draggable:  true,
                    position:   coords,
                    animation: google.maps.Animation.BOUNCE,
                    map:        map
                });
            
                var response = 'Latitude: ' + latitude + ' / Longitude: ' + longitude;  // build string containing lat/long
                $("#location").val(response);                                           // write string to input field

            
                //event listener to get marker location
                google.maps.event.addListener(marker, 'drag', function(event){
                    document.getElementById("lati").value = event.latLng.lat().toFixed(5);
                    document.getElementById("long").value = event.latLng.lng().toFixed(5);
                });


            }

        */

        // check if browser supports the geolocation api
            /*

            if(navigator.geolocation){

                navigator.geolocation.getCurrentPosition(success); 
                    
            }else{ 

                $("#location").val('Your browser doesn\'t support the geolocation api.');
            
            }

            */


            $(".nav-tabs a").click(function(){

                 $(this).tab('show');
                 $('a.active').removeClass('active');

            
            });

            $('.nav-tabs a').on('shown.bs.tab', function(event){

        
                var x = $(event.target).text();         
                var y = $(event.relatedTarget).text();  
                $(".act span").text(x);
                $(".prev span").text(y);
                $(this).addClass('active');

            });


   });  





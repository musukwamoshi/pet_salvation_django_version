
//Author:Moshi Musukwa

    $(document).ready(function(){

        //initialize variables    
            var map;
            var town;
            var marker=[];

            "use strict";


            //ensures there is only ever one marker on the map

            function setMapOnAll(map){

                  for (var i = 0; i < markers.length; i++){
                       markers[i].setMap(map);
                  }
            }


    
        
            //$('a[href="#ClientDetails"]').addClass('active');
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

        //render file input html 
            function addFileInput() {
  
                    var html='';
                    html+='<div class="alert alert-info">';
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


            
            /*
            $.ajax({

                     url: url+"pet/index",
                     type: "GET",
                     dataType: "JSON",
                     success: function(data){

                              console.log(data);
                              show(data)

                     }

            });

            */

            //show search bar

            $('a[href="#search"]').click(function(){

                       $('#envelope1').css('display', 'block');
                       $('#hidesearch').css('display', 'block');
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


            //function initialize and center the map    
            function initMap(){

                    //initialize latitude and longitude
                    var lat = "-15.3875"; 
                    var lng = "28.3228";

                    lat=parseFloat(lat);
                    lng=parseFloat(lng);

                // set lat/long object for new map
                    var coords = new google.maps.LatLng(lat,lng); 


                // set options for map
                    var options = {                                             
                            zoom: 14,
                            center: coords,
                            mapTypeControl: true
                            //navigationControlOptions: {
                                    //style: google.maps.NavigationControlStyle.SMALL
                            //}
                            //mapTypeId:'hybrid'
                    };

                 // create div to hold map
                    var mapcanvas = document.createElement('div');

                // give this div an id of 'map'           
                    mapcanvas.id = 'map'; 

                // set map height                                          
                    mapcanvas.style.height = '400px';

                // set map width                               
                    mapcanvas.style.width = '100%';                             
            
                    document.querySelector('#map-container').appendChild(mapcanvas);

                // create new map object using settings above 
                    map = new google.maps.Map(document.getElementById("map"), options);

                //create marker 
                    var marker = new google.maps.Marker({
                            draggable: true,
                            position: coords,
                            animation: google.maps.Animation.BOUNCE,
                            map: map
                    });

                //add marker to array
                    markers.push(marker);

                    var response = 'Latitude: ' + lat + ' / Longitude: ' + lng;  // build string containing lat/long
                    $("#location").val(response);                                           // write string to input field

            
                //event listener to get marker location
                    google.maps.event.addListener(marker, 'drag', function(event){
                            document.getElementById("lati").value = event.latLng.lat().toFixed(5);
                            document.getElementById("long").value = event.latLng.lng().toFixed(5);
                    });


            }


           //initialize map if certain conditions are met
            if($('#map-container').length  && (typeof google === "object" || typeof google.map === "object")){

                            if(navigator.geolocation){

                                    initMap();  
                        
                            }else{ 

                                    $("#location").val('Your browser doesn\'t support the geolocation api.');
            
                            }
            }



        //when a town is selected get coordinates to center map in that town
            $("#town").change(function() {
                    
                    town = $('select[name="town"]').val();
                    
            });



        //code that gets town's coordinates
            function getTownLocation(){
                        
                        setMapOnAll(null);

                        $.getJSON("https://maps.googleapis.com/maps/api/geocode/json?address="+encodeURIComponent(town), function(val) {
                                if(val.results.length) {


                                    var location = val.results[0].geometry.location
                                    var latcoord=location.lat;
                                    var lngcoord=location.lng;

                                     //set lat long global variables
                                    var  townlat=parseFloat(latcoord);
                                    var  townlng=parseFloat(lngcoord);
                                    var coords = new google.maps.LatLng(townlat,townlng); 

                                    var marker = new google.maps.Marker({                       
                                            draggable:  true,
                                            position:   coords,
                                            animation: google.maps.Animation.BOUNCE,
                                            map:        map
                                    });
                                    markers.push(marker);

                                    marker.setPosition(new google.maps.LatLng({lat:townlat,lng:townlng}));
                                    map.panTo(new google.maps.LatLng({lat:townlat,lng:townlng}));

            
                                    var response = 'Latitude: ' + townlat + ' / Longitude: ' + townlng;  // build string containing lat/long
                                    $("#location").val(response);                                           // write string to input field

            
                                    //event listener to get marker location
                                    google.maps.event.addListener(marker, 'drag', function(event){
                                            document.getElementById("lati").value = event.latLng.lat().toFixed(5);
                                            document.getElementById("long").value = event.latLng.lng().toFixed(5);
                                    });


                                }
                        });


            }
            
            //centre map to selected town

            $("#form-location-tab").click(function(){

                
                if(town && (typeof google === "object" || typeof google.map === "object")){

                      getTownLocation();

                    
                }

                    

            });


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





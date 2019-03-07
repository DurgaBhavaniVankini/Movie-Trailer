f = open('movietrailers.html','w')

message ='''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
	 <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!--some meta data for search engine-->
    <meta name="description" content="Durga Bhavani - Student">
    <meta name="keywords"
          content="APSSDC, Portfolio, full-stack, frontend, web development, HTML, CSS, JS, JavaScript">
    <meta name="author" content="Durga Bhavani">
    <title>Movie Trailers</title>

    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script>
  
     $(document).on('click', '.trailer', function (event) {
            var youTubeId = $(this).attr('data-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + youTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        
      </script>
  
      <style>
      
        #trailer-video{
             width: 100%;
             height: 200%;
            }
         body{
             background-color:#787878;
            }
            .img-thumbnail{
            height: 90%;
            width: 80%;

            }
            .navbar-brand{
            color :#FFFFFF;
            font-size:150%;
            }
            
      </style>
  

     </head>
     <body>    
       
      
      <div class="container">
      <div class="navbar-header">
            <a class="navbar-brand" href="#">Movie Trailers</a>
      </div>
      </div>
     <br/>
    <div class="container">
    <div class="well well-small">
    <div class="form-group row">    
    <div class="col-md-4 trailer rounded-bottom" data-toggle="modal" data-target="#trailer" data-id="HG7Lv384yTU">
    <img src="https://i0.wp.com/www.andhrawatch.com/wp-content/uploads/2018/09/027-ONLINE-SENSOR-POSTER.jpg" class="img-thumbnail" alt="">
    </div>
    <div class="col-md-4 trailer rounded-bottom" data-toggle="modal" data-target="#trailer" data-id="SPG3L0s5dw0">
    <img src="https://i.pinimg.com/736x/29/b4/b5/29b4b52ccd830a5fc3c0bb6635e1969a.jpg" class="img-thumbnail" alt="">
    </div>
    <div class="col-md-4 trailer rounded-bottom" data-toggle="modal" data-target="#trailer" data-id="U3dqoAHqagk">
    <img src="https://moviegalleri.net/wp-content/uploads/2018/06/Vijay-Devarakonda-Rashmika-Mandanna-Geetha-Govindam-First-Look-Poster-HD.jpg" class="img-thumbnail" alt="">
    </div>
    </div>
    <div class="form-group row">
    <div class="col-md-4 trailer rounded-bottom" data-toggle="modal" data-target="#trailer" data-id="MIBAkM2IbhI">
    <img src="https://moviegalleri.net/wp-content/uploads/2018/09/Jr-NTR-Aravinda-Sametha-Audio-Release-Date-Sep-20th-Poster-HD.jpg" class="img-thumbnail" alt="">
    </div>
     <div class="col-md-4 trailer rounded-bottom" data-toggle="modal" data-target="#trailer" data-id="v8FEpl9QmFU">
    <img src="https://moviegalleri.net/wp-content/uploads/2018/07/Ramya-Krishnan-Naga-Chaitanya-Anu-Emmanuel-Shailaja-Reddy-Alludu-First-Look-Posters.jpg" class="img-thumbnail" alt="">
    </div>
    <div class="col-md-4 trailer rounded-bottom" data-toggle="modal" data-target="#trailer" data-id="EzUHxKhgHIs">
    <img src="https://www.filmibeat.com/img/220x100x275/popcorn/movie_posters/nannu-dochukunduvate-20180629110312-17237.jpg" class="img-thumbnail" alt="">
    </div>
    
    </div>
    </div>

    <div class="modal" id="trailer">
			<div class="modal-dialog">
				<!-- Modal content-->
				<div class="modal-content">
					 <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24" alt=""/>
          </a>
					

						 <div class="scale-media" id="trailer-video-container">
						 </div>

						
					
					
				</div>
			</div>     
		</div>
		
    </div>

    
   
    </body></html>'''

f.write(message)
f.close()

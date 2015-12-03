
for (i = 0; i < recipes.length; i++) {
  console.log('<img '+'src="../static/img/'+recipes[i]+'.jpg" >');
  $("#recipesLearnt").append('<img '+'src="../static/img/'+recipes[i]+'.jpg" class="img-circle">');

}

for (i = 0; i < recipesNotLearnt.length; i++) {
  console.log('<img '+'src="../static/img/'+recipes[i]+'.jpg" >');
  $("#recipesNotLearnt").append('<img '+'src="../static/img/'+recipesNotLearnt[i]+'.jpg" class="img-circle">');

}

$(document).ready(function(){
  console.log("in document ready");


    $(".gallery_small").click(function(){
        // console.log(Number($(this).attr("id")));
        current = Number($(this).attr("id"));

        $(".slider .slides").animate({
          'margin-left': '-=' +  ((current-1) * width),
        }, 500
        );

        $("#default_gallery").fadeOut(1000);
        $(".slider").delay(1000).fadeIn(1000);
    });

});


for (i = 0; i < recipes.length; i++) {
  console.log('<a href="/yuecai/'+recipes[i]+'"><img '+'src="../static/img/'+recipes[i]+'.jpg" class="img-circle"> </a>');
  $("#recipesLearnt ul").append('<li><a href="/yuecai/ class="trigger"'+recipes[i]+'"><img '+'src="../static/img/'+recipes[i]+'.jpg" class="img-circle"> <span class="text-content"><span>'+recipes[i].replace(/_/g," ")+'</span></span></a></li>');

}

for (i = 0; i < recipesNotLearnt.length; i++) {
  console.log('<a href="/yuecai/'+recipesNotLearnt[i]+'"><img '+'src="../static/img/'+recipesNotLearnt[i]+'.jpg" class="img-circle"> <span class="img-text"><span>'+recipesNotLearnt[i]+'</span></span></a>');
  $("#recipesNotLearnt ul").append('<li><a href="/yuecai/ class="trigger"'+recipesNotLearnt[i]+'"><img '+'src="../static/img/'+recipesNotLearnt[i]+'.jpg" class="img-circle"><span class="text-content"><span>'+recipesNotLearnt[i].replace(/_/g," ")+'</span></span> </a></li>');

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

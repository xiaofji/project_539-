
for (i = 0; i < recipes.length; i++) {
  $("#recipesLearnt ul").append('<li><a href="/yuecai/'+recipes[i]+'" class="trigger"><img '+'src="../static/img/'+recipes[i]+'.jpg" class="img-circle" alt = "'+recipes[i]+'"> <span class="text-content"><span><p>'+recipes[i].replace(/_/g," ")+'</p><p class="clickToLearn">click to review!</p></span></span></a></li>');

}

for (i = 0; i < recipesNotLearnt.length; i++) {
  $("#recipesNotLearnt ul").append('<li><a href="/yuecai/'+recipesNotLearnt[i]+'"  class="trigger"><img '+'src="../static/img/'+recipesNotLearnt[i]+'.jpg" class="img-circle" alt = "'+recipes[i]+'"><span class="text-content"><span><p>'+recipesNotLearnt[i].replace(/_/g," ")+'</p><p class="clickToLearn">click to learn!</p></span></span> </a></li>');

}

$(document).ready(function(){

    $(".gallery_small").click(function(){
        current = Number($(this).attr("id"));

        $(".slider .slides").animate({
          'margin-left': '-=' +  ((current-1) * width),
        }, 500
        );

        $("#default_gallery").fadeOut(1000);
        $(".slider").delay(1000).fadeIn(1000);
    });

});

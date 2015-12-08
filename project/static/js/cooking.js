$(function(){
  num_material = materials.length;
  foodstep= steps1.slice(0);
  totalstep = foodstep.length;

  if(($(window).width())<=822)
  {
    $("#brand").text("Chinese Cooking Alchemy");
    $("#logo").attr("src","");
  }
  else{
    $("#brand").text("");
    $("#logo").attr("src","../static/img/logo.jpg");

  }

  $("#repeat").click(function(){
    if(foodstep[currentstep]=="add")
    {
      lock = 1;
      $("#drop"+currentmaterial).attr("id","material");
      $("#material").css({height:"150px",position: "absolute",top:"20px",bottom:"auto",right: "20px",left:"auto"});
      addmaterial();
    }
  });
  $("#prestep").click(function(){
    currentstep--;
    $("#addbutton").attr("class","hidden form-addrecipe");
    if(foodstep[currentstep+1]=="add")
    {
      $("#drop"+currentmaterial).remove();
      currentmaterial--;
    }
    if(foodstep[currentstep]=="add")
    {
      lock = 1;
      $("#drop"+currentmaterial).remove();
      $("#cookpage").append('<img id = "material"  alt="material">');
      $("#material").css({height:"150px",position: "absolute",top:"20px",bottom:"auto",right: "20px",left:"auto"});
      addmaterial();
    }
    else {
      lock = 0;
      $("#speech").text(foodstep[currentstep]);
    }
    icon();
  });
  $("#nextstep").click(function(){

    currentstep++;
    if(currentstep==totalstep-1){
      $("#addbutton").attr("class","form-addrecipe");
    }
    else{
      $("#addbutton").attr("class","hidden form-addrecipe");
    }
    if(foodstep[currentstep]=="add")
    {
      currentmaterial++;
      lock = 1;
      $("#cookpage").append('<img id = "material"  alt="material">');
      $("#material").css({height:"150px",position: "absolute",top:"20px",bottom:"auto",right: "20px",left:"auto"});
      addmaterial();
    }
    else {
      lock = 0;
      $("#speech").text(foodstep[currentstep]);
    }
    icon();
  });
});



function drag() {
  var $material = $( "#material" ),$dropbox = $( "#dropbox" );
  $material.draggable({cancel: "a.ui-icon", revert: "invalid", cursor: "move"});
  $dropbox.droppable({accept: "#material",
    drop: function( event, ui ) {
      $("#speech").text("You did it! Let's move to the next step");
      $("#prestep").attr('class', 'fa fa-backward fa-5x');
      $("#nextstep").attr('class', 'fa fa-forward fa-5x');
      $("#material").attr("id","drop"+currentmaterial);
      $("#dropbox").text("");
      $("#drop"+currentmaterial).css({position:"absolute",height: "70px", width:"auto", bottom:"10px",top:"auto"});
      lock = 0;
    }
  });
};

function addmaterial()
{
  $("#dropbox").text("Drop here!");
  $("#prestep").attr("class","nothing");
  $("#nextstep").attr("class","nothing");
  $("#speech").text("Add the " +materials[currentmaterial]+" in to the pot. Please drag drop it on the right place");
  // $("#material").attr("src","../static/img/"+materials[currentmaterial]+".jpg");
  $("#material").attr("src",materialsurl[currentmaterial]);

  drag();
};

function icon()
{
  if(currentstep==0)
  {
    $("#prestep").attr("class","nothing");
  }
  else if(currentstep == totalstep-1)
  {
    $("#nextstep").attr("class","nothing");
  }
  else if(lock==0){
    $("#prestep").attr("class","fa fa-backward fa-5x");
    $("#nextstep").attr("class","fa fa-forward fa-5x");
  }
};

var lock = 0;
var currentmaterial = -1;
var currentstep = 0;
var totalstep;
var num_materials;
var ingres;
// var steps1 = ["Hello! Welcome to my kitchen.","Today I am going to teach you how to make the sliced cold chicken.",
//               "Cut a chicken to small pieces",
//               "add",
//               "add",
//               "Boil the chicken for 10 mins",
//               "Poul out all the water",
//               "add",
//               "Cut the greenonions",
//               "add",
//               "Congratuations! You have finished learning this dish!"];
var foodstep;

$(function(){

  console.log(materials[3]);
  num_material = materials.length;
  foodstep= steps1.slice(0);
  totalstep = foodstep.length;

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
  $("#speech").text("Add the" +materials[currentmaterial]+" in to the pot. Please drag drop it on the right place");
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

function changeimage(id)
{
  currentmaterial = id;
  document.getElementById("displayimg").src = "static/img/"+id+"cai.jpg";
  var elems = document.getElementsByClassName("dish");
  for(var i = 0; i < elems.length; i++) {
    elems[i].style.backgroundColor = "rgba(0,0,0,0)";
  }
  document.getElementById(id).style.backgroundColor = "rgba(36,110,166,0.5)";
  if(id == "eight"){
    document.getElementById("short").innerHTML = "八大菜系---Eight best culinary traditions";
    document.getElementById("long").innerHTML = "Sichuan and Hunan cuisines: hot spice. Anhui and Fujian cuisines: inclusion of wild foods from their mountains. Guangdong (Cantonese), Fujian, Zhejiang, Jiangsu: great seafood, and generally sweet and light flavors. Shandong Cuisine: fresh and salty with a lot of seafood dishes.";
    document.getElementById("learnlink").innerHTML = "";
    document.getElementById("loginlink").innerHTML = "";
    document.getElementById("logintext").innerHTML = "";
  }
  else{
    document.getElementById("learnlink").innerHTML = "Learn how to cook.";
    document.getElementById("loginlink").innerHTML = "log in";
    document.getElementById("logintext").innerHTML = "to learn how to cook.";
    if(id == "yue"){
      document.getElementById("short").innerHTML = "粤菜 Yuècài---Sweeter, favoring braising and stewing, adding various mild sauces.";
      document.getElementById("long").innerHTML = "Cantonese food is the most popular style internationally.Guangdong Province and Hong Kong are noted for fine seafood dishes and rice dishes. They eat a very wide variety of foods. The dishes they serve don't have strong flavors since it is lightly seasoned, and they often tend to be a little sweet.";
      document.getElementById("learnlink").href = "/yuecai/sliced_cold_chicken";
    }
    else if(id == "chuan"){
      document.getElementById("short").innerHTML = "川菜 Chuāncài---Spicy and bold, often mouth-numbing, using lots of chili, garlic, ginger, and peanuts";
      document.getElementById("long").innerHTML = "Sichuan Province produced the most widely served cuisine in China. Their dishes are famous for their hot-spicy taste and the numbing flavor of Sichuan peppercorn that is rare in other regional cuisines. It is the food of Chengdu and Chongqing (which used to be part of Sichuan).";
      document.getElementById("learnlink").href = "/yuecai/sichuan_fish";
    }
    else if(id == "su"){
      document.getElementById("short").innerHTML = "苏菜 Sūcài---Fresh, moderately salty and sweet, precise cooking techniques, favoring seafood, soups and artistic, colorful presentation";
      document.getElementById("long").innerHTML = "Jiangsu Province and China's biggest city, Shanghai, have a very refined gourmet cuisine that is often served at government banquets. What makes it special is the exquisite cooking techniques that produce richly aromatic and visually artistic dishes. Their chefs also focus on serving meals that promote health.";
      document.getElementById("learnlink").href = "/yuecai/bitter_shrimp_ball";
    }
    else if(id == "zhe"){
      document.getElementById("short").innerHTML = "浙菜 Zhècài---Mellow, using fresh seafood, freshwater fish, and bamboo shoots, and a wide variety of cooking methods.";
      document.getElementById("long").innerHTML = "Zhejiang Province is the province south of Jiangsu, and it borders on Shanghai too, so their style is similar to theirs, but it is less elaborately prepared. They focus more on serving fresh food. The food is often served raw or almost raw and is fresh and crispy and seasonal. It is more like Japanese food. Ningbo cuisine is very salty.";
    }
    else if(id == "min"){
      document.getElementById("short").innerHTML = "闽菜 Mǐncài---Lighter, with a mild sweet and sour taste, using ingredients from the sea and the mountains.";
      document.getElementById("long").innerHTML = "Fujian Province is known for great seafood and soups and the precise use of scintillating but not tongue numbing spices. Adding much wild exotic delicacies from the sea and mountains makes their dishes have unusual flavors. It is like a culinary wild adventure.";
    }
    else if(id == "xiang"){
      document.getElementById("short").innerHTML = "湘菜 Xiāngcài---Quite spicy, with a hot and sour taste, favoring sautéing, stir-frying, steaming and smoking";
      document.getElementById("long").innerHTML = "If you like Sichuan food, you'll probably like Hunan food too since it is even hotter. It is tastier and more delicious because they don't use peppercorn that numbs the mouth. It is a rich agricultural area that produces a broad range of vegetables and herbs, and these are served up.";
    }
    else if(id == "hui"){
      document.getElementById("short").innerHTML = "徽菜 Huīcài---Uses many wild plants and animals as ingredients, favoring stewing and more oil";
      document.getElementById("long").innerHTML = "Anhui cuisine is even wilder than Fujian cuisine. It is inland, and big mountains such as the Yellow Mountains are the source of lots of different wild foods and herbs. It is basically a hearty mountain peasant food. Some of the best dishes incorporate wild food for an unusual taste. Some dishes are sweet from added sugar.";
    }
    else if(id == "lu"){
      document.getElementById("short").innerHTML = "鲁菜 Lǔcài---Salty and crispy, favoring braising and seafood";
      document.getElementById("long").innerHTML = "Shandong was one of the first civilized areas, and it set the pattern for northern styles of cooking. With a long coast, seafood is its forte. They preserve the original taste of the seafood by using simple ingredients and braising, and they like vinegar and salt. Unlike southern cuisines, they serve much more wheat food, including their noodles.";
    }
  }

}

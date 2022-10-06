var socket;
var hold = false;

function initMap() {
  var uluru = {
    lat: -25.344,
    lng: 131.036
  };
  var map = new google.maps.Map(
    document.getElementById('map'), {
      zoom: 4,
      center: uluru
    });
  var marker = new google.maps.Marker({
    position: uluru,
    map: map
  });
}

function buttonPressed(btn,key){
  $('#'+btn).addClass("active");
  console.log(hold);
  if(key && !hold){
    socket.emit('move',key);
  }
  hold = true;
}
function initMap() {
  var myLatLng = {
      lat: -25.363,
      lng: 131.044
  };

  var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 4,
      center: myLatLng
  });

  var marker = new google.maps.Marker({
      position: myLatLng,
      map: map
  });
}

function buttonRelease(btn,key){
  hold = false;
  $('#'+btn).removeClass("active");
  if(key){
    socket.emit('move','s');
  }
}

function getBase64Image(img) {
  var canvas = document.createElement("canvas");
  canvas.width = img.width;
  canvas.height = img.height;
  var ctx = canvas.getContext("2d");
  ctx.drawImage(img, 0, 0);
  var dataURL = canvas.toDataURL("image/jpeg");
  return dataURL;
}

function captureImage(){
  let date = new Date();
  let fileName = date.toLocaleDateString().replace(new RegExp('/',"g"),'-')+'_'+date.toLocaleTimeString().replace(new RegExp(':',"g"),'-').replace(new RegExp(' ',"g"),'-')+'.jpg';
  let ele = $('#currentImage');
  let b64 = getBase64Image(document.getElementById('currentImage'));
  let link = document.createElement('a')
  link.href = b64;
  link.download = fileName;
  $('#captured-image').html("");
  $('#captured-image').append(link);
  link.click();
}
function initSocketIO() {
       socket = io.connect('//' + document.domain + ':' + location.port);
}
$(document).ready(function(){
  initSocketIO();
  //KeyPress Event
  $(document).keydown(function(e){
    let key = e.originalEvent.key;
    switch (key) {
      case 'ArrowUp': buttonPressed('camera-up','u'); break;
      case 'w' : buttonPressed('forward-button','f'); break;
      case 'ArrowDown':buttonPressed('camera-down','d');break;
      case 's' : buttonPressed('back-button','b'); break;
      case 'ArrowLeft':buttonPressed('camera-left','x');break;
      case 'a' : buttonPressed('left-button','l'); break;
      case 'ArrowRight':buttonPressed('camera-right','y');break;
      case 'd' : buttonPressed('right-button','r'); break;
      case ' ': buttonPressed('capture-button'); break;
      case 'q' : socket.emit('move','q');
      default:
    }
  });
  //KeyRelease Event
  $(document).keyup(function(e){
    let key = e.originalEvent.key;
    switch (key) {
      case 'ArrowUp':buttonRelease('camera-up');break;
      case 'w' : buttonRelease('forward-button','f'); break;
      case 'ArrowDown':buttonRelease('camera-down');break;
      case 's' : buttonRelease('back-button','b'); break;
      case 'ArrowLeft':buttonRelease('camera-left');break;
      case 'a' : buttonRelease('left-button','l'); break;
      case 'ArrowRight':buttonRelease('camera-right');break;
      case 'd' : buttonRelease('right-button','r'); break;
      case ' ' :  buttonRelease('capture-button'); captureImage();break;
      default:
    }
  });
  //Scroll up events
  $(document).bind('DOMMouseScroll mousewheel',function(e){
    if(e.originalEvent.wheelDelta/120 > 0 || e.originalEvent.detail < 0){
      buttonPressed('camera-up','u');
      setTimeout(function(){
        buttonRelease('camera-up','u');
      },250);
    }else{
      buttonPressed('camera-down','d');
      setTimeout(function(){
        buttonRelease('camera-down','d');
      },250);
    }
  })

});

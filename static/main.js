$(document).ready(function () {
  if (localStorage.selected) {
    $('#' + localStorage.selected).attr('checked', true);
  }
  $('.db').click(function () {
    localStorage.setItem("selected", this.id);
  });
});
$(document).ready(function () {
  if (localStorage.selected) {
    $('#' + localStorage.selected1).attr('checked', true);
  }
  $('.db_config').click(function () {
    localStorage.setItem("selected1", this.id);
  });
});
$(document).ready(function () {
  if (localStorage.selected) {
    $('#' + localStorage.selected2).attr('checked', true);
  }
  $('.alg').click(function () {
    localStorage.setItem("selected2", this.id);
  });
});
$(document).ready(function () {
  if (localStorage.selected) {
    $('#' + localStorage.selected3).attr('checked', true);
  }
  $('.norm').click(function () {
    localStorage.setItem("selected3", this.id);
  });
});

$(document).ready(function () {
  var item = window.localStorage.getItem('selectedkn');
  $('select[name=kn]').val(item);
  $('select[name=kn]').change(function () {
    window.localStorage.setItem('selectedkn', $(this).val());
  });
});
$(document).ready(function () {
  var item = window.localStorage.getItem('selectedke');
  $('select[name=ke]').val(item);
  $('select[name=ke]').change(function () {
    window.localStorage.setItem('selectedke', $(this).val());
  });
});
$(document).ready(function () {
  var item = window.localStorage.getItem('selectedkl');
  $('select[name=kl]').val(item);
  $('select[name=kl]').change(function () {
    window.localStorage.setItem('selectedkl', $(this).val());
  });
});

$(document).ready(function () {
  var item = window.localStorage.getItem('selected2');
  if (item == "alg1") {
    $('.kval1').hide();
    $('.kval2').hide();
    $('.kval3').hide();
    $('.ppbtn').hide();
    $('.cdbradios').show();
    $('.normradios').show();
  }
  if (item == "alg2") {
    $('.kval1').show();
    $('.kval2').hide();
    $('.kval3').hide();
    $('.ppbtn').hide();
    $('.cdbradios').show();
    $('.normradios').show();
  }
  if (item == "alg3") {
    $('.ppbtn').show();
    $('.kval2').show();
    $('.kval1').hide();
    $('.kval3').hide();
    $('.cdbradios').show();
    $('.normradios').show();
  }
  if (item == "alg4") {
    $('.ppbtn').show();
    $('.kval3').show();
    $('.kval1').hide();
    $('.kval2').hide();
    $('.cdbradios').show();
    $('.normradios').show();
  }
});
$(document).ready(function () {
  var item = window.localStorage.getItem('selected1');
  if (item == "db_config1") {
    $('.p1').show();
    $('.p2').hide();
    $('.p3').hide();
  }
  if (item == "db_config2") {
    $('.p1').hide();
    $('.p2').show();
    $('.p3').hide();
  }
  if (item == "db_config3") {
    $('.p1').hide();
    $('.p2').hide();
    $('.p3').show();
  }
});

$(document).ready(function () {
  $(".ppbtn").click(function(){
    $('.searchbtn').show();
  });
  $(".kval2").click(function(){
    $('.searchbtn').hide();
  });
  $(".kval3").click(function(){
    $('.searchbtn').hide();
  });
  $("#db_config1").click(function(){
    $('.p1').show();
    $('.p2').hide();
    $('.p3').hide();
    $('.searchbtn').hide();
  });
  $("#db_config2").click(function(){
    $('.p1').hide();
    $('.p2').show();
    $('.p3').hide();
    $('.searchbtn').hide();
  });
  $("#db_config3").click(function(){
    $('.p1').hide();
    $('.p2').hide();
    $('.p3').show();
    $('.searchbtn').hide();
  });
  $('#alg1').click(function () {
    $('.kval1').hide();
    $('.kval2').hide();
    $('.kval3').hide();
    $('.ppbtn').hide();
    $('.searchbtn').show();
    $('.cdbradios').show();
    $('.normradios').show();
  });
  $('#alg2').click(function () {
    $('.kval1').show();
    $('.kval2').hide();
    $('.kval3').hide();
    $('.ppbtn').hide();
    $('.searchbtn').show();
    $('.cdbradios').show();
    $('.normradios').show();
  });
  $('#alg3').click(function () {
    $('.ppbtn').show();
    $('.kval2').show();
    $('.kval1').hide();
    $('.kval3').hide();
    $('.searchbtn').hide();
    $('.cdbradios').show();
    $('.normradios').show();
  });
  $('#alg4').click(function () {
    $('.ppbtn').show();
    $('.kval3').show();
    $('.kval1').hide();
    $('.kval2').hide();
    $('.searchbtn').hide();
    $('.cdbradios').show();
    $('.normradios').show();
  });
});

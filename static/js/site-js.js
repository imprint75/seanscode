// Base javascript file 
 
var siteBase = (function(){
    var itemList = [];
    return {
	init : function(args){
	    for(i in args.init){
		args.init[i]();
	    }
	}
    };
})();

var layout = {
    initSearchBars : function(){
	$('.txtClass').focus(function(){
	    if ( $(this).val() == $(this).attr('defaultVal') ){
		$(this).val('');
	    }
	});

	$('.txtClass').blur(function(){
	    if ( $(this).val() == '' ){
		$(this).val($(this).attr('defaultVal'));
	    }
	});
    }
};

var data = {
    getData : function(){
	console.log("inside getData");
    }
};

$('body').ready(function(){
  var init = [
      layout.initSearchBars,
      data.getData
  ];

  siteBase.init({"init" : init, "message" : "transmission"});
});
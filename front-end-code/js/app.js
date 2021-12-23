const inputs = document.querySelectorAll(".input");

function focusFunction(){
    let parentNode = this.parentNode.parentNode;
    parentNode.classList.add('focus');
}
function blurFunction(){
    let parentNode = this.parentNode.parentNode;
    if(this.value == ''){
        parentNode.classList.remove('focus');
    }
}

inputs.forEach(input=>{
    input.addEventListener('focus',focusFunction);
    input.addEventListener('blur',blurFunction);
});


//ajax:
$(function(){
    $("#register").click(function() {
        var para={
            stunum:$("#stunum").val(),
            stuphone:$("#stuphone").val(),
            stupwd:$("#stupwd").val(),
			stuemail:$("#stuemail").val(),
			stuface:cameraForm.base64Img
        }

        $.ajax({
            url:"http://192.168.160.135:5000/register",
            type:"Post",
            data:para,
            datatype:"html",
            success:function(data){
                eval(data);
            }
        });
    });
	$("#changepwd").click(function() {
	    var para={
	        user:$("#user").val(),
	        ver_code:$("#ver_code").val(),
	        stupwd:$("#stupwd").val(),
			stupwd2:$("#stupwd2").val()
	    }
	
	    $.ajax({
	        url:"/ayUser/check",//加网页的路径
	        url:"http://192.168.160.135:5000/find_pwd",//加网页的路径
	        type:"Post",
	        data:para,
	        datatype:"html",
	        success:function(data){
	            eval(data);
	        }
	    });
	});
	$("#sendcode").click(function() {

		
	    var para={
	        user:$("#user").val()
	    }
	
	    $.ajax({
	        url:"/ayUser/check",//加网页的路径
	        url:"http://192.168.160.135:5000/send_code",//加网页的路径
	        type:"Post",
	        data:para,
	        datatype:"html",
	        success:function(data){
	            eval(data);
	        }
	    });
		
	});
	$("#sendcode2").click(function() {
	
		
	    var para={
	        user:$("#user2").val()
	    }
	
	    $.ajax({
	        url:"/ayUser/check",//加网页的路径
	        url:"http://192.168.160.135:5000/send_code",//加网页的路径
	        type:"Post",
	        data:para,
	        datatype:"html",
	        success:function(data){
	            eval(data);
	        }
	    });
		
	});
	$("#login").click(function() {
	    var para={
	        user:$("#user").val(),
	        pwd:$("#stupwd").val()
	    }
	
	    $.ajax({
	        url:"/ayUser/check",//加网页的路径
	        url:"http://192.168.160.135:5000/pwd_login",//加网页的路径
	        type:"Post",
	        data:para,
	        datatype:"html",
	        success:function(data){
	            eval(data);
	        }
	    });
	});
	
	$("#login2").click(function() {
	    var para={
	        user:$("#user2").val(),
	        ver_code:$("#ver_code2").val()
	    }
	
	    $.ajax({
	        url:"/ayUser/check",//加网页的路径
	        url:"http://192.168.160.135:5000/code_login",//加网页的路径
	        type:"Post",
	        data:para,
	        datatype:"html",
	        success:function(data){
	            eval(data);
	        }
	    });
	});
	
	
	
	$(function() {
	    var btn = $("#sendcode");
	    $(function() {
	        btn.click(settime);
	    })
	    var countdown = 30;//倒计时总时间，为了演示效果，设为5秒，一般都是60s
	    function settime() {
	        if (countdown == 0) {
	            btn.attr("disabled", false);
	            btn.html("获取验证码");
	            btn.removeClass("disabled");
				$("#sendcode").css("background-image", "linear-gradient(to right,#32be8f,#38d39f,#32be8f)");
	            countdown = 30;
	            return;
	        } else {
				$("#sendcode").css("background-image", "linear-gradient(to right,#bdbeb3,#bdbeb3,#bdbeb3)");
				
				// $("#sendcode").css("cursor", "not-allowed");
				// $("#sendcode").css("pointer-events", "none");
	            btn.addClass("disabled");
	            btn.attr("disabled", true);
	            btn.html("重新发送(" + countdown + ")");
	            countdown--;
	        }
	        setTimeout(settime, 1000);
	    }
	
	})
	
	$(function() {
	    var btn = $("#sendcode2");
	    $(function() {
	        btn.click(settime);
	    })
	    var countdown = 30;//倒计时总时间，为了演示效果，设为5秒，一般都是60s
	    function settime() {
	        if (countdown == 0) {
	            btn.attr("disabled", false);
	            btn.html("获取验证码");
	            btn.removeClass("disabled");
				$("#sendcode2").css("background-image", "linear-gradient(to right,#32be8f,#38d39f,#32be8f)");
	            countdown = 30;
	            return;
	        } else {
				$("#sendcode2").css("background-image", "linear-gradient(to right,#bdbeb3,#bdbeb3,#bdbeb3)");
				
				// $("#sendcode").css("cursor", "not-allowed");
				// $("#sendcode").css("pointer-events", "none");
	            btn.addClass("disabled");
	            btn.attr("disabled", true);
	            btn.html("重新发送(" + countdown + ")");
	            countdown--;
	        }
	        setTimeout(settime, 1000);
	    }
	
	})
	
	
	

    $("input").each(function (i, domEle) {
        $(domEle).keyup(function () {
            if (i == 0) {
                if ($(this).val().length != 13) {
                    $(this).siblings(".tip").show();
                }else {
                    $(this).siblings(".tip").hide();
                }
            }
            if (i == 1) {
                if ($(this).val().length < 11) {
                    $(this).siblings(".tip").show();
                }else {
                    $(this).siblings(".tip").hide();
                }
            }
            if (i == 2) {
                if ($(this).val().length < 6) {
                    $(this).siblings(".tip").show();
                }else {
                    $(this).siblings(".tip").hide();
                }
            }
        })
    })
});
let cameraForm = {
    video: null,
    base64Img: "",
    open: function () {
        // 视频大小
        let constraints = {audio: false, video: {width: 250, height: 250}};
        // 开启视频
        navigator.mediaDevices.getUserMedia(constraints).then(function (mediaStream) {
            cameraForm.video = document.querySelector('video');
            cameraForm.video.srcObject = mediaStream;
            cameraForm.video.onloadedmetadata = function (e) {
                cameraForm.video.play();
            };
        }).catch(function (err) {
            console.log(err.name + ": " + err.message);
            alert("摄像头打开失败")
        });
    },
    close: function () {
        //关闭摄像头
        cameraForm.video.srcObject.getTracks()[0].stop();
    },
    save: function () {
        // 使用canvas进行拍照
        let canvas = document.getElementById('canvas');
        let ctx = canvas.getContext('2d');
		canvas.setAttribute("width", cameraForm.video.videoWidth);
		canvas.setAttribute("height", cameraForm.video.videoHeight);
        ctx.drawImage(cameraForm.video, 0,0,cameraForm.video.videoWidth, cameraForm.video.videoHeight);
		cameraForm.base64Img = canvas.toDataURL("image/png");
		// alert(cameraForm.base64Img);
        // document.getElementById('picture').src = cameraForm.base64Img;
    }
};
// $(function () {
//     cameraForm.open();
 
// });
$(function(){
	$("#facelogin").click(function() {
			$(function() {
				// cameraForm.close();
				// $("#video").attr("src",cameraForm.base64Img );
				
			});
			var para={
				face:cameraForm.base64Img
			}
			$.ajax({
				url:"/ayUser/check",//加网页的路径
				url:"http://192.168.160.135:5000/face_login",//加网页的路径
				type:"Post",
				data:para,
				datatype:"html",
				success:function(data){
					eval(data);
				}
			});
	});	
	

	$("#facebind").click(function() {
			$(function() {
				cameraForm.save();
				// cameraForm.close();
				alert('已选择人脸');
				cameraForm.close();
				// $("#video").attr("src",cameraForm.base64Img );
				
			});
			var para={
				face:cameraForm.base64Img
			}
			// $.ajax({
			// 	url:"/ayUser/check",//加网页的路径
			// 	url:"http://192.168.160.135:5000/face_login",//加网页的路径
			// 	type:"Post",
			// 	data:para,
			// 	datatype:"html",
			// 	success:function(data){
			// 		eval(data);
			// 	}
			// });
	});
});
